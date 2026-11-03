"""
IT2202 - Pre-Finals Performance Task
3D Scene Creation Using Python (Pygame + PyOpenGL)
Floating-island scene (geometric version of the reference image).

Scene graph:
  World
  ├── Sky
  ├── CloudGroup
  ├── MainIsland
  │   ├── HangingRock (cone), Cliff (cylinder), GrassTop (cube)
  │   ├── PeakHouse / MidHouse / Shed   (cube + cone)
  │   ├── Chimney (cylinder)
  │   ├── Stairs (cubes)
  │   └── Trees (cylinder + sphere)
  ├── WaterRing (torus) + LowerGrass (disk ring)
  └── FarIsland

Controls:
  LEFT / RIGHT  orbit camera around the island
  UP / DOWN     tilt camera
  S             save screenshot (scene.png)
"""

import math

import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *


pygame.init()

display = (1000, 700)
pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
pygame.display.set_caption("Pre-Finals 3D Scene - Arjune Abayabay")


glEnable(GL_DEPTH_TEST)
glEnable(GL_NORMALIZE)
glEnable(GL_LIGHTING)
glEnable(GL_LIGHT0)
glEnable(GL_LIGHT1)
glEnable(GL_COLOR_MATERIAL)
glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)
glLightModelfv(GL_LIGHT_MODEL_AMBIENT, (0.36, 0.38, 0.44, 1.0))
glClearColor(0.22, 0.58, 0.92, 1)
glShadeModel(GL_SMOOTH)

quad = gluNewQuadric()
gluQuadricNormals(quad, GLU_SMOOTH)

# Start similar to the photo: above-front, whole island in frame
cam_yaw = 22.0
cam_pitch = 34.0
cam_dist = 24.0


def apply_viewpoint():
    pitch = max(4.0, min(85.0, cam_pitch))
    yaw_r = math.radians(cam_yaw)
    pitch_r = math.radians(pitch)

    eye_x = cam_dist * math.cos(pitch_r) * math.sin(yaw_r)
    eye_y = cam_dist * math.sin(pitch_r)
    eye_z = cam_dist * math.cos(pitch_r) * math.cos(yaw_r)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(40, display[0] / display[1], 0.1, 160.0)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(eye_x, eye_y, eye_z, 0.0, 2.2, 0.0, 0, 1, 0)


def apply_lights():
    glLightfv(GL_LIGHT0, GL_POSITION, (10, 18, 8, 1))
    glLightfv(GL_LIGHT0, GL_DIFFUSE, (0.95, 0.92, 0.85, 1))
    glLightfv(GL_LIGHT0, GL_AMBIENT, (0.22, 0.24, 0.28, 1))
    glLightfv(GL_LIGHT0, GL_SPECULAR, (0.20, 0.20, 0.22, 1))

    glLightfv(GL_LIGHT1, GL_POSITION, (-12, 6, -6, 1))
    glLightfv(GL_LIGHT1, GL_DIFFUSE, (0.30, 0.38, 0.55, 1))
    glLightfv(GL_LIGHT1, GL_AMBIENT, (0.10, 0.12, 0.16, 1))


