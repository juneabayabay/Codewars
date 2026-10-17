"""Acceptance tests for the rules core. No window."""

from game.commands import Face, HoldYield, Move, Pause, StartMatch, Strike
from game.events import (
    MatchPaused,
    MatchResolved,
    MatchStarted,
    MatchWentLive,
    MenaceChanged,
    StrikeLanded,
    StrikeRecovered,
    StrikeStarted,
    StrikeWhiffed,
    TimeExpired,
    VillainBroken,
    VillainFaced,
    VillainHurt,
    VillainMoved,
    VillainYielded,
    YieldCancelled,
    YieldStarted,
)
from game.spec_ids import SPEC_7, SPEC_18
from game.model import (
    LIVE_CLOCK_MS,
    BodyState,
    Facing,
    Phase,
    Result,
    ResultReason,
    VillainId,
    new_match,
)
from game.tick import tick


def _live_match(seed: int = 1):
    match = new_match()
    tick(match, [StartMatch(seed)], 0)
    tick(match, [], 3000)
    assert match.phase is Phase.LIVE
    assert match.clock_ms == LIVE_CLOCK_MS
    return match


def test_ac1_start_match_emits_match_started_and_sets_countdown():
    match = new_match()
    assert match.phase is Phase.BOOT
    events = tick(match, [StartMatch(seed=7)], 0)

    started = [event for event in events if isinstance(event, MatchStarted)]
    assert len(started) == 1
    assert started[0].seed == 7
    assert started[0].room_width == 960
    assert started[0].room_height == 540
    assert match.phase is Phase.COUNTDOWN
    assert match.countdown_ms == 3000
    assert match.result is None
    assert set(match.villains) == {VillainId.A, VillainId.B}

    usurper = match.villains[VillainId.A]
    tyrant = match.villains[VillainId.B]
    assert usurper.name == "The Usurper"
    assert usurper.hp == 100
    assert usurper.max_hp == 100
    assert usurper.menace == 0
    assert tyrant.name == "The Tyrant"
    assert tyrant.hp == 130
    assert tyrant.max_hp == 130
    assert tyrant.menace == 10


def test_ac2_countdown_emits_exactly_one_match_went_live():
    match = new_match()
    opening = tick(match, [StartMatch(seed=1)], 0)
    assert match.phase is Phase.COUNTDOWN
    assert not any(isinstance(event, MatchWentLive) for event in opening)

    finishing = tick(match, [], 3000)
    assert match.phase is Phase.LIVE
    assert match.clock_ms == LIVE_CLOCK_MS
    assert sum(isinstance(event, MatchWentLive) for event in finishing) == 1

    after = tick(match, [], 16) + tick(match, [], 16)
    went_live = [
        event
        for event in opening + finishing + after
        if isinstance(event, MatchWentLive)
    ]
    assert len(went_live) == 1


def test_ac3_move_into_a_wall_stays_inside_the_room():
    match = _live_match()
    usurper = match.villains[VillainId.A]
    usurper.x = 950
    usurper.y = 270
    usurper.facing = Facing.E

    events = tick(match, [Move(VillainId.A, Facing.E)], 1000)

    moved = [event for event in events if isinstance(event, VillainMoved)]
    assert len(moved) == 1
    to_x, to_y = moved[0].to_xy
    assert moved[0].from_xy == (950, 270)
    assert to_x == match.room_width
    assert to_y == 270
    assert 0 <= to_x <= match.room_width
    assert 0 <= to_y <= match.room_height
    assert not any(isinstance(event, VillainFaced) for event in events)
    assert usurper.x == match.room_width
    assert usurper.state is BodyState.MOVING

    later = tick(match, [], 16)
    assert not any(isinstance(event, VillainMoved) for event in later)
    assert usurper.state is BodyState.IDLE


def _place_duel(match, attacker_xy: tuple[float, float], target_xy: tuple[float, float]) -> None:
    attacker = match.villains[VillainId.A]
    target = match.villains[VillainId.B]
    attacker.x, attacker.y = attacker_xy
    attacker.facing = Facing.E
    target.x, target.y = target_xy
    target.facing = Facing.W


def test_ac4_strike_while_striking_is_rejected():
    match = _live_match()
    tick(match, [Strike(VillainId.A)], 16)

    events = tick(match, [Strike(VillainId.A)], 16)

    assert not any(isinstance(event, StrikeStarted) for event in events)
    assert sum(isinstance(event, StrikeStarted) for event in match.log) == 1
    rejected = [item for item in match.rejections if item.spec_id == SPEC_18]
    assert len(rejected) == 1
    assert isinstance(rejected[0].command, Strike)
    assert match.villains[VillainId.A].state is BodyState.STRIKING


