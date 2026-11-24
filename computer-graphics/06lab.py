import pygame
from pygame.locals import DOUBLEBUF, OPENGL, QUIT
from OpenGL.GL import *
from OpenGL.GLU import *


def add_texture():
    image = pygame.image.load('texture.png')
    data = pygame.image.tostring(image, 'RGBA')
    texID = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, texID)
    glTexImage2D(
        GL_TEXTURE_2D, 0, GL_RGBA,
        image.get_width(), image.get_height(),
        0, GL_RGBA, GL_UNSIGNED_BYTE, data
    )
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glEnable(GL_TEXTURE_2D)


def draw_square():
    """One face of the cube: two triangles with texture coordinates."""
    glBegin(GL_TRIANGLES)

    # lower-left, lower-right, upper-right
    glTexCoord2f(0, 0)
    glVertex3f(-1, -1, 1)
    glTexCoord2f(1, 0)
    glVertex3f(1, -1, 1)
    glTexCoord2f(1, 1)
    glVertex3f(1, 1, 1)

    # lower-left, upper-right, upper-left
    glTexCoord2f(0, 0)
    glVertex3f(-1, -1, 1)
    glTexCoord2f(1, 1)
    glVertex3f(1, 1, 1)
    glTexCoord2f(0, 1)
    glVertex3f(-1, 1, 1)

    glEnd()


def draw_cube():
    glColor3f(1, 1, 1)

    # 1st — front
    glPushMatrix()
    draw_square()
    glPopMatrix()

    # 2nd — 90 degrees around Y
    glPushMatrix()
    glRotatef(90, 0, 1, 0)
    draw_square()
    glPopMatrix()

    # 3rd — -90 degrees around X
    glPushMatrix()
    glRotatef(-90, 1, 0, 0)
    draw_square()
    glPopMatrix()

    # 4th — 180 degrees around Y
    glPushMatrix()
    glRotatef(180, 0, 1, 0)
    draw_square()
    glPopMatrix()

    # 5th — -90 degrees around Y
    glPushMatrix()
    glRotatef(-90, 0, 1, 0)
    draw_square()
    glPopMatrix()

    # 6th — 90 degrees around X
    glPushMatrix()
    glRotatef(90, 1, 0, 0)
    draw_square()
    glPopMatrix()


def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    pygame.display.set_caption("06 Lab 1")

    glEnable(GL_DEPTH_TEST)
    add_texture()

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, display[0] / display[1], 0.1, 50.0)

    clock = pygame.time.Clock()
    angle = 0.0
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

        glClearColor(0.0, 0.0, 0.0, 1.0)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        glTranslatef(0.0, 0.0, -6.0)
        glRotatef(angle, 1.0, 1.0, 0.0)

        draw_cube()

        pygame.display.flip()
        angle += 0.6
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
