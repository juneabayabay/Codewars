# No Heroes Left

| | |
|---|---|
| Kind | 2D one-screen duel |
| Stack | Python 3, pygame |
| Players | 1 human vs 1 local rival |
| Length | One minute, then a result |
| Document | Spec-event-driven game design |

The player is a villain. The opponent is a villain. No hero enters the room.

This file is the source of truth for the game. Story explains what the moment means. Specs say what the build must do. Events are the only facts allowed to change a match.

---

## 1. How this document works

Read it from top to bottom. Later sections depend on earlier ones.

| Term | Meaning |
|---|---|
| SPEC | A numbered rule. If play breaks it, the build is wrong. |
| Command | An intent for this frame: move, strike, yield, start. |
| Event | A fact that already happened, written in the past tense. |
| Handler | Code that reads the current state and may emit the next event. |
| Invariant | A rule that is still true after every applied event. |
| Flow | A numbered path from a command to a result. |

One simulation tick, always in this order:

1. Read devices and the rival brain. Build a list of commands.
2. Accept or reject each command by checking the spec.
3. Emit events for accepted commands.
4. Run handlers in the fixed order in section 8.
5. Store the new state.
6. Draw that state.

Drawing reads state. Drawing emits nothing.

Match phase moves in one direction:

```text
BOOT → COUNTDOWN → LIVE → RESOLVED
```

A resolved match stays resolved until `StartMatch` opens a new one.

---

## 2. Story

### 2.1 Beginning

The king has been dead for three nights. The throne room is open to the weather. The guards have left. The city has locked its doors.

Two people still want the chair.

**The Tyrant** already ruled this city from the dark. Laws, gallows, and fear kept the streets quiet. With the king gone, the Tyrant comes to sit in the open and make the cruelty official.

**The Usurper** killed the king. Years of cutting ropes and feeding the same fear were for this walk into the hall. A crown on any other head is only another neck.

They meet on the same stone floor. The throne is behind them. Neither sits yet. There is no third fighter on the road.

### 2.2 Middle

A bell gives them one minute.

The Tyrant is heavy, long-armed, and hard to put down. The Usurper is faster, shorter in reach, and becomes more dangerous each time a blow lands. The fear they spread is visible. In the rules it is called menace. When menace is full, the next blow is a condemn and cuts twice as deep.

The player controls the Usurper. The Tyrant is a local rival: step in, strike when the Usurper is close, step away when nearly broken.

The room does not change. No door opens. The minute is the whole war.

### 2.3 End

The minute closes in one of three ways.

| Ending | What happened | Who sits |
|---|---|---|
| Break | One villain's health reaches 0. | The one still standing. |
| Yield | One villain holds surrender for a full breath and is not hit. | The one who did not blink. |
| Bell | Time runs out with both still up. | The one with more menace. Equal menace leaves the throne empty. |

Whoever wins, the city does not. A draw means the throne stays empty and the city burns with no master.

The lines shown on screen for each result are in section 11.

---

## 3. Design pillars

These are the promises the spec is protecting.

1. **Both are evil.** The Usurper is not a secret hero. Winning is taking a city that will suffer either way.
2. **One room, one minute.** No stages, no loot, no second fight inside a match.
3. **Asymmetry you can read.** Speed against weight. Short blade against long arm. Menace against a larger health pool.
4. **Events own the truth.** Health, menace, and the winner change only because an event was applied.
5. **A slow frame is not a second hit.** The simulation step is fixed. Rendering can hitch. The strike resolves once.

---

## 4. Cast

### 4.1 Roles

| | The Usurper | The Tyrant |
|---|---|---|
| Id | `A` | `B` |
| Controlled by | Human | Rival brain, version 1 |
| Fantasy | Fast usurper who grows sharper as fear spreads | Old power with reach and a larger body |
| Starts | Menace 0. Has to earn the condemn. | Menace 10. The room was already afraid. |

### 4.2 Starting numbers

| Field | Usurper `A` | Tyrant `B` |
|---|---|---|
| `max_hp` | 100 | 130 |
| `hp` | 100 | 130 |
| Speed | 180 px/s | 120 px/s |
| Strike reach | 36 px | 52 px |
| Strike damage | 12 | 16 |
| Strike recovery | 280 ms | 420 ms |
| Menace | 0 | 10 |
| Menace gained on a normal hit | +8 | +5 |

### 4.3 Shared fields

Every villain has:

