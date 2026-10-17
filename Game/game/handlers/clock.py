"""Countdown, then the live clock. Paused matches do not advance."""

from __future__ import annotations

from game.bus import EventBus
from game.commands import Command
from game.events import ClockTicked, CountdownTicked, MatchWentLive, TimeExpired
from game.model import Match, Phase, VillainId


def handle_clock(match: Match, commands: list[Command], bus: EventBus, dt_ms: int) -> None:
    del commands
    if match.paused:
        return
    if match.phase is Phase.COUNTDOWN:
        _countdown(match, bus, dt_ms)
        return
    if match.phase is Phase.LIVE:
        _live(match, bus, dt_ms)


def _countdown(match: Match, bus: EventBus, dt_ms: int) -> None:
    start = match.countdown_ms
    if start <= 0:
        if match.phase is Phase.COUNTDOWN:
            bus.emit(MatchWentLive())
        return
    end = start - dt_ms
    if end < 0:
        end = 0
    _emit_second_marks(match, bus, start, end)
    match.countdown_ms = end
    if end == 0 and match.phase is Phase.COUNTDOWN:
        bus.emit(MatchWentLive())


def _seconds_band(ms: int) -> int | None:
    if ms > 2000:
        return 3
    if ms > 1000:
        return 2
    if ms > 0:
        return 1
    return None


def _emit_second_marks(match: Match, bus: EventBus, start_ms: int, end_ms: int) -> None:
    start_mark = _seconds_band(start_ms)
    if start_mark is None:
        return
    end_mark = _seconds_band(end_ms)
    low = end_mark if end_mark is not None else 1
    last = match.last_countdown_mark
    for mark in range(start_mark, low - 1, -1):
        if last is not None and mark >= last:
            continue
        bus.emit(CountdownTicked(mark))
        match.last_countdown_mark = mark


def _live(match: Match, bus: EventBus, dt_ms: int) -> None:
    nxt = match.clock_ms - dt_ms
    if nxt < 0:
        nxt = 0
    bus.emit(ClockTicked(nxt))
    if nxt == 0:
        bus.emit(
            TimeExpired(
                menace_a=match.villains[VillainId.A].menace,
                menace_b=match.villains[VillainId.B].menace,
            )
        )
