"""The first legal end wins: break, then yield, then time."""

from __future__ import annotations

from game.bus import EventBus
from game.commands import Command
from game.events import MatchResolved, TimeExpired, VillainBroken, VillainYielded
from game.model import Match, Phase, Result, ResultReason, other_id, result_for


def handle_resolve(match: Match, commands: list[Command], bus: EventBus, dt_ms: int) -> None:
    del commands, dt_ms
    if match.resolved_latch or match.phase is not Phase.LIVE:
        return

    broken = bus.each(VillainBroken)
    if broken:
        winner = other_id(broken[0].villain_id)
        bus.emit(MatchResolved(result_for(winner), ResultReason.BREAK))
        return

    yielded = bus.each(VillainYielded)
    if yielded:
        winner = other_id(yielded[0].villain_id)
        bus.emit(MatchResolved(result_for(winner), ResultReason.YIELD))
        return

    expired = bus.each(TimeExpired)
    if not expired:
        return
    bus.emit(MatchResolved(_time_result(expired[0]), ResultReason.TIME))


def _time_result(event: TimeExpired) -> Result:
    if event.menace_a > event.menace_b:
        return Result.A_WINS
    if event.menace_b > event.menace_a:
        return Result.B_WINS
    return Result.DRAW