`id`, `name`, `role`, `hp`, `max_hp`, `menace`, `x`, `y`, `facing`, `state`, `strike_started_ms`, `yield_started_ms`.

States:

```text
IDLE, MOVING, STRIKING, HURT, BROKEN, YIELDED
```

Facing:

```text
N, E, S, W
```

### 4.4 Condemn

- Menace lives in `0..100`.
- A strike accepted while menace is already `100` is a condemn.
- Condemn damage is the role damage times 2.
- After that strike is resolved, menace becomes `0`.
- Usurper condemn damage is 24. Tyrant condemn damage is 32.

---

## 5. Arena and clock

| Rule | Value |
|---|---|
| Playable room | `960 × 540` pixels |
| Window | That room, plus a thin top bar for names, health, menace, and the clock |
| Combat clock | 60 seconds (`60000` ms) once the match is `LIVE` |
| Countdown before live | 3 seconds |
| Bodies | May overlap. There is no push. |
| Feet | Cannot leave the rectangle. A move is clamped to the edge. |
| Hit test | Once, at 120 ms after `StrikeStarted`, and only inside reach in the facing direction |

The throne is set dressing behind the fight. It is not a zone and it does not heal.

Simulation step is fixed at `16` ms. If a frame takes longer, the loop runs extra steps, then draws once.

---

## 6. Controls and commands

### 6.1 Human mapping

| Input | Command |
|---|---|
| W A S D, or arrow keys | `Move` in that direction and `Face` the same way |
| J, or Space | `Strike` |
| K held | `HoldYield` |
| K released early | `ReleaseYield` |
| Esc | `Pause` while counting down or live. `Resume` if already paused. |
| Enter on the result screen | `StartMatch` |

### 6.2 Command table

| Command | Who | Accepted when |
|---|---|---|
| `StartMatch` | Player or system | Phase is `BOOT` or `RESOLVED` |
| `Move` | Player or rival | Phase is `LIVE`, state is `IDLE` or `MOVING`, not paused |
| `Face` | Player or rival | Phase is `LIVE`, state is not `BROKEN` or `YIELDED`, not paused |
| `Strike` | Player or rival | Phase is `LIVE`, state is `IDLE` or `MOVING`, not paused |
| `HoldYield` | Player | Phase is `LIVE`, state is `IDLE`, `MOVING`, or `HURT`, not paused |
| `ReleaseYield` | Player | A yield hold is active for that villain |
| `Pause` | Player | Phase is `COUNTDOWN` or `LIVE` |
| `Resume` | Player | The match is paused |

Rejected commands do not become match events. Log them beside the match as `CommandRejected(command, spec_id)` so a failed input points at the rule that blocked it.

While paused, the clock does not move and no strike timer advances.

### 6.3 Rival brain, version 1

The Tyrant builds commands in this priority. No pathfinding. The room is an open rectangle.

1. If the Usurper is inside Tyrant reach and the Tyrant may strike, emit `Strike`.
2. If Tyrant health is below 30 and the Usurper state is `STRIKING`, step away along the nearest wall.
3. Otherwise face the Usurper and move toward the Usurper.

---

## 7. State the events own

```text
Match
  phase: BOOT | COUNTDOWN | LIVE | RESOLVED
  paused: bool
  clock_ms: int
  countdown_ms: int
  result: None | A_WINS | B_WINS | DRAW
  result_reason: None | BREAK | YIELD | TIME
  villains: A, B
  rng_seed: int
  resolved_latch: bool
```

Invariants, true after every applied event:

- **INV-1.** A match contains exactly two villains.
- **INV-2.** `0 <= hp <= max_hp` and `0 <= menace <= 100`.
- **INV-3.** Phase only moves `BOOT → COUNTDOWN → LIVE → RESOLVED`.
- **INV-4.** `resolved_latch` is set by the first `MatchResolved`. A second end event in the same tick does not emit another result.
- **INV-5.** Commands never write `hp`, `menace`, `phase`, or `result` directly.

Keep the event list for the current match. When a result looks wrong, replay the list.

---

## 8. Events and handlers

### 8.1 Event catalog

