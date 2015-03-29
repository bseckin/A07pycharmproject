__author__ = 'SECKIN Berkay'
from OpenGL.GL import *

class Light:
    def setupLighting(self):
        """
        Erlaubt und erstellt anschließend eine Beleuchtung in opengl
        :return:
        """
        glClearColor(0.,0.,0.,1.)
        glShadeModel(GL_SMOOTH)
        glEnable(GL_CULL_FACE)
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_LIGHTING)
        lightZeroPosition = [10, 8., 0., 1.]
        lightZeroColor = [0.8, 1.0, 0.8, 1.0] #green tinged
        glLightfv(GL_LIGHT0, GL_POSITION, lightZeroPosition)
        glLightfv(GL_LIGHT0, GL_DIFFUSE, lightZeroColor)
        glLightf(GL_LIGHT0, GL_CONSTANT_ATTENUATION, 0.1)
        glLightf(GL_LIGHT0, GL_LINEAR_ATTENUATION, 0.05)
        glEnable(GL_LIGHT0)

    def disableLight(self):
        """
        Deaktiviert die Beleuchtung
        :return:
        """
        glDisable(GL_LIGHTING)
        glDisable(GL_LIGHT0)