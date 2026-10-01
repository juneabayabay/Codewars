"""
IT2605 - 04 Laboratory Exercise 1
Geometric Transformations (Illustrator-equivalent output)

Generates:
  - Abayabay_Arjune_LE04-1.svg  (open in Illustrator → Save As .ai)
  - Abayabay_Arjune_LE04-1.png  (export for eLMS)

Artboard: 1000 x 700 px, RGB
Object size: 100 x 120 px (under 150 px limit)
Reference point: upper-left
"""

from pathlib import Path

from PIL import Image, ImageDraw

OUT_DIR = Path(__file__).resolve().parent
BASE = "Abayabay_Arjune_LE04-1"

ARTBOARD_W, ARTBOARD_H = 1000, 700
OBJ_W, OBJ_H = 100, 120  # under 150 px each

# Lab starting positions (upper-left reference), then transforms
# Object 1 Original:   (100, 100)
# Object 2 Translation: (400, 100) then +200 X, +100 Y → (600, 200)
# Object 3 Scaling:    (100, 400), width × 1.5 (proportions locked)
# Object 4 Rotation:   (500, 400), 30° counterclockwise


def draw_house(draw: ImageDraw.ImageDraw, ox: float, oy: float, scale: float = 1.0, angle_ccw: float = 0.0):
    """Draw a simple house from 4 geometric shapes at upper-left (ox, oy)."""
    import math

    w, h = OBJ_W * scale, OBJ_H * scale

    # Local points (upper-left origin), then rotate around upper-left if needed
    def xf(px, py):
        lx, ly = px * scale, py * scale
        if angle_ccw == 0:
            return (ox + lx, oy + ly)
        # Screen y-down: negative angle gives visual counterclockwise (matches Illustrator)
        rad = math.radians(-angle_ccw)
        c, s = math.cos(rad), math.sin(rad)
        rx = lx * c - ly * s
        ry = lx * s + ly * c
        return (ox + rx, oy + ry)

    # Roof (triangle)
    roof = [xf(0, 45), xf(50, 0), xf(100, 45)]
    # Body (rectangle)
    body = [xf(10, 45), xf(90, 45), xf(90, 120), xf(10, 120)]
    # Door (rectangle)
    door = [xf(40, 75), xf(60, 75), xf(60, 120), xf(40, 120)]
    # Window (square)
    window = [xf(20, 55), xf(35, 55), xf(35, 70), xf(20, 70)]

    draw.polygon(roof, fill=(180, 60, 50), outline=(40, 40, 40))
    draw.polygon(body, fill=(240, 220, 160), outline=(40, 40, 40))
    draw.polygon(door, fill=(120, 80, 40), outline=(40, 40, 40))
    draw.polygon(window, fill=(140, 200, 230), outline=(40, 40, 40))


def make_png():
    img = Image.new("RGB", (ARTBOARD_W, ARTBOARD_H), (245, 245, 248))
    draw = ImageDraw.Draw(img)

    # light artboard border
    draw.rectangle([0, 0, ARTBOARD_W - 1, ARTBOARD_H - 1], outline=(200, 200, 210))

    # labels (small, for clarity — optional for instructor)
    draw.text((100, 78), "1 Original", fill=(80, 80, 90))
    draw.text((600, 178), "2 Translation", fill=(80, 80, 90))
    draw.text((100, 378), "3 Scaling x1.5", fill=(80, 80, 90))
    draw.text((500, 378), "4 Rotation 30°", fill=(80, 80, 90))

    draw_house(draw, 100, 100)                 # Object 1
    draw_house(draw, 600, 200)                 # Object 2 after translation
    draw_house(draw, 100, 400, scale=1.5)      # Object 3 scaled
    draw_house(draw, 500, 400, angle_ccw=30)   # Object 4 rotated CCW

    path = OUT_DIR / f"{BASE}.png"
    img.save(path, "PNG")
    print(f"Wrote {path}")


def make_svg():
    # House group in local coords (0,0 upper-left), size 100x120
    house = """
    <g id="house">
      <!-- roof triangle -->
      <polygon points="0,45 50,0 100,45" fill="#b43c32" stroke="#282828" stroke-width="1.5"/>
      <!-- body rectangle -->
      <rect x="10" y="45" width="80" height="75" fill="#f0dca0" stroke="#282828" stroke-width="1.5"/>
      <!-- door -->
      <rect x="40" y="75" width="20" height="45" fill="#785028" stroke="#282828" stroke-width="1.5"/>
      <!-- window -->
      <rect x="20" y="55" width="15" height="15" fill="#8cc8e6" stroke="#282828" stroke-width="1.5"/>
    </g>
    """

    svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg"
     width="{ARTBOARD_W}" height="{ARTBOARD_H}"
     viewBox="0 0 {ARTBOARD_W} {ARTBOARD_H}">
  <rect width="100%" height="100%" fill="#f5f5f8"/>
  <defs>
    {house}
  </defs>

  <!-- Object 1: Original @ (100, 100) -->
  <use href="#house" x="100" y="100"/>
  <text x="100" y="92" font-family="Arial, sans-serif" font-size="12" fill="#50505a">1 Original</text>

  <!-- Object 2: Translation — start (400,100), then +200,+100 → (600,200) -->
  <use href="#house" x="600" y="200"/>
  <text x="600" y="192" font-family="Arial, sans-serif" font-size="12" fill="#50505a">2 Translation</text>

  <!-- Object 3: Scaling — (100,400), W × 1.5 with proportions locked -->
  <g transform="translate(100,400) scale(1.5)">
    <use href="#house" x="0" y="0"/>
  </g>
  <text x="100" y="392" font-family="Arial, sans-serif" font-size="12" fill="#50505a">3 Scaling x1.5</text>

  <!-- Object 4: Rotation — (500,400), 30° counterclockwise around upper-left -->
  <!-- SVG positive rotate is clockwise, so -30 = CCW 30° -->
  <g transform="translate(500,400) rotate(-30)">
    <use href="#house" x="0" y="0"/>
  </g>
  <text x="500" y="392" font-family="Arial, sans-serif" font-size="12" fill="#50505a">4 Rotation 30°</text>
</svg>
'''
    path = OUT_DIR / f"{BASE}.svg"
    path.write_text(svg.strip() + "\n", encoding="utf-8")
    print(f"Wrote {path}")


if __name__ == "__main__":
    make_svg()
    make_png()
