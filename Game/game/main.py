"""Fixed 16 ms steps, then one draw. The rules stay free of pygame."""

from __future__ import annotations

import pygame

from game.commands import (
    Face,
    HoldYield,
    Move,
    Pause,
    ReleaseYield,
    Resume,
    StartMatch,
    Strike,
)
from game.model import Facing, Phase, VillainId, new_match
from game.rival import tyrant_commands
from game.tick import tick
from game.view import BAR_HEIGHT, WINDOW_SIZE, draw

STEP_MS = 16
# A stalled frame still draws. It does not replay the whole minute.
MAX_FRAME_MS = 250

_NORTH = (pygame.K_w, pygame.K_UP)
_SOUTH = (pygame.K_s, pygame.K_DOWN)
_WEST = (pygame.K_a, pygame.K_LEFT)
_EAST = (pygame.K_d, pygame.K_RIGHT)
_STRIKE = (pygame.K_j, pygame.K_SPACE)
_YIELD = pygame.K_k
_PAUSE = (pygame.K_ESCAPE,)
_START = (pygame.K_RETURN, pygame.K_KP_ENTER)
_WATCHED = _NORTH + _SOUTH + _WEST + _EAST + _STRIKE + _PAUSE + _START + (_YIELD,)


def _snapshot(keys) -> dict[int, bool]:
    return {code: bool(keys[code]) for code in _WATCHED}


def main() -> None:
    pygame.init()
    screen = pygame.display.set_mode(WINDOW_SIZE)
    pygame.display.set_caption("No Heroes Left")
    clock = pygame.time.Clock()
    match = new_match()
    seed = 1
    previous = _snapshot(pygame.key.get_pressed())
    accumulator = 0
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        frame_ms = clock.tick(60)
        if frame_ms > MAX_FRAME_MS:
            frame_ms = MAX_FRAME_MS
        accumulator += frame_ms
        keys = pygame.key.get_pressed()
        first_step = True
        while accumulator >= STEP_MS and running:
            commands = _commands(match, keys, previous, seed, first_step)
            commands.extend(tyrant_commands(match))
            if any(isinstance(command, StartMatch) for command in commands):
                seed += 1
            tick(match, commands, STEP_MS)
            accumulator -= STEP_MS
            first_step = False
        previous = _snapshot(keys)
        draw(screen, match)
        pygame.display.flip()
    pygame.quit()


def _commands(match, keys, previous, seed: int, first_step: bool) -> list:
    commands = []
    if first_step and _newly_down(keys, previous, _START) and match.phase in (Phase.BOOT, Phase.RESOLVED):
        commands.append(StartMatch(seed))
    if first_step and _newly_down(keys, previous, _PAUSE):
        if match.paused:
            commands.append(Resume())
        elif match.phase in (Phase.COUNTDOWN, Phase.LIVE):
            commands.append(Pause())

    if match.phase is not Phase.LIVE or match.paused:
        return commands

    facing = _held_facing(keys)
    if facing is not None:
        commands.append(Move(VillainId.A, facing))
        commands.append(Face(VillainId.A, facing))
    if first_step and _newly_down(keys, previous, _STRIKE):
        commands.append(Strike(VillainId.A))
    if keys[_YIELD]:
        commands.append(HoldYield(VillainId.A))
    elif first_step and previous[_YIELD]:
        usurper = match.villains.get(VillainId.A)
        if usurper is not None and usurper.yield_started_ms is not None:
            commands.append(ReleaseYield(VillainId.A))
    return commands


def _held_facing(keys) -> Facing | None:
    if _held(keys, _NORTH) and not _held(keys, _SOUTH):
        return Facing.N
    if _held(keys, _SOUTH) and not _held(keys, _NORTH):
        return Facing.S
    if _held(keys, _WEST) and not _held(keys, _EAST):
        return Facing.W
    if _held(keys, _EAST) and not _held(keys, _WEST):
        return Facing.E
    return None


def _held(keys, keycodes: tuple[int, ...]) -> bool:
    return any(keys[key] for key in keycodes)


def _newly_down(keys, previous, keycodes: tuple[int, ...]) -> bool:
    return _held(keys, keycodes) and not _held(previous, keycodes)


if __name__ == "__main__":
    main()
