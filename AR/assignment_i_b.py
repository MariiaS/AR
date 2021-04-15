# -*- coding: utf-8 -*-
"""Assignment I.B.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1XFyvOGwyScza18WLVww481Kbxh0eZWRZ

Import libraries
"""

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np
import sys
import time
import math
import pylab as pl
# load the dataset
from biosppy import storage

"""Initializing settings"""

# Some api in the chain is translating the keystrokes to this binary string
# so instead of saying: ESCAPE = 27, we use the following.
ESCAPE = b'\x1b'

# Number of the glut window.
window = 0

def init():
    glEnable(GL_POINT_SMOOTH) # 1.1 enable GL to draw points with proper filtering, i.e., draw anti-aliased points, which looks more smooth.
    glEnable(GL_LINE_SMOOTH)  # 1.2 enable GL to draw lines with proper filtering, i.e., draw anti-aliased lines
    glEnable(GL_BLEND)        # 1.3 enable GL to draw piexls using  a function that blends the incoming (source) values with the values that are already in the color buffer (the destination values)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA) # 1.4 glBlendFunc defines the operation of blending
    glClearColor(1.0, 1.0, 1.0, 1.0) # 2.1
    gluOrtho2D(-5.0, 5.0, -5.0, 5.0) # 2.2

"""Function to be plotted

Square grid with inter line space of δx = δy = 1.
"""

def func_square_grid(center, width, radio=1):
    # according to center and width find the bottom left point
    x1 = center[0]-width/2
    y1 = center[1]-width/2
    
    vertices = []
    # calculate the point lie in horizen line
    x_interval = np.arange(x1,x1+width+1/radio,1/radio)
    for i in x_interval:
        vertices.append([i,y1])
        vertices.append([i,y1+width])
        
    # calculate the point lie in vertical line 
    y_interval = np.arange(y1,y1+width+1/radio,1/radio)
    for i in y_interval:
        vertices.append([x1,i])
        vertices.append([x1+width,i])
        
    return np.array(vertices)

"""load dataset"""

def get_singal(T):
    
    signal, mdata = storage.load_txt('ecg.txt')
    Fs = mdata['sampling_rate'] # can found in the beginning of the data file
    #N = len(signal)  # number of samples
    #T = (N - 1) / Fs  # duration 
    
    # set the duration
    Signal_second = signal[0:int(T*Fs+1)]
    N = len(Signal_second)
    ts = np.linspace(0, T, N, endpoint=False)  # relative timestamps
    ts = ts -4 # move to left
    # 2/5 is important to change the y scale
    Signal_second = (Signal_second-2047)*0.01*(2/5) # 2/5 due to the relationship between x-axis and y-axis
    
    vertices = list(zip(ts, Signal_second))
    return np.array(vertices)

"""Plotting function in OpenGL"""

def plot_func():
    
    # Commands # 3
    glClear(GL_COLOR_BUFFER_BIT) # 3.1
    
    glColor3f(0.0, 0.0, 0.0)     # 3.2 set the current color as black
    glPointSize(3.0)             # 3.3 set the point size as 3
    glLineWidth(1.0)             # 3.4 set the line width as 1
    
    
    # Commands # 4 draw the coordinate system
    glBegin(GL_LINES) 
    # delimit the vertices of a primitive or a group of like primitives
    # GL_LINES Treats each pair of vertices as an independent line segment.
    glColor3f(0,0,1)
    
    glVertex2f(-5.0, 0.0) # Specifies a vertex.
    glVertex2f(5.0, 0.0) 
    glVertex2f(0.0, 5.0)
    glVertex2f(0.0, -5.0)
    
    glEnd() # The glBegin and glend functions delimit the vertices of a primitive or a group of like primitives.

    # Set points to plot graphic
    # quadratic function points
    light_grid = func_square_grid(center=[0,0],width = 10, radio = 25)
    bold_grid = func_square_grid(center=[0,0],width = 10, radio = 5)
    # get signal data
    signal_vertices = get_singal(T=8)
    
    # I.A.4 Draw a square gird
    for i in np.arange(0, len(light_grid), 2): 
        glBegin(GL_LINES)
        glColor3f(1,0.71,0.75) # Sets the current color RGB
        glVertex2f(light_grid[i,0],light_grid[i,1])
        glVertex2f(light_grid[i+1,0],light_grid[i+1,1])
        glEnd()
        
    for i in np.arange(0, len(bold_grid), 2): 
        glLineWidth(1.5)
        glBegin(GL_LINES)
        glColor3f(1,0.1,0.1) # Sets the current color RGB
        glVertex2f(bold_grid[i,0],bold_grid[i,1])
        glVertex2f(bold_grid[i+1,0],bold_grid[i+1,1])
        glEnd()
        
    # draw the signal
    for i in range(len(signal_vertices)-1): 
        glLineWidth(1.0)
        glBegin(GL_LINES)
        glColor3f(0,0,0) # Sets the current color RGB
        glVertex2f(signal_vertices[i,0],signal_vertices[i,1])
        glVertex2f(signal_vertices[i+1,0],signal_vertices[i+1,1])
        glEnd()
        
    glutSwapBuffers()

"""Function that checks if a key has been pressed on the keyboard"""

# The function called whenever a key is pressed. Note the use of Python tuples to pass in: (key, x, y)  
def keyPressed(*args):
    print(args[0])
    # If escape is pressed, kill everything.
    if args[0]==ESCAPE:
        glutDestroyWindow(window)
        sys.exit(0)

"""Main function with initialization, drawing and querying for external inputs (keyboard)

GLUT_SINGLE

Bit mask to select a single buffered window. This is the default if neither GLUT_DOUBLE or GLUT_SINGLE are specified.

GLUT_RGB

An alias for GLUT_RGBA.

GLUT_RGBA
Bit mask to select an RGBA mode window. This is the default if neither GLUT_RGBA nor GLUT_INDEX are specified.
"""

import numpy as np
import pylab as pl
from biosppy import storage

signal, mdata = storage.load_txt('/Users/amaiaramon/Downloads/ecg.txt')
Fs = mdata['sampling_rate']
N = len(signal)  # number of samples
T = (N - 1) / Fs  # duration
ts = np.linspace(0, T, N, False)  # relative timestamps
pl.plot(ts, signal, 2)
pl.grid()

def main():
    global window
    glutInit(()) #   glutInit is used to initialize the GLUT library.
    glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB) #  glutInitDisplayMode sets the initial display mode.
    glutInitWindowPosition(50,50)
    glutInitWindowSize(500,500)# glutInitWindowPosition and glutInitWindowSize set the initial window position and size respectively.
    glutCreateWindow(b"Function Plotter") #   glutCreateWindow creates a top-level window.
    glutDisplayFunc(plot_func)# glutDisplayFunc sets the display callback for the current window. func The new display callback function.
   
    # When we are doing nothing, redraw the scene.
    glutIdleFunc(plot_func)#  glutIdleFunc sets the global idle callback.
    
    # Register the function called when the keyboard is pressed.  
    glutKeyboardFunc(keyPressed)#  glutKeyboardFunc sets the keyboard callback for the current window.
    # Initialization
    init()
    
    # Main drawing loop
    glutMainLoop() # enters the GLUT event processing loop.

"""Executing main function"""

# Print message to console, and kick off the main to get it rolling.
if __name__ == '__main__':
    print("Hit ESC key to quit.")
    main()

