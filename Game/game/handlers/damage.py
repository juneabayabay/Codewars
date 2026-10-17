"""Apply a hit that has already landed. Strike timing is a later slice."""

from __future__ import annotations

from game.bus import EventBus
from game.commands import Command
from game.events import MenaceChanged, StrikeLanded, VillainHurt
from game.model import MENACE_MAX, Match


def handle_damage(match: Match, commands: list[Command], bus: EventBus, dt_ms: int) -> None:
    del commands, dt_ms
    for event in bus.each(StrikeLanded):
        target = match.villains[event.target_id]
        attacker = match.villains[event.attacker_id]
        hp_before = target.hp
        hp_after = hp_before - event.damage
        if hp_after < 0:
            hp_after = 0
        if hp_after > target.max_hp:
            hp_after = target.max_hp
        menace_before = attacker.menace
        if event.condemn:
            menace_after = 0
        else:
            menace_after = menace_before + attacker.menace_gain
            if menace_after > MENACE_MAX:
                menace_after = MENACE_MAX
        bus.emit(VillainHurt(target.id, hp_before, hp_after))
        bus.emit(MenaceChanged(attacker.id, menace_before, menace_after))
