"""Match and villain state. Events are applied here; commands are not."""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Any


class Phase(Enum):
    BOOT = "BOOT"
    COUNTDOWN = "COUNTDOWN"
    LIVE = "LIVE"
    RESOLVED = "RESOLVED"


class Result(Enum):
    A_WINS = "A_WINS"
    B_WINS = "B_WINS"
    DRAW = "DRAW"


class ResultReason(Enum):
    BREAK = "BREAK"
    YIELD = "YIELD"
    TIME = "TIME"


class VillainId(Enum):
    A = "A"
    B = "B"


class Facing(Enum):
    N = "N"
    E = "E"
    S = "S"
    W = "W"


class BodyState(Enum):
    IDLE = "IDLE"
    MOVING = "MOVING"
    STRIKING = "STRIKING"
    HURT = "HURT"
    BROKEN = "BROKEN"
    YIELDED = "YIELDED"


class Role(Enum):
    USURPER = "usurper"
    TYRANT = "tyrant"


ROOM_WIDTH = 960
ROOM_HEIGHT = 540
COUNTDOWN_MS = 3000
LIVE_CLOCK_MS = 60000
MENACE_MAX = 100

# Section 4 does not name feet. These sit inside the room so a villain can exist.
SPAWN_XY = {
    VillainId.A: (180, 270, Facing.E),
    VillainId.B: (780, 270, Facing.W),
}

_PHASE_RANK = {
    Phase.BOOT: 0,
    Phase.COUNTDOWN: 1,
    Phase.LIVE: 2,
    Phase.RESOLVED: 3,
}


class InvariantError(Exception):
    """Raised when an applied event would leave the match illegal."""


@dataclass(frozen=True)
class Loadout:
    id: VillainId
    name: str
    role: Role
    max_hp: int
    hp: int
    speed: int
    strike_reach: int
    strike_damage: int
    strike_recovery_ms: int
    menace: int
    menace_gain: int


def usurper_loadout() -> Loadout:
    return Loadout(
        id=VillainId.A,
        name="The Usurper",
        role=Role.USURPER,
        max_hp=100,
        hp=100,
        speed=180,
        strike_reach=36,
        strike_damage=12,
        strike_recovery_ms=280,
        menace=0,
        menace_gain=8,
    )


def tyrant_loadout() -> Loadout:
    return Loadout(
        id=VillainId.B,
        name="The Tyrant",
        role=Role.TYRANT,
        max_hp=130,
        hp=130,
        speed=120,
        strike_reach=52,
        strike_damage=16,
        strike_recovery_ms=420,
        menace=10,
        menace_gain=5,
    )


def opening_loadouts() -> tuple[Loadout, Loadout]:
    return (usurper_loadout(), tyrant_loadout())


@dataclass
class Villain:
    id: VillainId
    name: str
    role: Role
    hp: int
    max_hp: int
    menace: int
    x: float
    y: float
    facing: Facing
    state: BodyState
    strike_started_ms: int | None
    yield_started_ms: int | None
    speed: int
    strike_reach: int
    strike_damage: int
    strike_recovery_ms: int
    menace_gain: int


@dataclass
class Match:
    phase: Phase = Phase.BOOT
    paused: bool = False
    clock_ms: int = 0
    countdown_ms: int = 0
    result: Result | None = None
    result_reason: ResultReason | None = None
    villains: dict[VillainId, Villain] = field(default_factory=dict)
    rng_seed: int = 0
    resolved_latch: bool = False
    room_width: int = ROOM_WIDTH
    room_height: int = ROOM_HEIGHT
    last_countdown_mark: int | None = None
    log: list[Any] = field(default_factory=list)
    rejections: list[Any] = field(default_factory=list)


def new_match() -> Match:
    return Match()


def other_id(villain_id: VillainId) -> VillainId:
    if villain_id is VillainId.A:
        return VillainId.B
    return VillainId.A


def result_for(villain_id: VillainId) -> Result:
    if villain_id is VillainId.A:
        return Result.A_WINS
    return Result.B_WINS


def _clamp(value: int, low: int, high: int) -> int:
    if value < low:
        return low
    if value > high:
        return high
    return value


def _set_phase(match: Match, new_phase: Phase) -> None:
    current = match.phase
    if current is new_phase:
        return
    restart = current is Phase.RESOLVED and new_phase is Phase.COUNTDOWN
    forward = _PHASE_RANK[new_phase] == _PHASE_RANK[current] + 1
    if not restart and not forward:
        raise InvariantError(
            f"INV-3 phase cannot move {current.value} → {new_phase.value}"
        )
    match.phase = new_phase


