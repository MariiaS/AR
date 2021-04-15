# -*- coding: utf-8 -*-


import sys

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

# Some api in the chain is translating the keystrokes to this binary string
# so instead of saying: ESCAPE = 27, we use the following.
ESCAPE = b'\x1b'

# Number of the glut window.
window = 0

# Rotations of arm parts and part_6 opening
part_2 = 90.0
part_4 = 0.0
part_5 = 0.0
part_6 = 0.3
fingers = 0.0
long = 2.0


# Main function
def main():
    global window

    # GLUT initialization
    glutInit(())

    # GLUT display mode
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)

    # Initial window size
    glutInitWindowSize(500, 500)

    # Initial window position
    glutInitWindowPosition(100, 100)

    # Window creation
    glutCreateWindow(b"Robot arm")

    # Initial colour and shading model
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glClearDepth(1.0)  # Enables Clearing Of The Depth Buffer
    glDepthFunc(GL_LESS)  # The Type Of Depth Test To Do
    glEnable(GL_DEPTH_TEST)  # Enables Depth Testing
    glShadeModel(GL_FLAT)  # Flat shading model

    # Pass drawing function to glut
    glutDisplayFunc(draw)

    # When we are doing nothing, redraw the scene.
    glutIdleFunc(draw)

    # Register the function called when our window is resized.
    glutReshapeFunc(reshape)

    # Register the function called when the keyboard is pressed.
    glutKeyboardFunc(keys)

    # Start Event Processing Engine
    glutMainLoop()


# Draw robot arm parts
def draw():
    global part_2, part_4, part_5, part_6, long

    # Initial position
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glPushMatrix()
    glTranslatef(0.0, -3.0, -7.0)

    # Part 1- BASE
    glColor3f(0.5, 0.5, 0.8)
    glPushMatrix()
    glScalef(4.0, 0.2, 4)
    glutWireCube(1.0)
    glPopMatrix()

    # Part 2 - LOWER ARM
    glColor3f(0.5, 0.8, 0.5)
    glRotatef(part_2, 0.0, 0.0, 1.0)
    glTranslatef(1.0, 0.0, 0.0)
    glPushMatrix()
    glScalef(2.0, 1.3, 0.5)
    glutWireCube(1.0)
    glPopMatrix()

    # Part # 4 - UPPER ARM
    glColor3f(0.8, 0.8, 0.5)
    glTranslatef(1.0, 0.0, 0.0);
    glRotatef(part_4, 0.0, 1.0, 1.0);
    glTranslatef(long * 0.50, 0.0, 0.0);
    glPushMatrix();
    glScalef(long, 1.3, 0.5)
    glutWireCube(1.0)
    glPopMatrix()

    # Part # 5 - HAND
    glColor3f(0.5, 0.5, 0.8)
    glTranslatef(long * 0.50, 0.0, 0.0);
    glRotatef(part_5, 0.0, 0.0, 0.0)
    glTranslatef(1.2, 0.0, 0.0)
    glPushMatrix()
    glScalef(2.3, 2.5, 0.8)
    glutWireCube(1.0)
    glPopMatrix()

    # Part 6 - FINGERS
    glColor3f(0.8, 0.5, 0.5)

    glTranslatef(0.8, 0.6, 0.0)

    glTranslatef(0.0, part_6, 0.0)
    glTranslatef(1.0, 0.0, 0.0)
    glRotatef(fingers, 0.0, 1.0, 0.0)
    glPushMatrix()
    glScalef(1.2, 0.2, 0.2)
    glutWireCube(1.0)
    glPopMatrix()

    glTranslatef(0.0, -2 * part_6, 0.0)
    glTranslatef(0.0, 0.0, 0.0)
    glPushMatrix()
    glScalef(1.2, 0.2, 0.2)
    glutWireCube(1.0)
    glPopMatrix()

    glTranslatef(0.0, -2 * part_6, 0.0)
    glTranslatef(0.0, 0.0, 0.0)
    glPushMatrix()
    glScalef(1.2, 0.2, 0.2)
    glutWireCube(1.0)
    glPopMatrix()

    glTranslatef(0.0, -2 * part_6, 0.0)
    glTranslatef(0.0, 0.0, 0.0)
    glPushMatrix()
    glScalef(1.2, 0.2, 0.2)
    glutWireCube(1.0)
    glPopMatrix()

    glTranslatef(0.0, -2 * part_6, 0.0)
    glTranslatef(-0.8, -0.1, 0.0)
    glRotatef(45, 0.0, 0.0, -0.3)
    glPushMatrix()
    glScalef(1.0, 0.2, 0.2)
    glutWireCube(1.0)
    glPopMatrix()
    # Part 6 - UPPER FINGERS
    glColor3f(0.8, 0.5, 0.1)

    glRotatef(-45, 0.0, 0.0, -0.3)
    glTranslatef(0.8, 2.2, 0.0)

    glTranslatef(0.0, part_6, 0.0)
    glTranslatef(1.1, 0.0, 0.0)
    glRotatef(fingers, 0.0, 1.0, 0.0)
    glPushMatrix()
    glScalef(1.1, 0.2, 0.2)
    glutWireCube(1.0)
    glPopMatrix()

    glTranslatef(0.2, -2 * part_6, 0.0)
    glTranslatef(0.0, 0.0, 0.0)
    glPushMatrix()
    glScalef(1.4, 0.2, 0.2)
    glutWireCube(1.0)
    glPopMatrix()

    glTranslatef(0.1, -2 * part_6, 0.0)
    glTranslatef(0.0, 0.0, 0.0)
    glPushMatrix()
    glScalef(1.7, 0.2, 0.2)
    glutWireCube(1.0)
    glPopMatrix()

    glTranslatef(-0.1, -2 * part_6, 0.0)
    glTranslatef(0.0, 0.0, 0.0)
    glPushMatrix()
    glScalef(1.5, 0.2, 0.2)
    glutWireCube(1.0)
    glPopMatrix()

    glTranslatef(-1.4, -2 * part_6, 0.0)
    glTranslatef(0.0, -0.8, 0.0)
    glRotatef(45, 0.0, 0.0, -0.3)
    glTranslatef(0.0, 0.0, 0.0)
    #glRotatef(fingers, 0.0, 1.0, 0.0)
    glPushMatrix()
    glScalef(0.9, 0.2, 0.2)
    glutWireCube(1.0)
    glPopMatrix()


    glPopMatrix()
    glutSwapBuffers()


