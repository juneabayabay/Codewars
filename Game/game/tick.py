"""One simulation step: handlers in order, then the events they emitted."""

from __future__ import annotations

from typing import Sequence

from game.bus import EventBus
from game.commands import Command
from game.events import Event
from game.handlers import HANDLERS
from game.model import Match


def tick(
    match: Match,
    commands: list[Command],
    dt_ms: int,
    *,
    seed_events: Sequence[Event] = (),
) -> list[Event]:
    bus = EventBus(match)
    for event in seed_events:
        bus.emit(event)
    for handler in HANDLERS:
        handler(match, commands, bus, dt_ms)
        commands = []
    return bus.drain()
