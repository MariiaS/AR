# -*- coding: utf-8 -*-
"""opengl3d.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1tcQx3wx5aLDity09nFm4431Wk9u9ywvL

## Cell # 1
"""

# Some api in the chain is translating the keystrokes to this binary string
# so instead of saying: ESCAPE = 27, we use the following.
ESCAPE = b'\x1b'

# Number of the glut window.
window = 0

# A general OpenGL initialization function.  Sets all of the initial parameters.
def InitGL(Width, Height):# We call this right after our OpenGL window is created.
    glClearColor(0.0, 0.0, 0.0, 0.0)# This Will Clear The Background Color To Black
    glClearDepth(1.0)# Enables Clearing Of The Depth Buffer
    glDepthFunc(GL_LESS)# The Type Of Depth Test To Do
    glEnable(GL_DEPTH_TEST)# Enables Depth Testing
    glShadeModel(GL_SMOOTH)# Enables Smooth Color Shading

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()# Reset The Projection Matrix
    # Calculate The Aspect Ratio Of The Window
    gluPerspective(45.0, float(Width)/float(Height), 0.1, 100.0)

    glMatrixMode(GL_MODELVIEW)

# The function called when our window is resized (which shouldn't happen if you enable fullscreen, below)
def ReSizeGLScene(Width, Height):
    if Height == 0:# Prevent A Divide By Zero If The Window Is Too Small
        Height = 1

    glViewport(0, 0, Width, Height) # Reset The Current Viewport And Perspective Transformation
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, float(Width)/float(Height), 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)

# The main drawing function.
def DrawGLScene():
    # Clear The Screen And The Depth Buffer
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()# Reset The View

    # Move Left 1.5 units and into the screen 6.0 units.
    glTranslatef(-1.5, 0.0, -6.0)

    # Draw a triangle
    glBegin(GL_TRIANGLES)                 # Start drawing a polygon
    glVertex3f(0.0, 1.0, 0.0)           # Top
    glVertex3f(1.0, -1.0, 0.0)          # Bottom Right
    glVertex3f(-1.0, -1.0, 0.0)         # Bottom Left
    glEnd()                             # We are done with the polygon


    # Move Right 3.0 units, Up 1.0 units.
    glTranslatef(3.0, 1.0, 0.0)

    # Draw a square (quadrilateral)
    glBegin(GL_QUADS)                   # Start drawing a 4 sided polygon
    glVertex3f(-1.0, 1.0, 0.0)          # Top Left
    glVertex3f(1.0, 1.0, 0.0)           # Top Right
    glVertex3f(1.0, -1.0, 0.0)          # Bottom Right
    glVertex3f(-1.0, -1.0, 0.0)         # Bottom Left
    glEnd()                             # We are done with the polygon

    #  since this is double buffered, swap the buffers to display what just got drawn.
    glutSwapBuffers()

# The function called whenever a key is pressed. Note the use of Python tuples to pass in: (key, x, y)
def keyPressed(*args):
    print(args[0])
    # If escape is pressed, kill everything.
    if args[0]==ESCAPE:
        glutDestroyWindow(window)
        sys.exit(0)

def main():
    global window
    # For now we just pass glutInit one empty argument. I wasn't sure what should or could be passed in (tuple, list, ...)
    # Once I find out the right stuff based on reading the PyOpenGL source, I'll address this.
    glutInit(())

    # Select type of Display mode:
    #  Double buffer
    #  RGBA color
    # Alpha components supported
    # Depth buffer
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)

    # get a 640 x 480 window
    glutInitWindowSize(640, 480)

    # the window starts at the upper left corner of the screen
    glutInitWindowPosition(0, 0)

    # Window creation
    window = glutCreateWindow(b"Triangle and square")

    # Pass drawing function to glut
    glutDisplayFunc(DrawGLScene)

    # Uncomment this line to get full screen.
    #glutFullScreen()

    # When we are doing nothing, redraw the scene.
    glutIdleFunc(DrawGLScene)

    # Register the function called when our window is resized.
    glutReshapeFunc(ReSizeGLScene)

    # Register the function called when the keyboard is pressed.
    glutKeyboardFunc(keyPressed)

    # Initialize our window.
    InitGL(640, 480)

    # Start Event Processing Engine
    glutMainLoop()

