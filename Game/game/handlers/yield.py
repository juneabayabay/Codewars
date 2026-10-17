"""Finish a surrender hold, or cancel it when that villain is hurt."""

from __future__ import annotations

from game.bus import EventBus
from game.commands import Command
from game.events import VillainHurt, VillainYielded, YieldCancelled
from game.model import BodyState, Match, Phase, VillainId

HOLD_MS = 600


def handle_yield(match: Match, commands: list[Command], bus: EventBus, dt_ms: int) -> None:
    del commands
    if match.paused or match.phase is not Phase.LIVE:
        return
    for villain in list(match.villains.values()):
        if villain.yield_started_ms is None or villain.state is BodyState.YIELDED:
            continue
        if _hurt_this_tick(bus, villain.id):
            bus.emit(YieldCancelled(villain.id, "HURT"))
            continue
        elapsed = villain.yield_started_ms + dt_ms
        villain.yield_started_ms = elapsed
        if elapsed >= HOLD_MS:
            bus.emit(VillainYielded(villain.id))


def _hurt_this_tick(bus: EventBus, villain_id: VillainId) -> bool:
    return any(event.villain_id == villain_id for event in bus.each(VillainHurt))
