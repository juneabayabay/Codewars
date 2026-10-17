"""A hurt that lands on 0 breaks that villain."""

from __future__ import annotations

from game.bus import EventBus
from game.commands import Command
from game.events import VillainBroken, VillainHurt
from game.model import BodyState, Match


def handle_break(match: Match, commands: list[Command], bus: EventBus, dt_ms: int) -> None:
    del commands, dt_ms
    for event in bus.each(VillainHurt):
        if event.hp_after != 0:
            continue
        villain = match.villains[event.villain_id]
        if villain.state is BodyState.BROKEN:
            continue
        bus.emit(VillainBroken(event.villain_id))