# Print message to console, and kick off the main to get it rolling.
print("Hit ESC key to quit.")
main()

"""## Cell # 2"""

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Some api in the chain is translating the keystrokes to a binary string
# so instead of saying: ESCAPE = 27, we use the following.
ESCAPE = b'\x1b'

# Number of the glut window.
window = 0

# A general OpenGL initialization function.  Sets all of the initial parameters.
def InitGL(Width, Height):              # We call this right after our OpenGL window is created.
    glClearColor(0.0, 0.0, 0.0, 0.0)    # This Will Clear The Background Color To Black
    glClearDepth(1.0)                   # Enables Clearing Of The Depth Buffer
    glDepthFunc(GL_LESS)                # The Type Of Depth Test To Do
    glEnable(GL_DEPTH_TEST)             # Enables Depth Testing
    glShadeModel(GL_SMOOTH)             # Enables Smooth Color Shading

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()                    # Reset The Projection Matrix
                                        # Calculate The Aspect Ratio Of The Window
    gluPerspective(45.0, float(Width)/float(Height), 0.1, 100.0)

    glMatrixMode(GL_MODELVIEW)

# The function called when our window is resized (which shouldn't happen if you enable fullscreen, below)
def ReSizeGLScene(Width, Height):
    if Height == 0:# Prevent A Divide By Zero If The Window Is Too Small
        Height = 1

    glViewport(0, 0, Width, Height)    # Reset The Current Viewport And Perspective Transformation
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, float(Width)/float(Height), 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)

# The main drawing function.
def DrawGLScene():
    # Clear The Screen And The Depth Buffer
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()# Reset The View

    # Move Left 1.5 units and into the screen 6.0 units.
    glTranslatef(-1.5, 0.0, -6.0)

    # Draw a triangle
    glBegin(GL_POLYGON)                 # Start drawing a polygon
    glColor3f(1.0, 0.0, 0.0)            # Red
    glVertex3f(0.0, 1.0, 0.0)           # Top
    glColor3f(0.0, 1.0, 0.0)            # Green
    glVertex3f(1.0, -1.0, 0.0)          # Bottom Right
    glColor3f(0.0, 0.0, 1.0)            # Blue
    glVertex3f(-1.0, -1.0, 0.0)         # Bottom Left
    glEnd()                             # We are done with the polygon


    # Move Right 3.0 units.
    glTranslatef(3.0, 0.0, 0.0)

    # Draw a square (quadrilateral)
    glColor3f(0.3, 0.5, 1.0)            # Bluish shade
    glBegin(GL_QUADS)                   # Start drawing a 4 sided polygon
    glVertex3f(-1.0, 1.0, 0.0)          # Top Left
    glVertex3f(1.0, 1.0, 0.0)           # Top Right
    glVertex3f(1.0, -1.0, 0.0)          # Bottom Right
    glVertex3f(-1.0, -1.0, 0.0)         # Bottom Left
    glEnd()                             # We are done with the polygon

    #  since this is double buffered, swap the buffers to display what just got drawn.
    glutSwapBuffers()

# The function called whenever a key is pressed. Note the use of Python tuples to pass in: (key, x, y)
def keyPressed(*args):
    print(args[0])
    # If escape is pressed, kill everything.
    if args[0]==ESCAPE:
        glutDestroyWindow(window)
        sys.exit(0)

