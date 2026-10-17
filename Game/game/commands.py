"""Intents for one tick. These records do not carry hp, menace, phase, or result."""

from __future__ import annotations

from dataclasses import dataclass

from game.model import Facing, VillainId


@dataclass(frozen=True)
class StartMatch:
    seed: int


@dataclass(frozen=True)
class Move:
    villain_id: VillainId
    facing: Facing


@dataclass(frozen=True)
class Face:
    villain_id: VillainId
    facing: Facing


@dataclass(frozen=True)
class Strike:
    villain_id: VillainId


@dataclass(frozen=True)
class HoldYield:
    villain_id: VillainId


@dataclass(frozen=True)
class ReleaseYield:
    villain_id: VillainId


@dataclass(frozen=True)
class Pause:
    pass


@dataclass(frozen=True)
class Resume:
    pass


@dataclass(frozen=True)
class CommandRejected:
    """Logged beside the match. Not a match event."""

    command: Command
    spec_id: str


Command = (
    StartMatch
    | Move
    | Face
    | Strike
    | HoldYield
    | ReleaseYield
    | Pause
    | Resume
)
