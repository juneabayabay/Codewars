"""Tyrant brain, version 1. No window."""

from game.commands import Face, Move, StartMatch, Strike
from game.model import BodyState, Facing, Phase, VillainId, new_match
from game.rival import tyrant_commands
from game.tick import tick


def _live():
    match = new_match()
    tick(match, [StartMatch(1)], 0)
    tick(match, [], 3000)
    assert match.phase is Phase.LIVE
    return match


def test_rival_strikes_when_the_usurper_is_in_reach():
    match = _live()
    usurper = match.villains[VillainId.A]
    tyrant = match.villains[VillainId.B]
    usurper.x, usurper.y = 400, 270
    usurper.state = BodyState.STRIKING
    tyrant.x, tyrant.y = 430, 270
    tyrant.hp = 20
    tyrant.state = BodyState.IDLE

    commands = tyrant_commands(match)

    assert commands == [Strike(VillainId.B)]
    assert not any(isinstance(command, (Move, Face)) for command in commands)


def test_rival_retreats_along_the_nearest_wall_when_nearly_broken():
    match = _live()
    usurper = match.villains[VillainId.A]
    tyrant = match.villains[VillainId.B]
    usurper.x, usurper.y = 800, 100
    usurper.state = BodyState.STRIKING
    tyrant.x, tyrant.y = 40, 400
    tyrant.hp = 29

    commands = tyrant_commands(match)

    assert commands == [Face(VillainId.B, Facing.W), Move(VillainId.B, Facing.W)]
    assert not any(isinstance(command, Strike) for command in commands)

    tyrant.x = 0
    tyrant.y = 200
    usurper.y = 400
    assert tyrant_commands(match) == [Face(VillainId.B, Facing.N), Move(VillainId.B, Facing.N)]


def test_rival_moves_toward_the_usurper():
    match = _live()
    usurper = match.villains[VillainId.A]
    tyrant = match.villains[VillainId.B]
    usurper.x, usurper.y = 200, 270
    tyrant.x, tyrant.y = 700, 270
    tyrant.hp = 130

    commands = tyrant_commands(match)

    assert commands == [Face(VillainId.B, Facing.W), Move(VillainId.B, Facing.W)]
    before = tyrant.x
    tick(match, commands, 1000)
    assert tyrant.x < before


def test_rival_is_quiet_when_the_match_is_not_live():
    match = _live()
    match.paused = True
    assert tyrant_commands(match) == []
    match.paused = False
    match.phase = Phase.RESOLVED
    assert tyrant_commands(match) == []