def main():
    global window

    # glut initialization
    glutInit("")

    # Select type of Display mode:
    #  Double buffer
    #  RGBA color
    # Alpha components supported
    # Depth buffer
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)

    # get a 640 x 480 window
    glutInitWindowSize(640, 480)

    # the window starts at the upper left corner of the screen
    glutInitWindowPosition(0, 0)

    # Window creation
    window = glutCreateWindow(b"Colored triangle and square")

    # Pass drawing function to glut
    glutDisplayFunc(DrawGLScene)

    # Uncomment this line to get full screen.
    #glutFullScreen()

    # When we are doing nothing, redraw the scene.
    glutIdleFunc(DrawGLScene)

    # Register the function called when our window is resized.
    glutReshapeFunc(ReSizeGLScene)

    # Register the function called when the keyboard is pressed.
    glutKeyboardFunc(keyPressed)

    # Initialize our window.
    InitGL(640, 480)

    # Start Event Processing Engine
    glutMainLoop()

# Print message to console, and kick off the main to get it rolling.
print("Hit ESC key to quit.")
main()

"""## Cell # 3"""

# Some api in the chain is translating the keystrokes to this binary string
# so instead of saying: ESCAPE = 27, we use the following.
ESCAPE = b'\x1b'

# Number of the glut window.
window = 0

# ?????????????
rtri = 0.0

# ?????????????
rquad = 0.0

# A general OpenGL initialization function.  Sets all of the initial parameters.
def InitGL(Width, Height):              # We call this right after our OpenGL window is created.
    glClearColor(0.0, 0.0, 0.0, 0.0)    # This Will Clear The Background Color To Black
    glClearDepth(1.0)                   # Enables Clearing Of The Depth Buffer
    glDepthFunc(GL_LESS)                # The Type Of Depth Test To Do
    glEnable(GL_DEPTH_TEST)             # Enables Depth Testing
    glShadeModel(GL_SMOOTH)             # Enables Smooth Color Shading

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()                    # Reset The Projection Matrix
                                        # Calculate The Aspect Ratio Of The Window
    gluPerspective(45.0, float(Width)/float(Height), 0.1, 100.0)

    glMatrixMode(GL_MODELVIEW)

# The function called when our window is resized (which shouldn't happen if you enable fullscreen, below)
def ReSizeGLScene(Width, Height):
    if Height == 0:                     # Prevent A Divide By Zero If The Window Is Too Small
        Height = 1

    glViewport(0, 0, Width, Height)     # Reset The Current Viewport And Perspective Transformation
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, float(Width)/float(Height), 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)

# The main drawing function.
def DrawGLScene():
    global rtri, rquad

    # Clear The Screen And The Depth Buffer
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()                   # Reset The View

    # Move Left 1.5 units and into the screen 6.0 units.
    glTranslatef(-1.5, 0.0, -6.0)

    # We have smooth color mode on, this will blend across the vertices.
    # Draw a triangle rotated on the Y axis.
    glRotatef(rtri, 0.0, 1.0, 0.0)      # Rotate
    glBegin(GL_POLYGON)                 # Start drawing a polygon
    glColor3f(1.0, 0.0, 0.0)            # Red
    glVertex3f(0.0, 1.0, 0.0)           # Top
    glColor3f(0.0, 1.0, 0.0)            # Green
    glVertex3f(1.0, -1.0, 0.0)          # Bottom Right
    glColor3f(0.0, 0.0, 1.0)            # Blue
    glVertex3f(-1.0, -1.0, 0.0)         # Bottom Left
    glEnd()                             # We are done with the polygon

    # We are "undoing" the rotation so that we may rotate the quad on its own axis.
    # We also "undo" the prior translate.  This could also have been done using the
    # matrix stack.
    glLoadIdentity()

    # Move Right 1.5 units and into the screen 6.0 units.
    glTranslatef(1.5, 0.0, -6.0)

    # Draw a square (quadrilateral) rotated on the X axis.
    glRotatef(rquad, 3.0, 0.0, 0.0)     # Rotate
    glColor3f(0.3, 0.5, 1.0)            # Bluish shade
    glBegin(GL_QUADS)                   # Start drawing a 4 sided polygon
    glVertex3f(-1.0, 1.0, 0.0)          # Top Left
    glVertex3f(1.0, 1.0, 0.0)           # Top Right
    glVertex3f(1.0, -1.0, 0.0)          # Bottom Right
    glVertex3f(-1.0, -1.0, 0.0)         # Bottom Left
    glEnd()                             # We are done with the polygon

    # What values to use?  Well, if you have a FAST machine and a FAST 3D Card, then
    # large values make an unpleasant display with flickering and tearing.  I found that
    # smaller values work better, but this was based on my experience.
    rtri  = rtri + 0.5                  # ?????????????
    rquad = rquad + 0.1                 # ?????????????


    #  since this is double buffered, swap the buffers to display what just got drawn.
    glutSwapBuffers()

