import PIL
from PIL.Image import Image
import numpy
import pygame
import sys
from pygame.locals import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import pyglet

__author__ = 'Berkay'
class Plnaet:
    def __init__(self, groesse, unterteilung):
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        color = [0.0, 0.5, 0.8, 1.]
        glMaterialfv(GL_FRONT, GL_DIFFUSE, color)

        glutSolidSphere(groesse, unterteilung, 400)

        #sphere = gluNewQuadric()
        #gluQuadricNormals(sphere,GLU_SMOOTH)
        #gluQuadricTexture(sphere,GL_TRUE)
        #glColor4f(1,1,0.2,1)
        #gluSphere(sphere, 2, 100, 100)

        glRotatef(1, 0, 1, 0)
