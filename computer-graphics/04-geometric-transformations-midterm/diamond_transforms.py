"""
IT2202 - 04 Performance Task 1 (Midterm)
Geometric Transformations

Draw a 3D diamond using GL_TRIANGLES.
Control translate / rotate / scale with the keyboard.
"""

import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *


# ============================================================
# 1. WINDOW SETUP
# ============================================================

pygame.init()

display = (800, 600)
pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
pygame.display.set_caption("04 Geometric Transformations (Midterm) - Arjune Abayabay")


# ============================================================
# 2. CAMERA / VIEW SETUP
# ============================================================

glEnable(GL_DEPTH_TEST)
gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
glTranslatef(0, 0, -5)
glScalef(0.7, 0.7, 0.7)


# ============================================================
# 3. DIAMOND (OCTAHEDRON) DATA
# ============================================================

# 6 points: top, bottom, and 4 around the middle
vertices = (
    (0, 1, 0),     # 0 top
    (0, -1, 0),    # 1 bottom
    (1, 0, 0),     # 2 +X
    (-1, 0, 0),    # 3 -X
    (0, 0, 1),     # 4 +Z
    (0, 0, -1),    # 5 -Z
)

# 8 triangular faces (upper pyramid + lower pyramid)
triangles = (
    # upper half
    (0, 2, 4),
    (0, 4, 3),
    (0, 3, 5),
    (0, 5, 2),
    # lower half
    (1, 4, 2),
    (1, 3, 4),
    (1, 5, 3),
    (1, 2, 5),
)

# one color per triangle face
face_colors = (
    (1, 0, 0),      # red
    (0, 1, 0),      # green
    (0, 0, 1),      # blue
    (1, 1, 0),      # yellow
    (1, 0, 1),      # magenta
    (0, 1, 1),      # cyan
    (1, 0.5, 0),    # orange
    (0.5, 0, 1),    # purple
)


# ============================================================
# 4. DRAW FUNCTION
# ============================================================

def draw_diamond():
    """Draw the solid 3D diamond using GL_TRIANGLES."""
    glBegin(GL_TRIANGLES)

    for i, triangle in enumerate(triangles):
        glColor3f(*face_colors[i])
        for vertex in triangle:
            glVertex3fv(vertices[vertex])

    glEnd()


# ============================================================
# 5. MAIN LOOP — keyboard geometric transformations
# ============================================================
#
# Translate: Arrow keys / WASD
# Rotate:    Q/E (Y), R/F (X), T/G (Z)
# Scale:     + / -   (or = / -)
#

print("Controls:")
print("  Arrows / WASD  = translate")
print("  Q / E          = rotate Y")
print("  R / F          = rotate X")
print("  T / G          = rotate Z")
print("  + / -          = scale up / down")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.KEYDOWN:
            # --- translation ---
            if event.key in (pygame.K_LEFT, pygame.K_a):
                glTranslatef(-0.2, 0, 0)
            elif event.key in (pygame.K_RIGHT, pygame.K_d):
                glTranslatef(0.2, 0, 0)
            elif event.key in (pygame.K_UP, pygame.K_w):
                glTranslatef(0, 0.2, 0)
            elif event.key in (pygame.K_DOWN, pygame.K_s):
                glTranslatef(0, -0.2, 0)

            # --- rotation ---
            elif event.key == pygame.K_q:
                glRotatef(10, 0, 1, 0)   # Y axis left
            elif event.key == pygame.K_e:
                glRotatef(-10, 0, 1, 0)  # Y axis right
            elif event.key == pygame.K_r:
                glRotatef(10, 1, 0, 0)   # X axis
            elif event.key == pygame.K_f:
                glRotatef(-10, 1, 0, 0)
            elif event.key == pygame.K_t:
                glRotatef(10, 0, 0, 1)   # Z axis
            elif event.key == pygame.K_g:
                glRotatef(-10, 0, 0, 1)

            # --- scaling ---
            elif event.key in (pygame.K_EQUALS, pygame.K_PLUS, pygame.K_KP_PLUS):
                glScalef(1.1, 1.1, 1.1)
            elif event.key in (pygame.K_MINUS, pygame.K_KP_MINUS):
                glScalef(0.9, 0.9, 0.9)

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    draw_diamond()
    pygame.display.flip()
    pygame.time.wait(15)
