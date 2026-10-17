"""Resolve a strike once at 120 ms, then recover."""

from __future__ import annotations

from math import hypot

from game.bus import EventBus
from game.commands import Command
from game.events import (
    StrikeLanded,
    StrikeRecovered,
    StrikeStarted,
    StrikeWhiffed,
)
from game.model import BodyState, Facing, Match, Phase, Villain, VillainId, other_id

ACTIVE_MS = 120
_DIRECTION = {
    Facing.N: (0.0, -1.0),
    Facing.E: (1.0, 0.0),
    Facing.S: (0.0, 1.0),
    Facing.W: (-1.0, 0.0),
}


def handle_strike(match: Match, commands: list[Command], bus: EventBus, dt_ms: int) -> None:
    del commands
    if match.paused or match.phase is not Phase.LIVE:
        return
    for villain in list(match.villains.values()):
        if villain.state is not BodyState.STRIKING:
            continue
        elapsed = (villain.strike_started_ms or 0) + dt_ms
        villain.strike_started_ms = elapsed
        started = _latest_start(match, villain.id)
        if started is None:
            continue
        if elapsed >= ACTIVE_MS and not _active_frame_resolved(match, villain.id):
            _resolve_active_frame(match, villain, started, bus)
        if elapsed >= villain.strike_recovery_ms and villain.state is BodyState.STRIKING:
            bus.emit(StrikeRecovered(villain.id))


def _resolve_active_frame(match: Match, attacker: Villain, started: StrikeStarted, bus: EventBus) -> None:
    target = match.villains[other_id(attacker.id)]
    if _in_cone(attacker, target, started.facing):
        damage = attacker.strike_damage * (2 if started.condemn else 1)
        bus.emit(
            StrikeLanded(
                attacker_id=attacker.id,
                target_id=target.id,
                damage=damage,
                condemn=started.condemn,
            )
        )
        return
    bus.emit(StrikeWhiffed(attacker.id))


def _in_cone(attacker: Villain, target: Villain, facing: Facing) -> bool:
    dx = target.x - attacker.x
    dy = target.y - attacker.y
    forward_x, forward_y = _DIRECTION[facing]
    in_front = dx * forward_x + dy * forward_y >= 0
    return in_front and hypot(dx, dy) <= attacker.strike_reach


def _latest_start(match: Match, villain_id: VillainId) -> StrikeStarted | None:
    started = None
    for event in match.log:
        if isinstance(event, StrikeStarted) and event.villain_id == villain_id:
            started = event
    return started


def _active_frame_resolved(match: Match, villain_id: VillainId) -> bool:
    resolved = False
    for event in match.log:
        if isinstance(event, StrikeStarted) and event.villain_id == villain_id:
            resolved = False
        elif isinstance(event, StrikeWhiffed) and event.villain_id == villain_id:
            resolved = True
        elif isinstance(event, StrikeLanded) and event.attacker_id == villain_id:
            resolved = True
    return resolved
