"""pygame drawing. This module reads a match and emits nothing."""

from __future__ import annotations

from pathlib import Path

import pygame

from game.events import ClockTicked, StrikeLanded
from game.model import (
    MENACE_MAX,
    ROOM_HEIGHT,
    ROOM_WIDTH,
    BodyState,
    Facing,
    Match,
    Phase,
    Result,
    ResultReason,
    Villain,
    VillainId,
)

BAR_HEIGHT = 52
WINDOW_SIZE = (ROOM_WIDTH, ROOM_HEIGHT + BAR_HEIGHT)

_RESULT_LINES = {
    (Result.A_WINS, ResultReason.BREAK): "The Tyrant breaks. The Usurper takes the chair.",
    (Result.A_WINS, ResultReason.YIELD): "The Tyrant yields. The city hears it.",
    (Result.A_WINS, ResultReason.TIME): "The bell. Fear keeps the crown on the Usurper.",
    (Result.B_WINS, ResultReason.BREAK): "The Usurper breaks. The old fear sits the throne.",
    (Result.B_WINS, ResultReason.YIELD): "The Usurper yields. The knife was never enough.",
    (Result.B_WINS, ResultReason.TIME): "The bell. The Tyrant's fear was older, and it holds.",
    (Result.DRAW, ResultReason.TIME): "The bell. Neither claim holds. The city burns anyway.",
}

_ROOM = (36, 32, 30)
_BAR = (18, 16, 16)
_INK = (232, 226, 214)
_TRACK = (48, 44, 42)
_HEALTH = (176, 64, 58)
_MENACE = (196, 154, 64)
_FLASH = (255, 244, 220)
_CONDEMN = (255, 236, 186)
_NORMAL_FLASH_TICKS = 6
_CONDEMN_FLASH_TICKS = 14
_BACKGROUND_PATH = Path(__file__).resolve().parent.parent / "background.jpg"
_HERO_PATH = Path(__file__).resolve().parent.parent / "evil1.png"
_ENEMY_PATH = Path(__file__).resolve().parent.parent / "Evil2.png"
_SPRITE_HEIGHT = {
    VillainId.A: 150,
    VillainId.B: 156,
}
_background: pygame.Surface | None = None
_sprites: dict[VillainId, pygame.Surface] | None = None

def draw(screen: pygame.Surface, match: Match) -> None:
    screen.fill(_BAR)
    _draw_room(screen)
    for villain_id in (VillainId.A, VillainId.B):
        villain = match.villains.get(villain_id)
        if villain is not None:
            _draw_villain(screen, match, villain)
    _draw_bar(screen, match)
    if match.phase is Phase.RESOLVED:
        _draw_result(screen, match)


def _draw_room(screen: pygame.Surface) -> None:
    screen.blit(_room_background(), (0, BAR_HEIGHT))


def _room_background() -> pygame.Surface:
    global _background
    if _background is None:
        image = pygame.image.load(_BACKGROUND_PATH).convert()
        _background = pygame.transform.smoothscale(image, (ROOM_WIDTH, ROOM_HEIGHT))
    return _background