# The function called whenever a key is pressed. Note the use of Python tuples to pass in: (key, x, y)
def keyPressed(*args):
    print(args[0])
    # If escape is pressed, kill everything.
    if args[0]==ESCAPE:
        glutDestroyWindow(window)
        sys.exit(0)

def main():
    global window
    # glut initialization
    glutInit("")

    # Select type of Display mode:
    #  Double buffer
    #  RGBA color
    # Alpha components supported
    # Depth buffer
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)

    # get a 640 x 480 window
    glutInitWindowSize(640, 480)

    # the window starts at the upper left corner of the screen
    glutInitWindowPosition(0, 0)

    # Window creation
    window = glutCreateWindow(b"Triangle and square rotation")

    # Pass drawing function to glut
    glutDisplayFunc(DrawGLScene)

    # Uncomment this line to get full screen.
    # glutFullScreen()

    # When we are doing nothing, redraw the scene.
    glutIdleFunc(DrawGLScene)

    # Register the function called when our window is resized.
    glutReshapeFunc(ReSizeGLScene)

    # Register the function called when the keyboard is pressed.
    glutKeyboardFunc(keyPressed)

    # Initialize our window.
    InitGL(640, 480)

    # Start Event Processing Engine
    glutMainLoop()

# Print message to console, and kick off the main to get it rolling.
print("Hit ESC key to quit.")
main()

"""## Cell # 4"""

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

# Some api in the chain is translating the keystrokes to this binary string
# so instead of saying: ESCAPE = 27, we use the following.
ESCAPE = b'\x1b'

# Number of the glut window.
window = 0

# Rotation angle for the pyramid. 
rtri = 0.0

# Rotation angle for the cube.
rquad = 0.0


# A general OpenGL initialization function.  Sets all of the initial parameters. 
def InitGL(Width, Height):  # We call this right after our OpenGL window is created.
    glClearColor(0.0, 0.0, 0.0, 0.0)  # This will clear the background color to black
    glClearDepth(1.0)  # Enables clearing of the depth buffer
    glDepthFunc(GL_LESS)  # The type Of Depth Test To Do
    glEnable(GL_DEPTH_TEST)  # ?????????????
    glShadeModel(GL_SMOOTH)  # Enables Smooth Color Shading

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()  # Reset The Projection Matrix
    # Calculate The Aspect Ratio Of The Window
    gluPerspective(45.0, float(Width) / float(Height), 0.1, 100.0)

    glMatrixMode(GL_MODELVIEW)


# The function called when our window is resized (which shouldn't happen if you enable fullscreen, below)
def ReSizeGLScene(Width, Height):
    if Height == 0:  # Prevent A Divide By Zero If The Window Is Too Small
        Height = 1

    glViewport(0, 0, Width, Height)  # Reset The Current Viewport And Perspective Transformation
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, float(Width) / float(Height), 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)


# The main drawing function.
import numpy as np


