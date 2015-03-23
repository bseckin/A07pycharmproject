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

name = 'ball_glut'
class Sphere:
    def main(self):
        """
        initialisiert pygame und erstellt opengl objekte

        :return:
        """

        pygame.init()
        glutInit(sys.argv)
        glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
        display = (800, 600)
        pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

        gluPerspective(33, (display[0]/display[1]), 0.1, 150.0)
        """gluLookAt(
            0,1,20, # eyepoint
            0,0,0, # center-of-view
            0,1,0, # up-vector
	    )"""
      #  glTranslatef(0.0, 0.0, -15)
        glRotatef(1, 3, 1, 1)


        gluLookAt(0.0, 0.0, 10, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0);
        #self.LoadTextures2()
        #self.loadTexture()

        x = 1
        glTranslate(0,0,-100)
        while True:
            for event in pygame.event.get():
                print(event)
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        print("key UP")
                        if x == 7:
                            print("maximum")
                        else :
                            x += 1
                            print(x)
                    if event.key == pygame.K_DOWN:
                        print("key down")
                        x -= 1

            glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

            glPushMatrix()
            color = [0.9, 0.6, 0.01]
            glColor3d(0.9, 0.6, 0.01)
            glMaterialfv(GL_FRONT, GL_DIFFUSE, color)

            glutSolidSphere(5, 200, 400)

            self.setupLighting()
            glPopMatrix()

            glPushMatrix()
            glColor3d(0, 0, 1)
            glRotate(1,0,1,0)
            glTranslate(20,0,0)

            glutSolidSphere(2,200,200)

            glPopMatrix()
            #sphere = gluNewQuadric()
            #gluQuadricNormals(sphere,GLU_SMOOTH)
            #gluQuadricTexture(sphere,GL_TRUE)
            #glColor4f(1,1,0.2,1)
            #gluSphere(sphere, 2, 100, 100)

            glRotatef(1, 0, 1, 0)
            pygame.display.flip()
            pygame.time.wait(10)

    def setupLighting(self):
        glClearColor(0.,0.,0.,1.)
        glShadeModel(GL_SMOOTH)
        glEnable(GL_CULL_FACE)
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_LIGHTING)
        lightZeroPosition = [10., 4., 10., 1.]
        lightZeroColor = [0.8, 1.0, 0.8, 1.0] #green tinged
        glLightfv(GL_LIGHT0, GL_POSITION, lightZeroPosition)
        glLightfv(GL_LIGHT0, GL_DIFFUSE, lightZeroColor)
        glLightf(GL_LIGHT0, GL_CONSTANT_ATTENUATION, 0.1)
        glLightf(GL_LIGHT0, GL_LINEAR_ATTENUATION, 0.05)
        glEnable(GL_LIGHT0)

    def loadTexture(self):
        glEnable(GL_TEXTURE_2D)
        image = pyglet.image.load("erde.png")
        texture = image.get_texture()
        glEnable(texture.target)
        glBindTexture(texture.target, texture.id)


    def LoadTextures2(self):
        global texture_num, textures
        image = open("erd.bmp")

        ix = image.size[0]
        iy = image.size[1]
        image = image.tostring("raw", "RGBX", 0, -1)

        # Create Texture
        textures = glGenTextures(3)
        glBindTexture(GL_TEXTURE_2D, int(textures[0]))   # 2d texture (x and y size)

        glPixelStorei(GL_UNPACK_ALIGNMENT,1)
        glTexImage2D(GL_TEXTURE_2D, 0, 3, ix, iy, 0, GL_RGBA, GL_UNSIGNED_BYTE, image)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
        glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)

if __name__ == '__main__':
    s = Sphere()
    s.main()