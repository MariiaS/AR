# -*- coding: utf-8 -*-
"""opengl2d.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1s0DLlR7aug7I4KgbuGxvObznLF6fYG2F

Import libraries
"""

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np
import sys
import time

"""Initializing settings"""

# Some api in the chain is translating the keystrokes to this binary string
# so instead of saying: ESCAPE = 27, we use the following.
ESCAPE = b'\x1b'

# Number of the glut window.
window = 0

def init():
    # Commands # 1
    glEnable(GL_POINT_SMOOTH) # 1.1
    glEnable(GL_LINE_SMOOTH)  # 1.2
    glEnable(GL_BLEND)        # 1.3
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA) # 1.4
    # Commands # 2
    glClearColor(1.0, 1.0, 1.0, 1.0) # 2.1
    gluOrtho2D(-5.0, 5.0, -5.0, 5.0) # 2.2

"""Function to be plotted"""

def func_x2(input_vec):
    vertices = [[x, x*x] for x in input_vec]
    return np.array(vertices)

def func_sine(input_vec):
    vertices = [[x, np.sin(x)] for x in input_vec]
    return np.array(vertices)

def func_rand_normal(input_vec):
    vertices = [[x, np.random.normal(loc=0, scale=0.1)] for x in input_vec]
    return np.array(vertices)

"""Plotting function in OpenGL"""

def plot_func():
    
    # Commands # 3
    glClear(GL_COLOR_BUFFER_BIT) # 3.1
    glColor3f(0.0, 0.0, 0.0)     # 3.2
    glPointSize(3.0)             # 3.3
    glLineWidth(1.0)             # 3.4
    
    # Commands # 4
    glBegin(GL_LINES)
    glVertex2f(-5.0, 0.0)
    glVertex2f(5.0, 0.0)
    glVertex2f(0.0, 5.0)
    glVertex2f(0.0, -5.0)
    for i in range(-5, 6):
        glVertex2f(-5.0, i)
        glVertex2f(5.0, i)
    for i in range(-5, 6):
        glVertex2f(i, -5.0)
        glVertex2f(i, 5.0)
    glEnd()

    # Set points to plot graphic
    vertices=func_x2(np.linspace(-5.0,5.0,101))
    vertices_sine = func_sine(np.linspace(-5.0, 5.0, 101))
    vertices_norm=func_rand_normal(np.linspace(-5.0,5.0,101))
    
    # Commands # 5
    for i in range(len(vertices)-1):
        glBegin(GL_LINES)
        glColor3f(0.8,0.2,0.2)
        glVertex2f(vertices[i,0],vertices[i,1])
        glVertex2f(vertices[i+1,0],vertices[i+1,1])
        glVertex2f(vertices_sine[i, 0], vertices_sine[i, 1])
        glVertex2f(vertices_sine[i + 1, 0], vertices_sine[i + 1, 1])
        glVertex2f(vertices_norm[i, 0], vertices_norm[i, 1])
        glVertex2f(vertices_norm[i + 1, 0], vertices_norm[i + 1, 1])
        glEnd()
    
    # Commands # 6
    for i in range(len(vertices)):
        glBegin(GL_POINTS)
        glColor3f(0.1,0.5,0.1)
        glVertex2f(vertices[i,0],vertices[i,1])
        glVertex2f(vertices_sine[i, 0], vertices_sine[i, 1])
        glVertex2f(vertices_norm[i, 0], vertices_norm[i, 1])
        glEnd()
    
    # Commands # 7
    # time.sleep(...)
    glutSwapBuffers()

"""Function that checks if a key has been pressed on the keyboard"""

# The function called whenever a key is pressed. Note the use of Python tuples to pass in: (key, x, y)  
def keyPressed(*args):
    print(args[0])
    # If escape is pressed, kill everything.
    if args[0]==ESCAPE:
        glutDestroyWindow(window)
        sys.exit(0)

"""Main function with initialization, drawing and querying for external inputs (keyboard)"""

def main():
    global window
    glutInit(())
    glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
    glutInitWindowPosition(50,50)
    glutInitWindowSize(500,500)
    glutCreateWindow(b"Function Plotter")
    glutDisplayFunc(plot_func)
    # When we are doing nothing, redraw the scene.
    glutIdleFunc(plot_func)
    # Register the function called when the keyboard is pressed.  
    glutKeyboardFunc(keyPressed)
    # Initialization
    init()
    # Main drawing loop
    glutMainLoop()

"""Executing main function"""

# Print message to console, and kick off the main to get it rolling.
if __name__ == '__main__':
    print("Hit ESC key to quit.")
    main()

