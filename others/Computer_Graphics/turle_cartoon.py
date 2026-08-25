"""Animated cute faux-3D capybara playing ball with a penguin."""

import math
import turtle

# ---------------------------------------------------------------------------
# Setup
# ---------------------------------------------------------------------------
SCREEN = turtle.Screen()
SCREEN.setup(width=900, height=700)
SCREEN.bgcolor("#A8D8EA")
SCREEN.title("Capybara & Penguin — Playing! (click to close)")
SCREEN.tracer(0)

t = turtle.Turtle(visible=False)
t.speed(0)
t.pensize(1)

RUNNING = True
FRAME = 0
ELLIPSE_STEPS = 28  # fewer points = smoother animation


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------
def move_to(x, y, heading=0):
    t.penup()
    t.goto(x, y)
    t.setheading(heading)
    t.pendown()


def filled_ellipse(cx, cy, rx, ry, fill, outline=None, steps=None):
    if outline is None:
        outline = fill
    if steps is None:
        steps = ELLIPSE_STEPS
    t.penup()
    t.goto(cx + rx, cy)
    t.pendown()
    t.color(outline, fill)
    t.begin_fill()
    for i in range(steps + 1):
        a = 2 * math.pi * i / steps
        t.goto(cx + rx * math.cos(a), cy + ry * math.sin(a))
    t.end_fill()


def filled_circle_at(cx, cy, r, fill, outline=None):
    filled_ellipse(cx, cy, r, r, fill, outline)


def filled_poly(points, fill, outline=None):
    if outline is None:
        outline = fill
    move_to(points[0][0], points[0][1])
    t.color(outline, fill)
    t.begin_fill()
    for x, y in points[1:]:
        t.goto(x, y)
    t.goto(points[0][0], points[0][1])
    t.end_fill()


def _darken(hex_color, amount=35):
    c = hex_color.lstrip("#")
    if len(c) != 6:
        return hex_color
    r = max(0, int(c[0:2], 16) - amount)
    g = max(0, int(c[2:4], 16) - amount)
    b = max(0, int(c[4:6], 16) - amount)
    return f"#{r:02x}{g:02x}{b:02x}"


def soft_blob(cx, cy, rx, ry, base, mid, hi, outline="#5D4037"):
    """Round soft 3D blob (shadow + body + highlight)."""
    filled_ellipse(cx + 4, cy - 5, rx, ry, _darken(base, 50), outline=_darken(base, 40))
    filled_ellipse(cx, cy, rx, ry, base, outline=outline)
    filled_ellipse(cx - rx * 0.18, cy + ry * 0.22, rx * 0.7, ry * 0.6, mid, outline=mid)
    filled_ellipse(cx - rx * 0.3, cy + ry * 0.36, rx * 0.26, ry * 0.2, hi, outline=hi)


def cute_eye(cx, cy, scale=1.0, look_x=0, look_y=0):
    filled_ellipse(cx, cy, 14 * scale, 16 * scale, "white", outline="#333333")
    px = cx + (2 + look_x) * scale
    py = cy + (-1 + look_y) * scale
    filled_ellipse(px, py, 8 * scale, 10 * scale, "#3E2723", outline="#3E2723")
    filled_circle_at(px + scale, py, 5 * scale, "black", "black")
    filled_circle_at(cx - 2 * scale, cy + 5 * scale, 3.5 * scale, "white", "white")


def blush(cx, cy):
    filled_ellipse(cx, cy, 16, 9, "#FFAB91", outline="#FFAB91")


def draw_heart(cx, cy, scale=1.0):
    s = 12 * scale
    filled_ellipse(cx - s * 0.55, cy + s * 0.2, s * 0.65, s * 0.6, "#F48FB1", outline="#F48FB1")
    filled_ellipse(cx + s * 0.55, cy + s * 0.2, s * 0.65, s * 0.6, "#F48FB1", outline="#F48FB1")
    filled_poly(
        [
            (cx - s * 1.15, cy + s * 0.1),
            (cx + s * 1.15, cy + s * 0.1),
            (cx, cy - s * 1.1),
        ],
        "#F48FB1",
        outline="#F48FB1",
    )


# ---------------------------------------------------------------------------
# Background (static pieces + drifting clouds)
# ---------------------------------------------------------------------------
def draw_background(frame):
    # Hills
    filled_ellipse(0, -280, 520, 120, "#81C784", outline="#66BB6A")
    filled_ellipse(-220, -300, 260, 90, "#A5D6A7", outline="#81C784")
    filled_ellipse(260, -310, 240, 85, "#A5D6A7", outline="#81C784")

    # Ground contact shadows (stretch with hop)
    filled_ellipse(-80, -245, 160, 28, "#66BB6A", outline="#66BB6A")
    filled_ellipse(160, -250, 90, 22, "#66BB6A", outline="#66BB6A")

    # Sun pulse
    pulse = 1 + 0.04 * math.sin(frame * 0.08)
    soft_blob(320, 260, 45 * pulse, 45 * pulse, "#FFE082", "#FFF59D", "#FFFDE7", "#FFD54F")

    # Drifting clouds
    drift = (frame * 0.35) % 900 - 450
    for base_x, cy, spread in ((-220, 235, 60), (80, 250, 55), (drift, 220, 50)):
        for dx in (-spread * 0.6, 0, spread * 0.55):
            filled_ellipse(base_x + dx, cy, 36, 22, "#E3F2FD", outline="#E3F2FD")


