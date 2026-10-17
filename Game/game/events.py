"""Facts that already happened. Applying one of these is what changes a match."""

from __future__ import annotations

from dataclasses import dataclass

from game.model import Facing, Loadout, Result, ResultReason, VillainId


@dataclass(frozen=True)
class MatchStarted:
    seed: int
    room_width: int
    room_height: int
    loadouts: tuple[Loadout, Loadout]


@dataclass(frozen=True)
class CountdownTicked:
    seconds_left: int


@dataclass(frozen=True)
class MatchWentLive:
    pass


@dataclass(frozen=True)
class VillainMoved:
    villain_id: VillainId
    from_xy: tuple[float, float]
    to_xy: tuple[float, float]


@dataclass(frozen=True)
class VillainFaced:
    villain_id: VillainId
    facing: Facing


@dataclass(frozen=True)
class StrikeStarted:
    villain_id: VillainId
    facing: Facing
    condemn: bool


@dataclass(frozen=True)
class StrikeWhiffed:
    villain_id: VillainId


@dataclass(frozen=True)
class StrikeLanded:
    attacker_id: VillainId
    target_id: VillainId
    damage: int
    condemn: bool


@dataclass(frozen=True)
class MenaceChanged:
    villain_id: VillainId
    before: int
    after: int


@dataclass(frozen=True)
class VillainHurt:
    villain_id: VillainId
    hp_before: int
    hp_after: int


@dataclass(frozen=True)
class VillainBroken:
    villain_id: VillainId


@dataclass(frozen=True)
class YieldStarted:
    villain_id: VillainId


@dataclass(frozen=True)
class YieldCancelled:
    villain_id: VillainId
    reason: str


@dataclass(frozen=True)
class VillainYielded:
    villain_id: VillainId


@dataclass(frozen=True)
class ClockTicked:
    clock_ms: int


@dataclass(frozen=True)
class TimeExpired:
    menace_a: int
    menace_b: int


@dataclass(frozen=True)
class MatchResolved:
    result: Result
    reason: ResultReason


@dataclass(frozen=True)
class StrikeRecovered:
    villain_id: VillainId


@dataclass(frozen=True)
class MatchPaused:
    pass


@dataclass(frozen=True)
class MatchResumed:
    pass


Event = (
    MatchStarted
    | CountdownTicked
    | MatchWentLive
    | VillainMoved
    | VillainFaced
    | StrikeStarted
    | StrikeWhiffed
    | StrikeLanded
    | MenaceChanged
    | VillainHurt
    | VillainBroken
    | YieldStarted
    | YieldCancelled
    | VillainYielded
    | ClockTicked
    | TimeExpired
    | MatchResolved
    | StrikeRecovered
    | MatchPaused
    | MatchResumed
)
