"""Handler order from section 8.2. Missing slices are left out."""

from __future__ import annotations

import importlib

from game.handlers.clock import handle_clock
from game.handlers.damage import handle_damage
from game.handlers.input import handle_input
from game.handlers.resolve import handle_resolve
from game.handlers.strike import handle_strike

# `break` and `yield` are keywords, so those modules are loaded by name.
handle_break = importlib.import_module("game.handlers.break").handle_break
handle_yield = importlib.import_module("game.handlers.yield").handle_yield

# Presentation is not in this slice.
HANDLERS = (
    handle_input,
    handle_strike,
    handle_damage,
    handle_break,
    handle_yield,
    handle_clock,
    handle_resolve,
)
