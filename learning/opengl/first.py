# Playing around with vertices in OpenGL
# (cc) 2017 Ali Rassolie

import sys
from OpenGL.GLUT import *
from OpenGL.GL import *

def display():
	glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
	glColor3f(1.0, 1.0, 0.0)
	glBegin(GL_QUADS)
	glVertex3f (-0.2, -0.5, 0.0)
	glVertex3f (0.5, -0.5, 0.0)
	glVertex3f (0.5, 0.5, 0.0)
	glVertex3f (-0.5, 0.5, 0.0)
	glEnd()
	glFlush();

glutInit(sys.argv)
glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
glutInitWindowSize(400, 400)
glutCreateWindow(b"oldgl")
glutDisplayFunc(display)
glutMainLoop()