| ID | Event | Payload | When |
|---|---|---|---|
| E1 | `MatchStarted` | seed, room size, both loadouts | `StartMatch` accepted |
| E2 | `CountdownTicked` | seconds_left | Each second of the opening count |
| E3 | `MatchWentLive` | — | Countdown reaches 0 |
| E4 | `VillainMoved` | id, from_xy, to_xy | `Move` accepted and clamped |
| E5 | `VillainFaced` | id, facing | Facing changed |
| E6 | `StrikeStarted` | id, facing, condemn | `Strike` accepted |
| E7 | `StrikeWhiffed` | id | Active frame, target not in the cone |
| E8 | `StrikeLanded` | attacker_id, target_id, damage, condemn | Active frame, target in the cone |
| E9 | `MenaceChanged` | id, before, after | A hit grants menace, or a condemn resets it |
| E10 | `VillainHurt` | id, hp_before, hp_after | Damage applied |
| E11 | `VillainBroken` | id | Health reached 0 |
| E12 | `YieldStarted` | id | `HoldYield` accepted |
| E13 | `YieldCancelled` | id, reason | Released early, or hit during the hold |
| E14 | `VillainYielded` | id | Hold lasted 600 ms without a cancel |
| E15 | `ClockTicked` | clock_ms | Each live step that is not paused |
| E16 | `TimeExpired` | menace_a, menace_b | Clock reached 0 |
| E17 | `MatchResolved` | result, reason | First legal end of the match |
| E18 | `StrikeRecovered` | id | Recovery time elapsed |
| E19 | `MatchPaused` | — | `Pause` accepted |
| E20 | `MatchResumed` | — | `Resume` accepted |

### 8.2 Handler order

Run these in this order every tick. Clear the command list after the input handler so later handlers cannot see the same command twice.

| Order | Handler | Responsibility |
|---|---|---|
| 1 | Input | Commands become move, face, strike, yield, pause, and start events. |
| 2 | Strike timer | At +120 ms emit `StrikeLanded` or `StrikeWhiffed`. At recovery time emit `StrikeRecovered`. |
| 3 | Damage | `StrikeLanded` writes health and menace. Emits `VillainHurt` and `MenaceChanged`. |
| 4 | Break | `VillainHurt` with `hp_after == 0` emits `VillainBroken`. |
| 5 | Yield | A finished hold emits `VillainYielded`. A hurt on that id emits `YieldCancelled`. |
| 6 | Clock | Emits `ClockTicked`. At 0 emits `TimeExpired`. Skipped while paused. |
| 7 | Resolve | The first of break, yield, or time emits one `MatchResolved` and sets the latch. |
| 8 | Presentation | Draws. Emits nothing. |

Condemn order inside Damage: apply doubled damage, emit the hurt, then set that attacker's menace to 0 and emit `MenaceChanged` ending at 0.

---

## 9. Flows, from the first prompt to the last result

### Flow A — Boot to the bell

1. The file loads. Phase is `BOOT`. The throne room is on screen. No health has moved.
2. The player confirms. Command `StartMatch`.
3. Emit `MatchStarted`. Spawn both villains from section 4. Phase is `COUNTDOWN`. `countdown_ms` is 3000.
4. Each second, emit `CountdownTicked` with 3, then 2, then 1.
5. At 0, emit `MatchWentLive`. Phase is `LIVE`. `clock_ms` is 60000.

### Flow B — Circle

1. The player holds a direction. Commands `Move` and `Face`.
2. `step = min(speed * dt_seconds, distance_to_edge)`.
3. Emit `VillainFaced` when the facing is new.
4. Emit `VillainMoved` with the clamped point.
5. State is `MOVING` while a move is held.
6. A later tick with no move, and with the villain not striking, returns state to `IDLE`.

### Flow C — A normal hit

Example: Usurper menace is 40, state is `IDLE`, Tyrant is inside 36 px and inside the facing cone.

1. Command `Strike`.
2. Emit `StrikeStarted(A, facing, condemn=false)`. State is `STRIKING`.
3. At +120 ms emit `StrikeLanded(A, B, damage=12, condemn=false)`.
4. Emit `VillainHurt(B, hp_before=130, hp_after=118)`.
5. Emit `MenaceChanged(A, before=40, after=48)`.
6. At +280 ms emit `StrikeRecovered(A)`. State is `IDLE`.

If the target is outside the cone at the active frame, emit `StrikeWhiffed` and leave health and menace unchanged.

A `Strike` command while state is `STRIKING` is `CommandRejected` under SPEC-18. No second `StrikeStarted` is emitted.

### Flow D — Condemn, then a break

1. Attacker menace is 100. `Strike` is accepted.
2. Emit `StrikeStarted(..., condemn=true)`.
3. On a hit, damage is role damage times 2.
4. Emit `StrikeLanded`, then `VillainHurt`, then `MenaceChanged` ending at 0.
5. If the target's health is 0, emit `VillainBroken`.
6. Emit `MatchResolved` for the other villain, reason `BREAK`.
7. Phase is `RESOLVED`. Further combat commands are rejected until `StartMatch`.