def DrawGLScene():
    global rtri, rquad
    # glMatrixMode(GL_MODELVIEW)
    # glPushMatrix()
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);  # Clear The Screen And The Depth Buffer
    glLoadIdentity()  # Reset The View
    glTranslatef(-1.5, 0.0, -6.0)  # Move Left And Into The Screen
    # glRotatef(rtri,0.0,1.0,0.0)     # ?????????????
    rotationMatrix = np.array(
        [[np.cos(rtri), -np.sin(rtri), 0, 0], [np.sin(rtri), np.cos(rtri), 0, 0], [0.0, 0.0, 1.0, 0.0],
         [0.0, 0.0, 0.0, 1.0]])
    glMultMatrixd(rotationMatrix.transpose())

    glBegin(GL_TRIANGLES)  # Start Drawing The Pyramid

    glColor3f(1.0, 0.0, 0.0)  # Red
    glVertex3f(0.0, 1.0, 0.0)  # Top Of Triangle (Front)
    glColor3f(0.0, 1.0, 0.0)  # Green
    glVertex3f(-1.0, -1.0, 1.0)  # Left Of Triangle (Front)
    glColor3f(0.0, 0.0, 1.0)  # Blue
    glVertex3f(1.0, -1.0, 1.0)

    glColor3f(1.0, 0.0, 0.0)  # Red
    glVertex3f(0.0, 1.0, 0.0)  # Top Of Triangle (Right)
    glColor3f(0.0, 0.0, 1.0)  # Blue
    glVertex3f(1.0, -1.0, 1.0)  # Left Of Triangle (Right)
    glColor3f(0.0, 1.0, 0.0)  # Green
    glVertex3f(1.0, -1.0, -1.0)  # Right

    glColor3f(1.0, 0.0, 0.0)  # Red
    glVertex3f(0.0, 1.0, 0.0)  # Top Of Triangle (Back)
    glColor3f(0.0, 1.0, 0.0)  # Green
    glVertex3f(1.0, -1.0, -1.0)  # Left Of Triangle (Back)
    glColor3f(0.0, 0.0, 1.0)  # Blue
    glVertex3f(-1.0, -1.0, -1.0)  # Right Of

    glColor3f(1.0, 0.0, 0.0)  # Red
    glVertex3f(0.0, 1.0, 0.0)  # Top Of Triangle (Left)
    glColor3f(0.0, 0.0, 1.0)  # Blue
    glVertex3f(-1.0, -1.0, -1.0)  # Left Of Triangle (Left)
    glColor3f(0.0, 1.0, 0.0)  # Green
    glVertex3f(-1.0, -1.0, 1.0)  # Right Of Triangle (Left)
    glEnd()
    # glPopMatrix()

    glLoadIdentity()
    glTranslatef(1.5, 0.0, -7.0)  # Move Right And Into The Screen
    glRotatef(rquad, 1.0, 1.0, 1.0)  # ?????????????
    glBegin(GL_QUADS)  # Start Drawing The Cube

    glColor3f(0.0, 1.0, 0.0)  # Set The Color To Blue
    glVertex3f(1.0, 1.0, -1.0)  # Top Right Of The Quad (Top)
    glVertex3f(-1.0, 1.0, -1.0)  # Top Left Of The Quad (Top)
    glVertex3f(-1.0, 1.0, 1.0)  # Bottom Left Of The Quad (Top)
    glVertex3f(1.0, 1.0, 1.0)  # Bottom Right Of The Quad (Top)

    glColor3f(1.0, 0.5, 0.0)  # Set The Color To Orange
    glVertex3f(1.0, -1.0, 1.0)  # Top Right Of The Quad (Bottom)
    glVertex3f(-1.0, -1.0, 1.0)  # Top Left Of The Quad (Bottom)
    glVertex3f(-1.0, -1.0, -1.0)  # Bottom Left Of The Quad (Bottom)
    glVertex3f(1.0, -1.0, -1.0)  # Bottom Right Of The Quad (Bottom)

    glColor3f(1.0, 0.0, 0.0)  # Set The Color To Red
    glVertex3f(1.0, 1.0, 1.0)  # Top Right Of The Quad (Front)
    glVertex3f(-1.0, 1.0, 1.0)  # Top Left Of The Quad (Front)
    glVertex3f(-1.0, -1.0, 1.0)  # Bottom Left Of The Quad (Front)
    glVertex3f(1.0, -1.0, 1.0)  # Bottom Right Of The Quad (Front)

    glColor3f(1.0, 1.0, 0.0)  # Set The Color To Yellow
    glVertex3f(1.0, -1.0, -1.0)  # Bottom Left Of The Quad (Back)
    glVertex3f(-1.0, -1.0, -1.0)  # Bottom Right Of The Quad (Back)
    glVertex3f(-1.0, 1.0, -1.0)  # Top Right Of The Quad (Back)
    glVertex3f(1.0, 1.0, -1.0)  # Top Left Of The Quad (Back)

    glColor3f(0.0, 0.0, 1.0)  # Set The Color To Blue
    glVertex3f(-1.0, 1.0, 1.0)  # Top Right Of The Quad (Left)
    glVertex3f(-1.0, 1.0, -1.0)  # Top Left Of The Quad (Left)
    glVertex3f(-1.0, -1.0, -1.0)  # Bottom Left Of The Quad (Left)
    glVertex3f(-1.0, -1.0, 1.0)  # Bottom Right Of The Quad (Left)

    glColor3f(1.0, 0.0, 1.0)  # Set The Color To Violet
    glVertex3f(1.0, 1.0, -1.0)  # Top Right Of The Quad (Right)
    glVertex3f(1.0, 1.0, 1.0)  # Top Left Of The Quad (Right)
    glVertex3f(1.0, -1.0, 1.0)  # Bottom Left Of The Quad (Right)
    glVertex3f(1.0, -1.0, -1.0)  # Bottom Right Of The Quad (Right)
    glEnd()  # Done Drawing The Quad

    # What values to use?  Well, if you have a FAST machine and a FAST 3D Card, then
    # large values make an unpleasant display with flickering and tearing.  I found that
    # smaller values work better, but this was based on my experience.
    rtri = rtri + 0.1  # ?????????????
    rquad = rquad - 0.2  # ?????????????

    #  since this is double buffered, swap the buffers to display what just got drawn.
    glutSwapBuffers()