def test_ac5_target_outside_the_cone_whiffs():
    match = _live_match()
    _place_duel(match, (400, 270), (380, 270))
    hp_before = match.villains[VillainId.B].hp
    menace_before = match.villains[VillainId.A].menace

    events = tick(match, [Strike(VillainId.A)], 120)

    whiffed = [event for event in events if isinstance(event, StrikeWhiffed)]
    assert len(whiffed) == 1
    assert not any(isinstance(event, StrikeLanded) for event in events)
    assert match.villains[VillainId.B].hp == hp_before
    assert match.villains[VillainId.A].menace == menace_before


def test_ac6_target_inside_the_cone_lands_role_damage():
    match = _live_match()
    _place_duel(match, (400, 270), (420, 270))

    events = tick(match, [Strike(VillainId.A)], 120)

    landed = [event for event in events if isinstance(event, StrikeLanded)]
    assert len(landed) == 1
    assert landed[0].damage == 12
    assert landed[0].condemn is False
    assert match.villains[VillainId.B].hp == 118
    assert not any(isinstance(event, StrikeWhiffed) for event in events)

    recovered = tick(match, [], 160)
    assert sum(isinstance(event, StrikeRecovered) for event in recovered) == 1
    assert match.villains[VillainId.A].state is BodyState.IDLE


def test_ac7_condemn_doubles_damage_and_clears_menace():
    match = _live_match()
    _place_duel(match, (400, 270), (420, 270))
    match.villains[VillainId.A].menace = 100

    events = tick(match, [Strike(VillainId.A)], 120)

    started = [event for event in events if isinstance(event, StrikeStarted)]
    landed = [event for event in events if isinstance(event, StrikeLanded)]
    menace = [event for event in events if isinstance(event, MenaceChanged)]
    assert len(started) == 1
    assert started[0].condemn is True
    assert len(landed) == 1
    assert landed[0].damage == 24
    assert landed[0].condemn is True
    assert match.villains[VillainId.B].hp == 106
    assert len(menace) == 1
    assert menace[0].before == 100
    assert menace[0].after == 0
    assert match.villains[VillainId.A].menace == 0


def test_ac16_two_steps_resolve_one_strike_once():
    match = _live_match()
    _place_duel(match, (400, 270), (420, 270))
    opening = tick(match, [Strike(VillainId.A)], 112)
    assert not any(isinstance(event, (StrikeLanded, StrikeWhiffed)) for event in opening)

    first = tick(match, [], 16)
    second = tick(match, [], 16)
    resolutions = [
        event
        for event in first + second
        if isinstance(event, (StrikeLanded, StrikeWhiffed))
    ]
    assert len(resolutions) == 1
    assert isinstance(resolutions[0], StrikeLanded)


def test_ac8_hit_past_zero_clamps_breaks_and_resolves():
    match = _live_match()
    match.villains[VillainId.B].hp = 10

    events = tick(
        match,
        [],
        0,
        seed_events=[
            StrikeLanded(
                attacker_id=VillainId.A,
                target_id=VillainId.B,
                damage=12,
                condemn=False,
            )
        ],
    )

    assert match.villains[VillainId.B].hp == 0
    hurts = [event for event in events if isinstance(event, VillainHurt)]
    assert len(hurts) == 1
    assert hurts[0].hp_before == 10
    assert hurts[0].hp_after == 0
    assert sum(isinstance(event, VillainBroken) for event in events) == 1
    resolved = [event for event in events if isinstance(event, MatchResolved)]
    assert len(resolved) == 1
    assert resolved[0].result is Result.A_WINS
    assert resolved[0].reason is ResultReason.BREAK
    assert match.phase is Phase.RESOLVED
    assert match.result is Result.A_WINS
    assert match.result_reason is ResultReason.BREAK

    later = tick(match, [], 16)
    assert not any(isinstance(event, MatchResolved) for event in later)
    assert not any(isinstance(event, VillainBroken) for event in later)


def test_ac9_yield_held_for_a_breath_resolves():
    match = _live_match()

    events = tick(match, [HoldYield(VillainId.A)], 600)

    assert sum(isinstance(event, YieldStarted) for event in events) == 1
    yielded = [event for event in events if isinstance(event, VillainYielded)]
    assert len(yielded) == 1
    assert yielded[0].villain_id is VillainId.A
    resolved = [event for event in events if isinstance(event, MatchResolved)]
    assert len(resolved) == 1
    assert resolved[0].result is Result.B_WINS
    assert resolved[0].reason is ResultReason.YIELD
    assert match.phase is Phase.RESOLVED
    assert match.result is Result.B_WINS
    assert match.result_reason is ResultReason.YIELD