# ---------------------------------------------------------------------------
# Characters (positions driven by animation state)
# ---------------------------------------------------------------------------
def draw_capybara(ox, oy, paw_lift=0, look_x=2, bob=0):
    oy = oy + bob

    # back legs
    soft_blob(ox - 55, oy - 145, 28, 38, "#8D6E63", "#A1887F", "#BCAAA4", "#5D4037")
    soft_blob(ox + 70, oy - 145, 28, 38, "#8D6E63", "#A1887F", "#BCAAA4", "#5D4037")
    filled_ellipse(ox - 55, oy - 185, 32, 14, "#6D4C41", outline="#5D4037")
    filled_ellipse(ox + 70, oy - 185, 32, 14, "#6D4C41", outline="#5D4037")

    # body
    soft_blob(ox + 10, oy - 70, 115, 85, "#A1887F", "#BCAAA4", "#D7CCC8", "#5D4037")
    filled_ellipse(ox + 15, oy - 95, 70, 40, "#D7CCC8", outline="#D7CCC8")

    # front legs — one paw lifts to bat the ball
    soft_blob(ox - 40, oy - 130 + paw_lift * 0.3, 22, 42, "#8D6E63", "#A1887F", "#BCAAA4", "#5D4037")
    soft_blob(
        ox + 45 + paw_lift * 0.15,
        oy - 130 + paw_lift,
        22,
        42,
        "#8D6E63",
        "#A1887F",
        "#BCAAA4",
        "#5D4037",
    )
    filled_ellipse(ox - 40, oy - 175 + paw_lift * 0.2, 26, 12, "#6D4C41", outline="#5D4037")
    filled_ellipse(
        ox + 45 + paw_lift * 0.15,
        oy - 175 + paw_lift * 0.85,
        26,
        12,
        "#6D4C41",
        outline="#5D4037",
    )

    # head
    soft_blob(ox - 70, oy + 20, 70, 58, "#A1887F", "#BCAAA4", "#EFEBE9", "#5D4037")
    soft_blob(ox - 115, oy + 5, 42, 32, "#8D6E63", "#A1887F", "#BCAAA4", "#5D4037")
    filled_ellipse(ox - 145, oy + 12, 10, 8, "#4E342E", outline="#3E2723")
    filled_ellipse(ox - 145, oy - 2, 10, 8, "#4E342E", outline="#3E2723")

    move_to(ox - 130, oy - 12, -40)
    t.color("#5D4037")
    t.pensize(2)
    t.circle(22, 70)
    t.pensize(1)

    soft_blob(ox - 55, oy + 70, 16, 20, "#8D6E63", "#A1887F", "#BCAAA4", "#5D4037")
    soft_blob(ox - 25, oy + 75, 16, 20, "#8D6E63", "#A1887F", "#BCAAA4", "#5D4037")
    filled_ellipse(ox - 55, oy + 70, 7, 9, "#FFAB91", outline="#FFAB91")
    filled_ellipse(ox - 25, oy + 75, 7, 9, "#FFAB91", outline="#FFAB91")

    cute_eye(ox - 90, oy + 35, 1.05, look_x=look_x, look_y=1)
    cute_eye(ox - 50, oy + 40, 1.05, look_x=look_x, look_y=1)
    blush(ox - 105, oy + 8)
    blush(ox - 40, oy + 12)
    soft_blob(ox - 40, oy + 55, 14, 12, "#FF9800", "#FFB74D", "#FFE0B2", "#EF6C00")