Health never goes below 0. A hit that would pass 0 clamps to 0, then the break event fires.

### Flow E — Yield

1. The player holds K. Emit `YieldStarted` on the first accepted frame.
2. If the hold reaches 600 ms with no cancel, emit `VillainYielded`.
3. Emit `MatchResolved` for the other villain, reason `YIELD`.
4. If the yielding villain is hurt during the hold, emit `YieldCancelled(reason=HURT)`. The phase stays `LIVE`.
5. If K is released early, emit `YieldCancelled(reason=RELEASED)`.

The Tyrant does not yield in version 1.

### Flow F — The bell

1. Phase is `LIVE`. Nobody is broken or yielded. `clock_ms` reaches 0.
2. Emit `TimeExpired(menace_a, menace_b)`.
3. Higher menace wins. Equal menace is `DRAW`.
4. Emit `MatchResolved`, reason `TIME`.

### Flow G — Two endings, one tick

If `VillainBroken` and `TimeExpired` are both emitted before Resolve runs, Resolve emits one `MatchResolved` with reason `BREAK` and sets the latch. The time result is not applied.

Priority inside Resolve:

```text
BREAK, then YIELD, then TIME
```

### Flow H — Again

1. Phase is `RESOLVED`. The result line from section 11 is on screen.
2. Enter sends `StartMatch`.
3. The previous event log is cleared.
4. Flow A runs again with a new seed.

---

## 10. Feature spec

### 10.1 Match

- **SPEC-1.** A match is one arena, two villains, and one clock.
- **SPEC-2.** Combat commands are accepted only in phase `LIVE`, and only when the match is not paused.
- **SPEC-3.** The human controls villain A. Villain B is the rival brain in section 6.3.
- **SPEC-4.** The live clock starts at 60000 ms and decreases by the fixed step.
- **SPEC-5.** The match ends on the first applied end: a break, a yield, or time.
- **SPEC-6.** The result is exactly one of `A_WINS`, `B_WINS`, `DRAW`.
- **SPEC-7.** After `RESOLVED`, every command except `StartMatch` is rejected.

### 10.2 Bodies and space

- **SPEC-8.** `hp` stays inside `0..max_hp`. `menace` stays inside `0..100`.
- **SPEC-9.** A villain in `BROKEN` or `YIELDED` accepts no move and no strike.
- **SPEC-10.** A move that would leave the room is clamped to the edge. The emitted `to_xy` is inside the room.
- **SPEC-11.** Overlap does not push either villain.

### 10.3 Combat

- **SPEC-12.** `Strike` is accepted only from `IDLE` or `MOVING`.
- **SPEC-13.** The attacker stays in `STRIKING` until `StrikeRecovered`.
- **SPEC-14.** The hit test runs once, at 120 ms, in the facing direction, within that role's reach.
- **SPEC-15.** A hit reduces the target's health by the damage on `StrikeLanded` and grants the attacker's menace gain, capped at 100.
- **SPEC-16.** A strike accepted at menace 100 is a condemn: damage times 2, then menace is set to 0.
- **SPEC-17.** Health 0 emits `VillainBroken` and that villain loses, even with higher menace.
- **SPEC-18.** A second strike during `STRIKING` is rejected and does not emit `StrikeStarted`.

### 10.4 Yield, time, and presentation

- **SPEC-19.** Yield completes at 600 ms of continuous hold.
- **SPEC-20.** A hurt or an early release cancels the yield and does not resolve the match.
- **SPEC-21.** At clock 0, higher menace wins. Equal menace is `DRAW`.
- **SPEC-22.** Break outranks yield, and yield outranks time, when more than one end is pending in the same tick.
- **SPEC-23.** The screen shows both names, both health bars, both menace bars, the clock, and one result line when the phase is `RESOLVED`.
- **SPEC-24.** The two villains use different colors and silhouettes.
- **SPEC-25.** A normal hit plays a short flash on the target. A condemn plays a stronger flash.
- **SPEC-26.** One strike produces at most one of `StrikeLanded` or `StrikeWhiffed`, including when several fixed steps run inside one rendered frame.

---

## 11. Result lines

Show exactly one line when the phase becomes `RESOLVED`.