def test_ac10_hurt_during_yield_cancels_and_stays_live():
    match = _live_match()
    _place_duel(match, (420, 270), (400, 270))
    match.villains[VillainId.B].facing = Facing.E
    tick(match, [HoldYield(VillainId.A)], 16)

    events = tick(match, [Strike(VillainId.B)], 120)

    cancelled = [event for event in events if isinstance(event, YieldCancelled)]
    assert len(cancelled) == 1
    assert cancelled[0].reason == "HURT"
    assert cancelled[0].villain_id is VillainId.A
    assert not any(isinstance(event, VillainYielded) for event in events)
    assert not any(isinstance(event, MatchResolved) for event in events)
    assert match.phase is Phase.LIVE
    assert match.villains[VillainId.A].yield_started_ms is None


def test_ac13_break_outranks_time_in_the_same_tick():
    match = _live_match()
    match.clock_ms = 16
    match.villains[VillainId.B].hp = 10

    events = tick(
        match,
        [],
        16,
        seed_events=[
            StrikeLanded(
                attacker_id=VillainId.A,
                target_id=VillainId.B,
                damage=12,
                condemn=False,
            )
        ],
    )

    assert any(isinstance(event, VillainBroken) for event in events)
    assert any(isinstance(event, TimeExpired) for event in events)
    resolved = [event for event in events if isinstance(event, MatchResolved)]
    assert len(resolved) == 1
    assert resolved[0].reason is ResultReason.BREAK
    assert resolved[0].result is Result.A_WINS
    assert match.phase is Phase.RESOLVED
    assert match.resolved_latch is True

    later = tick(match, [], 16)
    assert not any(isinstance(event, MatchResolved) for event in later)


def test_ac15_pause_stops_the_clock():
    match = _live_match()
    clock = match.clock_ms

    events = tick(match, [Pause()], 16)

    assert sum(isinstance(event, MatchPaused) for event in events) == 1
    assert match.paused is True
    assert match.clock_ms == clock

    tick(match, [], 16)
    assert match.clock_ms == clock
    assert match.phase is Phase.LIVE


def test_ac12_higher_menace_wins_when_time_expires():
    match = _live_match()
    match.villains[VillainId.A].menace = 30
    match.villains[VillainId.B].menace = 10
    match.clock_ms = 16

    events = tick(match, [], 16)

    resolved = [event for event in events if isinstance(event, MatchResolved)]
    assert len(resolved) == 1
    assert resolved[0].result is Result.A_WINS
    assert resolved[0].reason is ResultReason.TIME
    assert match.phase is Phase.RESOLVED
    assert match.result is Result.A_WINS
    assert match.result_reason is ResultReason.TIME


def test_ac14_combat_after_resolved_is_rejected():
    match = _live_match()
    match.clock_ms = 16
    tick(match, [], 16)
    assert match.phase is Phase.RESOLVED
    usurper = match.villains[VillainId.A]
    tyrant = match.villains[VillainId.B]
    before = (
        usurper.hp,
        usurper.menace,
        usurper.x,
        usurper.y,
        usurper.state,
        tyrant.hp,
        tyrant.menace,
        match.phase,
        match.result,
        match.result_reason,
    )

    events = tick(
        match,
        [
            Move(VillainId.A, Facing.E),
            Face(VillainId.A, Facing.N),
            Strike(VillainId.A),
            HoldYield(VillainId.A),
        ],
        16,
    )

    assert events == []
    assert [item.spec_id for item in match.rejections] == [SPEC_7, SPEC_7, SPEC_7, SPEC_7]
    assert before == (
        usurper.hp,
        usurper.menace,
        usurper.x,
        usurper.y,
        usurper.state,
        tyrant.hp,
        tyrant.menace,
        match.phase,
        match.result,
        match.result_reason,
    )


def test_ac11_equal_menace_at_clock_zero_is_a_draw():
    match = _live_match()
    match.villains[VillainId.A].menace = 20
    match.villains[VillainId.B].menace = 20
    match.clock_ms = 16

    events = tick(match, [], 16)
    resolved = [event for event in events if isinstance(event, MatchResolved)]
    assert len(resolved) == 1
    assert resolved[0].result is Result.DRAW
    assert resolved[0].reason is ResultReason.TIME
    assert match.phase is Phase.RESOLVED
    assert match.result is Result.DRAW
    assert match.result_reason is ResultReason.TIME
    assert match.clock_ms == 0

    later = tick(match, [], 16)
    assert not any(isinstance(event, MatchResolved) for event in later)