def _spawn(loadout: Loadout) -> Villain:
    x, y, facing = SPAWN_XY[loadout.id]
    return Villain(
        id=loadout.id,
        name=loadout.name,
        role=loadout.role,
        hp=loadout.hp,
        max_hp=loadout.max_hp,
        menace=loadout.menace,
        x=x,
        y=y,
        facing=facing,
        state=BodyState.IDLE,
        strike_started_ms=None,
        yield_started_ms=None,
        speed=loadout.speed,
        strike_reach=loadout.strike_reach,
        strike_damage=loadout.strike_damage,
        strike_recovery_ms=loadout.strike_recovery_ms,
        menace_gain=loadout.menace_gain,
    )


def _check(match: Match) -> None:
    if match.phase is not Phase.BOOT and len(match.villains) != 2:
        raise InvariantError("INV-1 a match contains exactly two villains")
    ids = set(match.villains)
    if match.villains and ids != {VillainId.A, VillainId.B}:
        raise InvariantError("INV-1 villains must be A and B")
    for villain in match.villains.values():
        if not 0 <= villain.hp <= villain.max_hp:
            raise InvariantError("INV-2 hp out of range")
        if not 0 <= villain.menace <= MENACE_MAX:
            raise InvariantError("INV-2 menace out of range")
    if match.phase is Phase.RESOLVED:
        if match.result is None or match.result_reason is None or not match.resolved_latch:
            raise InvariantError("INV-4 resolved match is missing its latch")
    elif match.resolved_latch or match.result is not None or match.result_reason is not None:
        raise InvariantError("INV-4 result is set before the match resolves")


def apply(match: Match, event: Any) -> None:
    """Write state from one event. Commands never call this."""
    from game.events import (
        ClockTicked,
        MatchPaused,
        MatchResolved,
        MatchResumed,
        MatchStarted,
        MatchWentLive,
        MenaceChanged,
        StrikeRecovered,
        StrikeStarted,
        VillainBroken,
        VillainFaced,
        VillainHurt,
        VillainMoved,
        VillainYielded,
        YieldCancelled,
        YieldStarted,
    )

    if isinstance(event, MatchStarted):
        if match.phase not in (Phase.BOOT, Phase.RESOLVED):
            raise InvariantError("INV-3 StartMatch is only legal from BOOT or RESOLVED")
        ids = {item.id for item in event.loadouts}
        if ids != {VillainId.A, VillainId.B} or len(event.loadouts) != 2:
            raise InvariantError("INV-1 MatchStarted must spawn A and B")
        match.log.clear()
        match.rejections.clear()
        match.paused = False
        match.clock_ms = 0
        match.countdown_ms = COUNTDOWN_MS
        match.result = None
        match.result_reason = None
        match.resolved_latch = False
        match.last_countdown_mark = None
        match.rng_seed = event.seed
        match.room_width = event.room_width
        match.room_height = event.room_height
        match.villains = {item.id: _spawn(item) for item in event.loadouts}
        _set_phase(match, Phase.COUNTDOWN)
    elif isinstance(event, MatchWentLive):
        if match.phase is Phase.LIVE:
            return
        _set_phase(match, Phase.LIVE)
        match.clock_ms = LIVE_CLOCK_MS
        match.countdown_ms = 0
    elif isinstance(event, ClockTicked):
        match.clock_ms = event.clock_ms
    elif isinstance(event, StrikeStarted):
        villain = match.villains[event.villain_id]
        villain.state = BodyState.STRIKING
        villain.facing = event.facing
        villain.strike_started_ms = 0
    elif isinstance(event, StrikeRecovered):
        villain = match.villains[event.villain_id]
        villain.state = BodyState.IDLE
        villain.strike_started_ms = None
    elif isinstance(event, VillainMoved):
        villain = match.villains[event.villain_id]
        villain.x, villain.y = event.to_xy
        villain.state = BodyState.MOVING
    elif isinstance(event, VillainFaced):
        villain = match.villains[event.villain_id]
        villain.facing = event.facing
    elif isinstance(event, VillainHurt):
        villain = match.villains[event.villain_id]
        villain.hp = _clamp(event.hp_after, 0, villain.max_hp)
    elif isinstance(event, MenaceChanged):
        villain = match.villains[event.villain_id]
        villain.menace = _clamp(event.after, 0, MENACE_MAX)
    elif isinstance(event, VillainBroken):
        villain = match.villains[event.villain_id]
        villain.hp = 0
        villain.state = BodyState.BROKEN
    elif isinstance(event, YieldStarted):
        villain = match.villains[event.villain_id]
        villain.yield_started_ms = 0
    elif isinstance(event, YieldCancelled):
        villain = match.villains[event.villain_id]
        villain.yield_started_ms = None
    elif isinstance(event, VillainYielded):
        villain = match.villains[event.villain_id]
        villain.state = BodyState.YIELDED
        villain.yield_started_ms = None
    elif isinstance(event, MatchPaused):
        match.paused = True
    elif isinstance(event, MatchResumed):
        match.paused = False
    elif isinstance(event, MatchResolved):
        if match.resolved_latch:
            return
        _set_phase(match, Phase.RESOLVED)
        match.result = event.result
        match.result_reason = event.reason
        match.resolved_latch = True
    _check(match)