| Result | Reason | Line | Version 1 |
|---|---|---|---|
| `A_WINS` | `BREAK` | The Tyrant breaks. The Usurper takes the chair. | Reachable |
| `A_WINS` | `YIELD` | The Tyrant yields. The city hears it. | Reserved. The Tyrant has no yield command yet. |
| `A_WINS` | `TIME` | The bell. Fear keeps the crown on the Usurper. | Reachable |
| `B_WINS` | `BREAK` | The Usurper breaks. The old fear sits the throne. | Reachable |
| `B_WINS` | `YIELD` | The Usurper yields. The knife was never enough. | Reachable. The player held K for 600 ms. |
| `B_WINS` | `TIME` | The bell. The Tyrant's fear was older, and it holds. | Reachable |
| `DRAW` | `TIME` | The bell. Neither claim holds. The city burns anyway. | Reachable |

Enter returns to Flow A.

---

## 12. Code map

Rules stay free of pygame so the acceptance tests can run without a window.

```text
game/
  main.py                 loop: fixed tick, then one draw
  spec_ids.py             SPEC constants used in reject logs
  model.py                Match, Villain, enums
  commands.py             command dataclasses
  events.py               event dataclasses
  bus.py                  queue for a single tick
  handlers/
    input.py
    strike.py
    damage.py
    break.py
    yield.py
    clock.py
    resolve.py
  rival.py                Tyrant commands, section 6.3
  view.py                 pygame drawing only
tests/
  test_match_flow.py      section 13
```

Shape of one tick:

```python
def tick(match: Match, commands: list[Command], dt_ms: int) -> list[Event]:
    bus = EventBus()
    for handler in HANDLERS:
        handler(match, commands, bus, dt_ms)
        commands = []
    return bus.drain()
```

`HANDLERS` is the order in section 8.2, without Presentation. `main.py` draws after the steps for that frame.

---

## 13. Acceptance tests

Each test feeds commands into `tick` and reads events. No window.

| Test | Given | Expect |
|---|---|---|
| AC-1 | `StartMatch` from `BOOT` | `MatchStarted`, phase `COUNTDOWN` |
| AC-2 | Countdown runs out | Exactly one `MatchWentLive` |
| AC-3 | Move into a wall | `VillainMoved.to_xy` is inside the room |
| AC-4 | `Strike` while `STRIKING` | `CommandRejected` citing SPEC-18, no second `StrikeStarted` |
| AC-5 | Target outside the cone at +120 ms | `StrikeWhiffed`, health unchanged |
| AC-6 | Target inside the cone | `StrikeLanded`, health drops by role damage |
| AC-7 | Menace is 100, then a hit | Damage times 2, menace ends at 0 |
| AC-8 | Damage would pass 0 | Health is 0, one `VillainBroken`, one `MatchResolved` with `BREAK` |
| AC-9 | Yield held 600 ms, no hit | `VillainYielded`, opponent wins, reason `YIELD` |
| AC-10 | Hit during the yield hold | `YieldCancelled`, phase still `LIVE` |
| AC-11 | Clock 0, menace 20 and 20 | `MatchResolved(DRAW, TIME)` |
| AC-12 | Clock 0, menace 30 and 10 | Higher menace wins, reason `TIME` |
| AC-13 | Break and clock 0 in one tick | One result, reason `BREAK` |
| AC-14 | Any combat command after `RESOLVED` | Rejected, state unchanged |
| AC-15 | Pause during `LIVE` | `MatchPaused`, clock unchanged across the next tick |
| AC-16 | Two fixed steps in one frame for one strike | One of `StrikeLanded` or `StrikeWhiffed`, never both |

---

## 14. Build order

1. Model, events, bus, and AC-1, AC-8, AC-11. No graphics.
2. Move, clamp, and face. AC-3.
3. Strike timing, cone, damage, menace, condemn. AC-4 through AC-7 and AC-16.
4. Yield, pause, and the resolve latch. AC-9, AC-10, AC-13, AC-15.
5. A pygame window: bars, clock, two rectangles as the villains.
6. The rival brain from section 6.3.
7. Replace the rectangles with silhouettes. Add the hit flash and the condemn flash.

Step 5 is the first playable build. Rectangles are enough while the tests are going green.

---

## 15. Out of scope for version 1

These need new specs and new events. They are not hidden inside the handlers above.

- A second human on the same keyboard.
- Online play.
- Extra rooms, loot, or dialogue.
- More than two villains.
- A Tyrant yield command.
- Saving a match, or a meta unlock.

Version 1 is finished when AC-1 through AC-16 pass and the six reachable result lines in section 11 render with the correct text.
