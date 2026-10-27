import pygame
from pygame.locals import DOUBLEBUF, OPENGL, QUIT
from OpenGL.GL import *
from OpenGL.GLU import *

# Draw one cube
def draw_cube():
 vertices = [
 (1, 1, -1),
 (1, -1, -1),
 (-1, -1, -1),
 (-1, 1, -1),
 (1, 1, 1),
 (1, -1, 1),
 (-1, -1, 1),
 (-1, 1, 1)
 ]

 faces = [
 (0, 1, 2, 3),
 (4, 5, 6, 7),
 (0, 1, 5, 4),
 (2, 3, 7, 6),
 (0, 3, 7, 4),
 (1, 2, 6, 5)
 ]

 glBegin(GL_QUADS)

 for face in faces:
 for vertex in face:
 glVertex3fv(vertices[vertex])

 glEnd()

# Draw four cubes using the model matrix stack
def draw_object():
 # Cube 1 - outer dark green
 glPushMatrix()
 glScalef(1.8, 1.8, 1.😎
 glColor3f(0.0, 0.3, 0.0)
 draw_cube()
 glPopMatrix()

 # Cube 2 - medium-dark green
 glPushMatrix()
 glScalef(1.4, 1.4, 1.4)
 glColor3f(0.0, 0.5, 0.0)
 draw_cube()
 glPopMatrix()

 # Cube 3 - medium green
 glPushMatrix()
 glScalef(1.0, 1.0, 1.0)
 glColor3f(0.0, 0.7, 0.0)
 draw_cube()
 glPopMatrix()

 # Cube 4 - bright green
 glPushMatrix()
 glScalef(0.6, 0.6, 0.6)
 glColor3f(0.0, 1.0, 0.0)
 draw_cube()
 glPopMatrix()

# Main program
def main():
 pygame.init()

 display = (800, 600)

 pygame.display.set_mode(
 display,
 DOUBLEBUF | OPENGL
 )

 pygame.display.set_caption("05 Lab 1 - Model Matrix")

 # Set up perspective projection
 glMatrixMode(GL_PROJECTION)
 glLoadIdentity()

 gluPerspective(
 45,
 display[0] / display[1],
 0.1,
 50.0
 )

 # Set up the model view
 glMatrixMode(GL_MODELVIEW)
 glLoadIdentity()
 glTranslatef(0.0, 0.0, -8.0)

 # Allow the nested cube layers to remain visible
 glDisable(GL_DEPTH_TEST)

 clock = pygame.time.Clock()
 angle = 0.0
 running = True

 while running:
 for event in pygame.event.get():
 if event.type == QUIT:
 running = False

 # Clear the black background
 glClearColor(0.0, 0.0, 0.0, 1.0)
 glClear(GL_COLOR_BUFFER_BIT)

 glMatrixMode(GL_MODELVIEW)
 glLoadIdentity()

 glTranslatef(0.0, 0.0, -8.0)

 glRotatef(angle, 1.0, 1.0, 0.0)

 draw_object()

 pygame.display.flip()

 angle += 0.7

 clock.tick(60)

 pygame.quit()

if _name_ == "_main_":
 main()
