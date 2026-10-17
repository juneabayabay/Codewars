"""Turn accepted commands into events. Rejected commands stay off the match log."""

from __future__ import annotations

from typing import Any

from game.bus import EventBus
from game.commands import (
    Command,
    CommandRejected,
    Face,
    HoldYield,
    Move,
    Pause,
    ReleaseYield,
    Resume,
    StartMatch,
    Strike,
)
from game.events import (
    MatchPaused,
    MatchResumed,
    MatchStarted,
    StrikeStarted,
    VillainFaced,
    VillainMoved,
    YieldCancelled,
    YieldStarted,
)
from game.model import (
    ROOM_HEIGHT,
    ROOM_WIDTH,
    BodyState,
    Facing,
    Match,
    Phase,
    Villain,
    VillainId,
    opening_loadouts,
)
from game.spec_ids import SPEC_1, SPEC_2, SPEC_3, SPEC_7, SPEC_9, SPEC_12, SPEC_18, SPEC_20


_DIRECTION = {
    Facing.N: (0.0, -1.0),
    Facing.E: (1.0, 0.0),
    Facing.S: (0.0, 1.0),
    Facing.W: (-1.0, 0.0),
}


def handle_input(match: Match, commands: list[Command], bus: EventBus, dt_ms: int) -> None:
    moved: set[VillainId] = set()
    for command in commands:
        spec_id = _rejection_spec(match, command)
        if spec_id is not None:
            match.rejections.append(CommandRejected(command, spec_id))
            continue
        if isinstance(command, StartMatch):
            bus.emit(
                MatchStarted(
                    seed=command.seed,
                    room_width=ROOM_WIDTH,
                    room_height=ROOM_HEIGHT,
                    loadouts=opening_loadouts(),
                )
            )
        elif isinstance(command, Face):
            _face(match, command, bus)
        elif isinstance(command, Move):
            _move(match, command, bus, dt_ms)
            moved.add(command.villain_id)
        elif isinstance(command, Strike):
            _strike(match, command, bus)
        elif isinstance(command, HoldYield):
            _hold_yield(match, command, bus)
        elif isinstance(command, ReleaseYield):
            bus.emit(YieldCancelled(command.villain_id, "RELEASED"))
        elif isinstance(command, Pause):
            bus.emit(MatchPaused())
        elif isinstance(command, Resume):
            bus.emit(MatchResumed())
    _release_unheld_moves(match, moved)


def _hold_yield(match: Match, command: HoldYield, bus: EventBus) -> None:
    villain = match.villains[command.villain_id]
    if villain.yield_started_ms is not None:
        return
    bus.emit(YieldStarted(villain.id))


def _strike(match: Match, command: Strike, bus: EventBus) -> None:
    villain = match.villains[command.villain_id]
    bus.emit(StrikeStarted(villain.id, villain.facing, villain.menace >= 100))


def _face(match: Match, command: Face, bus: EventBus) -> None:
    villain = match.villains[command.villain_id]
    if villain.facing is command.facing:
        return
    bus.emit(VillainFaced(villain.id, command.facing))


def _move(match: Match, command: Move, bus: EventBus, dt_ms: int) -> None:
    villain = match.villains[command.villain_id]
    destination = _clamped_destination(
        villain,
        command.facing,
        dt_ms,
        match.room_width,
        match.room_height,
    )
    bus.emit(VillainMoved(villain.id, (villain.x, villain.y), destination))


def _clamped_destination(
    villain: Villain,
    facing: Facing,
    dt_ms: int,
    room_width: int,
    room_height: int,
) -> tuple[float, float]:
    dx, dy = _DIRECTION[facing]
    if dx > 0:
        distance_to_edge = room_width - villain.x
    elif dx < 0:
        distance_to_edge = villain.x
    elif dy > 0:
        distance_to_edge = room_height - villain.y
    else:
        distance_to_edge = villain.y
    if distance_to_edge < 0:
        distance_to_edge = 0
    step = villain.speed * (dt_ms / 1000)
    if step > distance_to_edge:
        step = distance_to_edge
    x = villain.x + dx * step
    y = villain.y + dy * step
    if x < 0:
        x = 0.0
    elif x > room_width:
        x = float(room_width)
    if y < 0:
        y = 0.0
    elif y > room_height:
        y = float(room_height)
    return (x, y)


def _release_unheld_moves(match: Match, moved: set[VillainId]) -> None:
    if match.phase is not Phase.LIVE or match.paused:
        return
    for villain in match.villains.values():
        if villain.id in moved or villain.state is not BodyState.MOVING:
            continue
        villain.state = BodyState.IDLE


def _rejection_spec(match: Match, command: Command) -> str | None:
    if isinstance(command, StartMatch):
        if match.phase in (Phase.BOOT, Phase.RESOLVED):
            return None
        return SPEC_1

    if match.phase is Phase.RESOLVED or match.resolved_latch:
        return SPEC_7

    if isinstance(command, Pause):
        if match.phase in (Phase.COUNTDOWN, Phase.LIVE) and not match.paused:
            return None
        return SPEC_2

    if isinstance(command, Resume):
        if match.paused:
            return None
        return SPEC_2

    if isinstance(command, ReleaseYield):
        villain = match.villains.get(command.villain_id)
        if villain is None or villain.yield_started_ms is None:
            return SPEC_20
        return None

    if not isinstance(command, (Move, Face, Strike, HoldYield)):
        return SPEC_1

    if match.phase is not Phase.LIVE or match.paused:
        return SPEC_2

    villain: Any = match.villains.get(command.villain_id)
    if villain is None:
        return SPEC_1

    if isinstance(command, HoldYield):
        if command.villain_id is not VillainId.A:
            return SPEC_3
        if villain.state in (BodyState.BROKEN, BodyState.YIELDED):
            return SPEC_9
        if villain.state not in (BodyState.IDLE, BodyState.MOVING, BodyState.HURT):
            return SPEC_2
        return None

    if isinstance(command, Move):
        if villain.state in (BodyState.BROKEN, BodyState.YIELDED):
            return SPEC_9
        if villain.state not in (BodyState.IDLE, BodyState.MOVING):
            return SPEC_2
        return None

    if isinstance(command, Face):
        if villain.state in (BodyState.BROKEN, BodyState.YIELDED):
            return SPEC_9
        return None

    if villain.state in (BodyState.BROKEN, BodyState.YIELDED):
        return SPEC_9
    if villain.state is BodyState.STRIKING:
        return SPEC_18
    if villain.state not in (BodyState.IDLE, BodyState.MOVING):
        return SPEC_12
    return None
