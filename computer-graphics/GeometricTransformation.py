"""
IT2202 - 04 Laboratory Exercise 2
Geometric Transformations Using Python
Scale, translate, and rotate a cube with OpenGL + Pygame.
"""

import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *


# ============================================================
# 1. WINDOW SETUP
# ============================================================

pygame.init()  # start pygame

display = (800, 600)  # window width and height
pygame.display.set_mode(display, DOUBLEBUF | OPENGL)  # create OpenGL window
pygame.display.set_caption("04 Lab 1")  # lab window title


# ============================================================
# 2. CAMERA / VIEW SETUP
# ============================================================

# draw nearer objects in front of farther ones
glEnable(GL_DEPTH_TEST)

# set 3D perspective (field of view, aspect ratio, near, far)
gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)

glTranslatef(0, 0, -5)   # move camera back so the cube is visible
glScalef(0.5, 0.5, 0.5)  # shrink the cube (lab step 6)


# ============================================================
# 3. CUBE DATA
# ============================================================

# 8 corner points of the cube (x, y, z)
vertices = (
    (1, 1, 1),      # 0
    (1, 1, -1),     # 1
    (1, -1, -1),    # 2
    (1, -1, 1),     # 3
    (-1, 1, 1),     # 4
    (-1, -1, -1),   # 5
    (-1, -1, 1),    # 6
    (-1, 1, -1),    # 7
)

# 12 triangles = 6 faces x 2 triangles each
triangles = (
    (0, 1, 2), (0, 2, 3),  # right face  (+X)
    (4, 6, 5), (4, 5, 7),  # left face   (-X)
    (0, 4, 7), (0, 7, 1),  # top face    (+Y)
    (3, 2, 5), (3, 5, 6),  # bottom face (-Y)
    (0, 3, 6), (0, 6, 4),  # front face  (+Z)
    (1, 7, 5), (1, 5, 2),  # back face   (-Z)
)

# RGB color for each face (one color per triangle pair)
face_colors = (
    (1, 0, 0),  # red
    (0, 1, 0),  # green
    (0, 0, 1),  # blue
    (1, 1, 0),  # yellow
    (1, 0, 1),  # magenta
    (0, 1, 1),  # cyan
)


# ============================================================
# 4. DRAW FUNCTION
# ============================================================

def draw_cube():
    """Draw the solid cube using colored triangles."""
    glBegin(GL_TRIANGLES)  # start drawing filled triangles

    for i, triangle in enumerate(triangles):
        # change color every 2 triangles (each face)
        if i % 2 == 0:
            glColor3f(*face_colors[i // 2])

        # plot the 3 vertices of this triangle
        for vertex in triangle:
            glVertex3fv(vertices[vertex])

    glEnd()  # finish drawing


# ============================================================
# 5. MAIN LOOP
# ============================================================

while True:
    # --- handle window / keyboard events ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        # move the cube with keyboard (translate)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:          # lab sample: A = left
                glTranslatef(-1, 0, 0)
            elif event.key == pygame.K_LEFT:     # arrow left
                glTranslatef(-1, 0, 0)
            elif event.key == pygame.K_RIGHT:    # arrow right
                glTranslatef(1, 0, 0)
            elif event.key == pygame.K_UP:       # arrow up
                glTranslatef(0, 1, 0)
            elif event.key == pygame.K_DOWN:     # arrow down
                glTranslatef(0, -1, 0)

    # spin the cube a little each frame
    glRotatef(1, 1, 1, 1)

    # clear previous frame (color + depth)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    draw_cube()  # draw the updated cube

    pygame.display.flip()   # show the new frame on screen
    pygame.time.wait(15)    # short delay to control speed
