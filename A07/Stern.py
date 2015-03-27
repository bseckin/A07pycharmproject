__author__ = 'nermin'

from OpenGL.GLU import *
from OpenGL.GL import *


class Stern:

    #def__init__(self,radius, slices, stacks)
        #self.Radius = radius
        #self.Slices = slices
       # self.Stacks = stacks

    def createObject(self, radius, slices, stacks):
        """
        Erstellt eine Kugel mit gluSphere und erlaubt Texturierung darauf

        :param radius:
        :param slices:
        :param stacks:
        :return:
        """
        sphere = gluNewQuadric()
        gluQuadricNormals(sphere, GLU_SMOOTH)
        gluQuadricTexture(sphere, GL_TRUE)
        gluSphere(sphere, radius, slices, stacks)