def draw_penguin(ox, oy, hop=0, flipper=0, lean=0):
    oy = oy + hop
    ox = ox + lean

    # back flipper
    soft_blob(ox + 55, oy - 40, 18, 48, "#212121", "#424242", "#616161", "#000000")

    # body + belly
    soft_blob(ox, oy - 40, 55, 85, "#212121", "#424242", "#616161", "#000000")
    soft_blob(ox, oy - 50, 38, 62, "#FAFAFA", "#FFFFFF", "#FFFFFF", "#E0E0E0")

    # feet (squash a little when landing)
    squash = max(0, -hop) * 0.08
    filled_ellipse(ox - 22, oy - 130, 24 + squash, 12 - squash * 0.3, "#FF9800", outline="#EF6C00")
    filled_ellipse(ox + 22, oy - 130, 24 + squash, 12 - squash * 0.3, "#FF9800", outline="#EF6C00")

    # waving / kicking flipper
    soft_blob(
        ox - 60 - flipper * 0.2,
        oy - 10 + flipper,
        16,
        42,
        "#212121",
        "#424242",
        "#757575",
        "#000000",
    )

    # motion streaks when flipper is up
    if flipper > 12:
        t.color("#90CAF9")
        t.pensize(2)
        for i, (dx, dy) in enumerate(((-25, 30), (-32, 15), (-20, 8))):
            move_to(ox - 60 + dx, oy - 10 + flipper + dy, 140 + i * 12)
            t.forward(10 + flipper * 0.15)
        t.pensize(1)

    # head
    soft_blob(ox, oy + 55, 42, 40, "#212121", "#424242", "#757575", "#000000")
    filled_ellipse(ox - 16, oy + 55, 14, 16, "#FAFAFA", outline="#FAFAFA")
    filled_ellipse(ox + 16, oy + 55, 14, 16, "#FAFAFA", outline="#FAFAFA")
    cute_eye(ox - 14, oy + 58, 0.85, look_x=-2)
    cute_eye(ox + 14, oy + 58, 0.85, look_x=-2)
    blush(ox - 28, oy + 40)
    blush(ox + 28, oy + 40)

    filled_poly(
        [(ox - 8, oy + 48), (ox + 8, oy + 48), (ox, oy + 32)],
        "#FF9800",
        outline="#EF6C00",
    )
    filled_ellipse(ox, oy + 44, 5, 3, "#FFB74D", outline="#FFB74D")


def draw_ball(cx, cy, spin=0):
    soft_blob(cx, cy, 26, 26, "#EF5350", "#FF8A80", "#FFCDD2", outline="#C62828")
    # spinning stripe
    ang = spin
    filled_ellipse(
        cx + 10 * math.cos(ang),
        cy + 8 * math.sin(ang),
        22,
        5,
        "#E53935",
        outline="#E53935",
    )
    filled_ellipse(cx - 8, cy + 10, 7, 4, "#FFEBEE", outline="#FFEBEE")


def draw_floating_hearts(frame):
    hearts = (
        (20, 0.7, 0.05, 0.0),
        (90, 0.55, 0.07, 1.5),
        (-200, 0.5, 0.06, 3.0),
        (250, 0.45, 0.08, 2.2),
    )
    for hx, scale, speed, phase in hearts:
        hy = -40 + ((frame * speed * 40 + phase * 40) % 280)
        wobble = 12 * math.sin(frame * 0.1 + phase)
        draw_heart(hx + wobble, hy, scale)


# ---------------------------------------------------------------------------
# Animation
# ---------------------------------------------------------------------------
def scene_state(frame):
    """Compute positions / poses for this frame."""
    # Ball arcs back and forth between friends
    cycle = (frame * 0.045) % (2 * math.pi)
    ball_x = 40 + 110 * math.sin(cycle)
    ball_y = -90 + abs(math.cos(cycle)) * 110  # bounce arc
    ball_spin = frame * 0.2

    # Capybara gently rocks and bats when ball is near
    cap_bob = 4 * math.sin(frame * 0.12)
    near_cap = max(0, 1 - abs(ball_x - (-20)) / 90)
    paw_lift = 35 * near_cap * max(0, math.sin(cycle + 0.4))
    cap_x = -90 + 8 * math.sin(frame * 0.06)
    look = 3 if ball_x > -40 else -1

    # Penguin hops and waves toward the ball
    hop_wave = abs(math.sin(frame * 0.16))
    hop = hop_wave * 28
    flipper = 10 + 30 * abs(math.sin(frame * 0.2))
    near_pen = max(0, 1 - abs(ball_x - 150) / 100)
    lean = -18 * near_pen
    pen_x = 170 + 6 * math.sin(frame * 0.09)

    return {
        "ball": (ball_x, ball_y, ball_spin),
        "cap": (cap_x, -40, paw_lift, look, cap_bob),
        "pen": (pen_x, -30, hop, flipper, lean),
    }


def draw_frame():
    global FRAME
    if not RUNNING:
        return

    FRAME += 1
    state = scene_state(FRAME)

    t.clear()
    draw_background(FRAME)

    bx, by, spin = state["ball"]
    # shadow under ball
    filled_ellipse(bx, -230, 22, 8, "#66BB6A", outline="#66BB6A")

    cx, cy, paw, look, bob = state["cap"]
    draw_capybara(cx, cy, paw_lift=paw, look_x=look, bob=bob)

    px, py, hop, flip, lean = state["pen"]
    # penguin ground shadow squashes when hopping
    shadow_w = 70 - hop * 0.8
    filled_ellipse(px + lean, -248, max(30, shadow_w), 16, "#66BB6A", outline="#66BB6A")
    draw_penguin(px, py, hop=hop, flipper=flip, lean=lean)

    draw_ball(bx, by, spin=spin)
    draw_floating_hearts(FRAME)

    SCREEN.update()
    SCREEN.ontimer(draw_frame, 40)  # ~25 FPS


def stop(_x=None, _y=None):
    global RUNNING
    RUNNING = False
    try:
        SCREEN.bye()
    except turtle.Terminator:
        pass


# ---------------------------------------------------------------------------
# Go!
# ---------------------------------------------------------------------------
SCREEN.onscreenclick(stop)
draw_frame()
SCREEN.mainloop()
