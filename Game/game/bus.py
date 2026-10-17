"""Queue of events emitted during a single tick."""

from __future__ import annotations

from typing import Any

from game.model import Match, apply


class EventBus:
    def __init__(self, match: Match) -> None:
        self.match = match
        self.events: list[Any] = []

    def emit(self, event: Any) -> None:
        apply(self.match, event)
        self.match.log.append(event)
        self.events.append(event)

    def each(self, kind: type) -> list[Any]:
        return [event for event in self.events if isinstance(event, kind)]

    def drain(self) -> list[Any]:
        return list(self.events)
