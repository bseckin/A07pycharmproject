__author__ = 'nermin'

from OpenGL.GLU import *
from OpenGL.GL import *


class GLObject:
    def createObject(self, radius, slices, stacks):
        """
        Erstellt eine Kugel mit gluSphere und erlaubt Texturierung darauf

        :param radius:
        :param slices:
        :param stacks:
        :return:
        """
        if radius > 0:
            sphere = gluNewQuadric()
            gluQuadricNormals(sphere, GLU_SMOOTH)
            gluQuadricTexture(sphere, GL_TRUE)
            gluSphere(sphere, radius, slices, stacks)
        else:
            raise TypeError("Radius darf nicht negativ sein!")