# Recalculate projection matrix if window size is modified
def reshape(w, h):
    glViewport(0, 0, w, h)  # Reset The Current Viewport And Perspective Transformation
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(65.0, float(w) / float(h), 1.0, 20.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glTranslatef(0.0, 0.0, -6.0)


# This function reads the keyboard to move the part_4 accordingly
def keys(*args):
    global part_2, part_4, part_5, part_6, fingers, long
    key = args[0]
    if (key == b's'):
        long = (long + 0.05)
    elif (key == b'S'):
        long = (long - 0.05)
    elif (key == b'e'):
        part_2 = (part_2 + 5.0) % 360.0
    elif (key == b'E'):
        part_2 = (part_2 - 5.0) % 360.0
    elif (key == b'w'):
        part_4 = (part_4 + 5.0) % 360.0
    elif (key == b'W'):
        part_4 = (part_4 - 5.0) % 360.0
    elif (key == b'r'):  # The part below to rotate hand up to 90 degrees around Y axes from left to right and back with r and R keys
        if part_5 < 90.0:
            part_5 = (part_5 + 5.0) % 360.0
    elif (key == b'R'):
        if part_5 > 0.0:
            part_5 = (part_5 - 5.0) % 360.0
    elif (key == b'd'):  # The part below to move fingers with keys d and D
        if fingers < 45:
            fingers = (fingers + 5.0) % 360.0
    elif (key == b'D'):
        if fingers > 0.0:
            fingers = (fingers - 5.0) % 360.0
    elif (key == ESCAPE):
        glutDestroyWindow(window)
        sys.exit(0)


# Print message to console, and kick off the main to get it rolling.
if __name__ == '__main__':
    print("Hit ESC key to quit.")
    main()
