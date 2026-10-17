"""Tyrant commands, version 1. No pathfinding."""

from __future__ import annotations

from math import hypot

from game.commands import Command, Face, Move, Strike
from game.model import BodyState, Facing, Match, Phase, Villain, VillainId


def tyrant_commands(match: Match) -> list[Command]:
    if match.phase is not Phase.LIVE or match.paused:
        return []
    usurper = match.villains.get(VillainId.A)
    tyrant = match.villains.get(VillainId.B)
    if usurper is None or tyrant is None:
        return []
    if _in_reach(usurper, tyrant) and tyrant.state in (BodyState.IDLE, BodyState.MOVING):
        return [Strike(VillainId.B)]
    if tyrant.hp < 30 and usurper.state is BodyState.STRIKING:
        facing = _retreat_facing(match, usurper, tyrant)
        return [Face(VillainId.B, facing), Move(VillainId.B, facing)]
    facing = _toward(usurper, tyrant)
    return [Face(VillainId.B, facing), Move(VillainId.B, facing)]


def _in_reach(usurper: Villain, tyrant: Villain) -> bool:
    return _distance(usurper, tyrant) <= tyrant.strike_reach


def _distance(usurper: Villain, tyrant: Villain) -> float:
    return hypot(usurper.x - tyrant.x, usurper.y - tyrant.y)


def _toward(usurper: Villain, tyrant: Villain) -> Facing:
    dx = usurper.x - tyrant.x
    dy = usurper.y - tyrant.y
    if abs(dx) >= abs(dy):
        if dx >= 0:
            return Facing.E
        return Facing.W
    if dy >= 0:
        return Facing.S
    return Facing.N


def _retreat_facing(match: Match, usurper: Villain, tyrant: Villain) -> Facing:
    walls = (
        (tyrant.x, Facing.W),
        (match.room_width - tyrant.x, Facing.E),
        (tyrant.y, Facing.N),
        (match.room_height - tyrant.y, Facing.S),
    )
    distance, wall = min(walls, key=lambda item: item[0])
    if distance > 0:
        return wall
    if wall in (Facing.W, Facing.E):
        if usurper.y > tyrant.y:
            return Facing.N
        if usurper.y < tyrant.y:
            return Facing.S
        return Facing.N
    if usurper.x > tyrant.x:
        return Facing.W
    if usurper.x < tyrant.x:
        return Facing.E
    return Facing.W
