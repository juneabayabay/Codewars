import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

# Initialize pygame
pygame.init()

# Set up display window
display = (800, 600)
pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

# set up window captions
pygame.display.set_caption("03 Lab 1 - [Arjune Abay abay]")

# Viewers perspective
gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
glTranslatef(0, 0, -5)

# define the 8 vertex and value to get the spicific value start start with 0 index
vertices = (
    (1, 1, 1),    
    (1, 1, -1),   
    (1, -1, -1),  
    (1, -1, 1),  
    (-1, 1, 1),  
    (-1, -1, -1), 
    (-1, -1, 1), 
    (-1, 1, -1) 
)

# Define the 12 edges 

edges = (
    (0, 1), 
    (1, 2),
    (2, 3),
    (3, 0), 
    (4, 7),
    (7, 5),
    (5, 6),
    (6, 4),
    (3, 6),
    (0, 4),
    (2, 5),
    (1, 7)
)

# Function to draw the wireframe cube
def draw_cube():
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

# Main event loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

 # Rotate the cube (angle=1, x=1, y=1, z=1) before glClear()
    glRotatef(1, 1, 1, 1)

 # Clear color and depth buffers
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

#  Draw the cube after glClear()
    draw_cube()

# Update display and control frame rate
    pygame.display.flip()
    pygame.time.wait(15)