def _draw_villain(screen: pygame.Surface, match: Match, villain: Villain) -> None:
    flash = _flash(match, villain.id)
    if flash is not None and flash[0]:
        _draw_halo(screen, villain, flash[1])
    sprite = _villain_sprite(villain, flash)
    feet_x = round(villain.x)
    feet_y = round(BAR_HEIGHT + villain.y)
    screen.blit(sprite, (feet_x - sprite.get_width() // 2, feet_y - sprite.get_height()))


def _villain_sprite(villain: Villain, flash: tuple[bool, float] | None) -> pygame.Surface:
    sprite = _character_sprites()[villain.id]
    if villain.facing is Facing.W:
        sprite = pygame.transform.flip(sprite, True, False)
    if villain.state in (BodyState.BROKEN, BodyState.YIELDED):
        darkened = sprite.copy()
        darkened.fill((110, 110, 110, 255), special_flags=pygame.BLEND_RGBA_MULT)
        sprite = darkened
    if flash is None:
        return sprite
    _condemn, strength = flash
    lit = sprite.copy()
    glow = pygame.Surface(sprite.get_size(), pygame.SRCALPHA)
    glow.fill((*_FLASH, round(180 * strength)))
    lit.blit(glow, (0, 0), special_flags=pygame.BLEND_RGBA_ADD)
    return lit


def _character_sprites() -> dict[VillainId, pygame.Surface]:
    global _sprites
    if _sprites is None:
        hero = _punch_black(pygame.image.load(_HERO_PATH).convert_alpha())
        enemy_sheet = _punch_black(pygame.image.load(_ENEMY_PATH).convert_alpha())
        enemy = enemy_sheet.subsurface((0, 0, 134, enemy_sheet.get_height()))
        _sprites = {
            VillainId.A: _fit(_crop_opaque(hero), _SPRITE_HEIGHT[VillainId.A]),
            VillainId.B: _fit(_crop_opaque(enemy), _SPRITE_HEIGHT[VillainId.B]),
        }
    return _sprites


def _punch_black(sheet: pygame.Surface) -> pygame.Surface:
    punched = sheet.copy()
    for x in range(punched.get_width()):
        for y in range(punched.get_height()):
            red, green, blue, _alpha = punched.get_at((x, y))
            if max(red, green, blue) < 12:
                punched.set_at((x, y), (0, 0, 0, 0))
    return punched


def _crop_opaque(sheet: pygame.Surface) -> pygame.Surface:
    bounds = sheet.get_bounding_rect()
    if bounds.width == 0 or bounds.height == 0:
        return sheet
    return sheet.subsurface(bounds).copy()


def _fit(sheet: pygame.Surface, height: int) -> pygame.Surface:
    width = max(1, round(sheet.get_width() * height / sheet.get_height()))
    return pygame.transform.smoothscale(sheet, (width, height))


def _draw_halo(screen: pygame.Surface, villain: Villain, strength: float) -> None:
    color = _mix(_ROOM, _CONDEMN, 0.35 + 0.5 * strength)
    x = round(villain.x)
    y = round(BAR_HEIGHT + villain.y)
    pygame.draw.circle(screen, color, (x, y - 36), round(26 + 10 * strength))


def _flash(match: Match, villain_id: VillainId) -> tuple[bool, float] | None:
    condemn = False
    clocks = 0
    seen = False
    for event in match.log:
        if isinstance(event, StrikeLanded) and event.target_id == villain_id:
            seen = True
            condemn = event.condemn
            clocks = 0
        elif seen and isinstance(event, ClockTicked):
            clocks += 1
    if not seen:
        return None
    limit = _CONDEMN_FLASH_TICKS if condemn else _NORMAL_FLASH_TICKS
    if clocks > limit:
        return None
    strength = 1 - clocks / limit
    return condemn, strength


def _mix(base: tuple[int, int, int], target: tuple[int, int, int], amount: float) -> tuple[int, int, int]:
    return tuple(round(base[index] + (target[index] - base[index]) * amount) for index in range(3))


def _draw_bar(screen: pygame.Surface, match: Match) -> None:
    font = pygame.font.Font(None, 22)
    if VillainId.A in match.villains:
        _draw_fighter(screen, font, match.villains[VillainId.A], 16, align_right=False)
    if VillainId.B in match.villains:
        _draw_fighter(screen, font, match.villains[VillainId.B], ROOM_WIDTH - 16 - 280, align_right=True)
    clock = font.render(_clock_text(match), True, _INK)
    screen.blit(clock, clock.get_rect(center=(ROOM_WIDTH // 2, BAR_HEIGHT // 2)))


def _draw_fighter(screen: pygame.Surface, font: pygame.font.Font, villain: Villain, x: int, align_right: bool) -> None:
    name = font.render(villain.name, True, _INK)
    name_x = x + 280 - name.get_width() if align_right else x
    screen.blit(name, (name_x, 4))
    _meter(screen, x, 24, 280, 10, villain.hp / villain.max_hp, _HEALTH)
    _meter(screen, x, 38, 280, 6, villain.menace / MENACE_MAX, _MENACE)


def _meter(
    screen: pygame.Surface,
    x: int,
    y: int,
    width: int,
    height: int,
    fraction: float,
    color: tuple[int, int, int],
) -> None:
    pygame.draw.rect(screen, _TRACK, (x, y, width, height))
    fill = round(width * fraction)
    if fill < 0:
        fill = 0
    if fill > width:
        fill = width
    if fill:
        pygame.draw.rect(screen, color, (x, y, fill, height))


def _clock_text(match: Match) -> str:
    if match.phase is Phase.BOOT:
        return "Enter"
    if match.phase is Phase.COUNTDOWN:
        return str(_seconds_left(match.countdown_ms))
    if match.phase is Phase.LIVE:
        label = str(_seconds_left(match.clock_ms))
        if match.paused:
            return f"{label}  Paused"
        return label
    if match.phase is Phase.RESOLVED:
        return "Enter"
    return ""


def _seconds_left(ms: int) -> int:
    if ms <= 0:
        return 0
    return (ms + 999) // 1000


def _draw_result(screen: pygame.Surface, match: Match) -> None:
    if match.result is None or match.result_reason is None:
        return
    line = _RESULT_LINES.get((match.result, match.result_reason))
    if line is None:
        return
    font = pygame.font.Font(None, 32)
    text = font.render(line, True, _INK)
    rect = text.get_rect(center=(ROOM_WIDTH // 2, BAR_HEIGHT + ROOM_HEIGHT // 2))
    backing = rect.inflate(24, 16)
    pygame.draw.rect(screen, _BAR, backing)
    screen.blit(text, rect)
