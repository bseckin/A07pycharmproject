import pygame
import sys
from pygame.locals import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *

name = 'ball_glut'
class Sphere:
    def main(self):
        pygame.init()
        glutInit(sys.argv)
        glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
        display = (800, 600)
        pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

        gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
        glTranslatef(0.0, 0.0, -15)
        glRotatef(1, 3, 1, 1)
        self.setupLighting()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
            color = [0.0, 0.5, 0.8, 1.]
            glMaterialfv(GL_FRONT, GL_DIFFUSE, color)
            glutSolidSphere(1, 60, 20)
            glRotatef(1, 0, 1, 0)
            pygame.display.flip()
            pygame.time.wait(10)

    def setupLighting(self):
        """ Initializing Lighting and Light0

        :return:
        """
        zeros = (0.15, 0.15, 0.15, 0.3)
        ones = (1.0, 1.0, 1.0, 0.3)
        half = (0.5, 0.5, 0.5, 0.5)

        glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT, zeros)
        glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, half)
        glMaterialf(GL_FRONT_AND_BACK, GL_SHININESS, 15)
        glLightfv(GL_LIGHT0, GL_AMBIENT, zeros)
        glLightfv(GL_LIGHT0, GL_DIFFUSE, ones)
        glLightfv(GL_LIGHT0, GL_SPECULAR, half)
        glEnable(GL_LIGHT0)
        glEnable(GL_LIGHTING)
        glColorMaterial(GL_FRONT_AND_BACK, GL_DIFFUSE)

        glTexGeni(GL_S, GL_TEXTURE_GEN_MODE, GL_SPHERE_MAP)
        glTexGeni(GL_T, GL_TEXTURE_GEN_MODE, GL_SPHERE_MAP)
        glEnable(GL_TEXTURE_GEN_S)
        glEnable(GL_TEXTURE_GEN_T)

        glEnable(GL_COLOR_MATERIAL)
        glEnable(GL_NORMALIZE)
        glShadeModel(GL_SMOOTH)

if __name__ == '__main__':
    main()