def draw_cube():
    vertices = (
        (1, 1, 1), (1, 1, -1), (1, -1, -1), (1, -1, 1),
        (-1, 1, 1), (-1, -1, -1), (-1, -1, 1), (-1, 1, -1),
    )
    triangles = (
        (0, 1, 2), (0, 2, 3),
        (4, 6, 5), (4, 5, 7),
        (0, 4, 7), (0, 7, 1),
        (3, 2, 5), (3, 5, 6),
        (0, 3, 6), (0, 6, 4),
        (1, 7, 5), (1, 5, 2),
    )
    normals = (
        (1, 0, 0), (-1, 0, 0), (0, 1, 0),
        (0, -1, 0), (0, 0, 1), (0, 0, -1),
    )
    glBegin(GL_TRIANGLES)
    for i, triangle in enumerate(triangles):
        glNormal3f(*normals[i // 2])
        for vertex in triangle:
            glVertex3fv(vertices[vertex])
    glEnd()


def draw_sphere():
    gluSphere(quad, 1, 24, 18)


def draw_sky():
    glDisable(GL_LIGHTING)
    glCullFace(GL_FRONT)
    glEnable(GL_CULL_FACE)
    gluSphere(quad, 1, 32, 18)
    glDisable(GL_CULL_FACE)
    glCullFace(GL_BACK)
    glEnable(GL_LIGHTING)


def draw_cylinder():
    glPushMatrix()
    glRotatef(-90, 1, 0, 0)
    gluCylinder(quad, 0.4, 0.4, 1.5, 28, 4)
    gluDisk(quad, 0, 0.4, 28, 1)
    glTranslatef(0, 0, 1.5)
    gluDisk(quad, 0, 0.4, 28, 1)
    glPopMatrix()


def draw_cone():
    glPushMatrix()
    glRotatef(-90, 1, 0, 0)
    gluCylinder(quad, 0.55, 0.0, 1.3, 28, 4)
    gluDisk(quad, 0, 0.55, 28, 1)
    glPopMatrix()


def draw_torus(major=1.0, minor=0.22, rings=36, sides=16):
    for i in range(rings):
        glBegin(GL_QUAD_STRIP)
        for j in range(sides + 1):
            for k in (i, i + 1):
                theta = 2 * math.pi * k / rings
                phi = 2 * math.pi * j / sides
                cos_t, sin_t = math.cos(theta), math.sin(theta)
                cos_p, sin_p = math.cos(phi), math.sin(phi)
                x = (major + minor * cos_p) * cos_t
                y = minor * sin_p
                z = (major + minor * cos_p) * sin_t
                glNormal3f(cos_p * cos_t, sin_p, cos_p * sin_t)
                glVertex3f(x, y, z)
        glEnd()


def draw_disk():
    """Unit disk in the XZ plane (used for grass rings)."""
    glPushMatrix()
    glRotatef(-90, 1, 0, 0)
    gluDisk(quad, 0.0, 1.0, 40, 1)
    glPopMatrix()


def draw_ring():
    """Annulus in the XZ plane: inner 0.70, outer 1.0."""
    glPushMatrix()
    glRotatef(-90, 1, 0, 0)
    gluDisk(quad, 0.70, 1.0, 48, 1)
    glPopMatrix()


# ============================================================
# 4. SCENE GRAPH FRAMEWORK
# ============================================================

class Node:
    """Parent-child node. Children inherit location, rotation, and scale."""

    def __init__(
        self,
        name,
        draw_fn=None,
        pos=(0, 0, 0),
        rot=(0, 0, 1, 0),
        scale=(1, 1, 1),
        color=(1, 1, 1),
        lit=True,
    ):
        self.name = name
        self.draw_fn = draw_fn
        self.pos = pos
        self.rot = rot
        self.scale = scale
        self.color = color
        self.lit = lit
        self.children = []

    def add(self, child):
        self.children.append(child)
        return child

    def draw(self):
        glPushMatrix()
        glTranslatef(*self.pos)
        glRotatef(*self.rot)
        glScalef(*self.scale)
        if self.draw_fn:
            if not self.lit:
                glDisable(GL_LIGHTING)
            glColor3f(*self.color)
            self.draw_fn()
            if not self.lit:
                glEnable(GL_LIGHTING)
        for child in self.children:
            child.draw()
        glPopMatrix()


# ============================================================
# 5. BUILD THE FLOATING ISLAND
# ============================================================

ROCK = (0.34, 0.34, 0.36)
GRASS = (0.32, 0.66, 0.30)
WATER = (0.20, 0.80, 0.90)
WOOD = (0.70, 0.48, 0.28)
CREAM = (0.93, 0.88, 0.80)
ROOF = (0.62, 0.34, 0.20)
TRUNK = (0.40, 0.26, 0.16)
LEAF = (0.20, 0.50, 0.22)


def make_house(name, pos, rot=0, size=1.0, roof=ROOF, body=CREAM):
    house = Node(name, pos=pos, rot=(rot, 0, 1, 0), scale=(size, size, size))
    house.add(Node("Body", draw_fn=draw_cube, pos=(0, 0.55, 0),
                   scale=(0.85, 0.50, 0.65), color=body))
    house.add(Node("Roof", draw_fn=draw_cone, pos=(0, 1.02, 0),
                   scale=(1.15, 0.52, 1.05), color=roof))
    return house


def make_tree(name, pos, size=1.0):
    tree = Node(name, pos=pos, scale=(size, size, size))
    tree.add(Node("Trunk", draw_fn=draw_cylinder, pos=(0, 0, 0),
                  scale=(0.10, 0.65, 0.10), color=TRUNK))
    tree.add(Node("Canopy", draw_fn=draw_sphere, pos=(0, 1.25, 0),
                  scale=(0.52, 0.46, 0.52), color=LEAF))
    return tree


world = Node("World")

world.add(Node("Sky", draw_fn=draw_sky, scale=(70, 70, 70),
               color=(0.28, 0.62, 0.94), lit=False))

# --- clouds ---
clouds = world.add(Node("CloudGroup", pos=(0, 6.0, 0)))
c1 = clouds.add(Node("Cloud1", pos=(-8.5, 2.5, -6.0)))
c1.add(Node("PuffA", draw_fn=draw_sphere, scale=(1.6, 0.70, 1.1), color=(1, 1, 1)))
c1.add(Node("PuffB", draw_fn=draw_sphere, pos=(1.3, 0.15, 0.2),
            scale=(1.1, 0.55, 0.85), color=(0.96, 0.97, 1.0)))
c2 = clouds.add(Node("Cloud2", pos=(9.0, 1.8, -4.0)))
c2.add(Node("PuffA", draw_fn=draw_sphere, scale=(1.3, 0.60, 0.95), color=(1, 1, 1)))
c2.add(Node("PuffB", draw_fn=draw_sphere, pos=(1.0, 0.1, 0.15),
            scale=(0.85, 0.45, 0.70), color=(0.96, 0.97, 1.0)))
c3 = clouds.add(Node("Cloud3", pos=(2.0, -8.5, 6.0)))
c3.add(Node("PuffA", draw_fn=draw_sphere, scale=(1.8, 0.75, 1.2), color=(1, 1, 1)))

# --- main floating island (parent: move this, everything on it follows) ---
island = world.add(Node("MainIsland", pos=(0, 0.4, 0)))

# Dark hanging rock (upside-down cone) + cliff shaft
island.add(Node("HangingRock", draw_fn=draw_cone,
                pos=(0, 1.0, 0), rot=(180, 1, 0, 0),
                scale=(5.5, 5.0, 5.5), color=ROCK))
island.add(Node("Cliff", draw_fn=draw_cylinder,
                pos=(0, 1.0, 0),
                scale=(5.2, 2.15, 5.2), color=ROCK))
island.add(Node("GrassTop", draw_fn=draw_disk,
                pos=(0, 4.28, 0),
                scale=(2.55, 1.0, 2.55), color=GRASS))

# Houses on the plateau
island.add(make_house("PeakHouse", pos=(0.15, 4.28, -1.35), rot=18, size=0.68,
                      roof=(0.48, 0.30, 0.22)))
island.add(make_house("MidHouse", pos=(-0.55, 4.28, 0.45), rot=-12, size=0.95,
                      roof=ROOF))
shed = island.add(Node("Shed", pos=(1.45, 4.28, 0.95), rot=(25, 0, 1, 0)))
shed.add(Node("Body", draw_fn=draw_cube, pos=(0, 0.16, 0),
              scale=(0.32, 0.14, 0.20), color=(0.72, 0.50, 0.32)))

island.add(Node("Chimney", draw_fn=draw_cylinder,
                pos=(-1.25, 4.28, -0.20),
                scale=(0.14, 0.70, 0.14), color=(0.35, 0.32, 0.30)))

# Wooden stairs down the cliff toward the water
stairs = island.add(Node("Stairs", pos=(0.20, 4.22, 1.70)))
for i in range(12):
    t = i / 11.0
    stairs.add(Node(
        f"Step{i}",
        draw_fn=draw_cube,
        pos=(0.04 * i, -2.55 * t, 1.35 * t),
        scale=(0.28, 0.04, 0.20),
        color=WOOD,
    ))

# Trees on the top plateau
for name, pos, size in (
    ("TopTree1", (-1.6, 4.28, -1.35), 0.62),
    ("TopTree2", (1.55, 4.28, -1.20), 0.52),
    ("TopTree3", (1.85, 4.28, 0.20), 0.46),
    ("TopTree4", (-1.80, 4.28, 0.85), 0.55),
    ("TopTree5", (0.85, 4.28, 1.55), 0.44),
):
    island.add(make_tree(name, pos, size))

# Cyan water moat sitting on a wider grass terrace
world.add(Node("LowerGrass", draw_fn=draw_disk,
               pos=(0, 1.00, 0),
               scale=(5.10, 1.0, 5.10), color=GRASS))
world.add(Node("WaterRing", draw_fn=draw_ring,
               pos=(0, 1.08, 0),
               scale=(4.35, 1.0, 4.35), color=WATER))

# Trees on the lower ring
ring = world.add(Node("LowerTrees", pos=(0, 1.05, 0)))
for i, size in enumerate((0.70, 0.55, 0.62, 0.48, 0.58, 0.50)):
    angle = math.radians(i * 60 + 15)
    x = 4.35 * math.cos(angle)
    z = 4.35 * math.sin(angle)
    ring.add(make_tree(f"RingTree{i}", (x, 0, z), size))

# Tiny distant island (same hierarchy, scaled down)
far = world.add(Node("FarIsland", pos=(11.5, 7.2, -16.0), scale=(0.28, 0.28, 0.28)))
far.add(Node("Rock", draw_fn=draw_cone, pos=(0, 0, 0), rot=(180, 1, 0, 0),
             scale=(4.5, 3.5, 4.5), color=ROCK))
far.add(Node("Grass", draw_fn=draw_cube, pos=(0, 0.2, 0),
             scale=(2.2, 0.12, 2.2), color=GRASS))
far.add(make_tree("FarTree", (0.4, 0.3, 0.2), 1.1))


def save_screenshot(filename="scene.png"):
    glReadBuffer(GL_BACK)
    data = glReadPixels(0, 0, display[0], display[1], GL_RGB, GL_UNSIGNED_BYTE)
    surface = pygame.image.frombytes(data, display, "RGB")
    surface = pygame.transform.flip(surface, False, True)
    pygame.image.save(surface, filename)
    print("Saved", filename, flush=True)


# ============================================================
# 7. MAIN LOOP  — arrow keys turn the camera
# ============================================================

first_frame = True
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
            save_screenshot("scene.png")

    keys = pygame.key.get_pressed()
    if keys[K_LEFT]:
        cam_yaw -= 1.6
    if keys[K_RIGHT]:
        cam_yaw += 1.6
    if keys[K_UP]:
        cam_pitch += 1.1
    if keys[K_DOWN]:
        cam_pitch -= 1.1

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    apply_viewpoint()
    apply_lights()
    world.draw()
    if first_frame:
        save_screenshot("scene.png")
        first_frame = False
    pygame.display.flip()
    clock.tick(60)