# The function called whenever a key is pressed. Note the use of Python tuples to pass in: (key, x, y)
def keyPressed(*args):
    print(args[0])
    # If escape is pressed, kill everything.
    if args[0] == ESCAPE:
        glutDestroyWindow(window)
        sys.exit(0)


def main():
    global window

    glutInit("")

    # Select type of Display mode:   
    #  Double buffer 
    #  RGBA color
    # Alpha components supported 
    # Depth buffer
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)

    # Get a 640 x 480 window 
    glutInitWindowSize(640, 480)

    # The window starts at the upper left corner of the screen 
    glutInitWindowPosition(0, 0)

    # Window creation
    window = glutCreateWindow(b"Pyramid and cube rotation")

    # Pass drawing function to glut
    glutDisplayFunc(DrawGLScene)
    # glutDisplayFunc()

    # Uncomment this line to get full screen.
    # glutFullScreen()

    # When we are doing nothing, redraw the scene.
    glutIdleFunc(DrawGLScene)

    # Register the function called when our window is resized.
    glutReshapeFunc(ReSizeGLScene)

    # Register the function called when the keyboard is pressed.
    glutKeyboardFunc(keyPressed)

    # Initialize our window. 
    InitGL(640, 480)

    # Start Event Processing Engine
    glutMainLoop()


# Print message to console, and kick off the main to get it rolling.
if __name__ == '__main__':
    print("Hit ESC key to quit.")
    main()
    # glMatrixMult
