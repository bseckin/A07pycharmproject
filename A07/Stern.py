__author__ = 'nermin'

from PIL import Image
import pygame
import sys
from pygame.locals import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import pyglet


class Stern(object):

    #def__init__(self,radius, slices, stacks)
        #self.Radius = radius
        #self.Slices = slices
       # self.Stacks = stacks


    def draw(radius, slices, stacks):
         sphere = gluNewQuadric()
         gluQuadricNormals(sphere, GLU_SMOOTH)
         gluQuadricTexture(sphere, GL_TRUE)

         gluSphere(sphere, radius, slices, stacks)




