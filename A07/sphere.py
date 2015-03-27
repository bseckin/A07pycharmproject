from PIL import Image
import pygame
import sys
from pygame.locals import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import pyglet
from Stern import Stern

name = 'ball_glut'

class Sphere:
    def main(self):
        """
        initialisiert pygame und erstellt opengl objekte

        :return:
        """
        pygame.init()
        #glutInit(sys.argv)

        display = (800, 600)
        pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
        pygame.display.set_caption("A07 - Welcome to our solar system")
        gluPerspective(33, (display[0]/display[1]), 0.1, 150.0)
        """gluLookAt(
            0,1,20, # eyepoint
            0,0,0, # center-of-view
            0,1,0, # up-vector
	    )"""
        glEnable(GL_TEXTURE_2D) # Texturierung aktivieren

        gluLookAt(0.0, 0.0, 10, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0);

        # Texturen laden
        self.texture_sonne = self.loadTexture("sonne.jpg")
        self.texture_erde = self.loadTexture("erde.png")

        # Objekte als Stern definieren
        Sonne = Stern()
        Erde = Stern()
        Mond = Stern()
        rotationSpeed = 1
        mouseClicked = 0

        glTranslate(0, 0, -50)
        while True:
            for event in pygame.event.get():
                #print(event)
                if event.type == pygame.QUIT:
                    """ Wenn schließen gedrueckt wurde -> pygame beenden"""
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        """ Erhoehe Geschwindigkeit """
                        if(rotationSpeed > 5):
                            print("TOO FAST")
                        else:
                            rotationSpeed += 1
                    if event.key == pygame.K_LEFT:
                        """ Verlangsame Geschwindigkeit """
                        if(rotationSpeed <= 0):
                            print("STOPPED ANIMATION")
                            print(rotationSpeed)
                            rotationSpeed = 0
                        else:
                            rotationSpeed -= 1
                        print("key LEFT")
                if event.type == pygame.MOUSEBUTTONDOWN:
                    print("MOSUE GEDRUECKT")
                    if mouseClicked == 0:
                        mouseClicked = 1 #Maus geklickt
                        glDisable(GL_TEXTURE_2D)
                    else:
                        mouseClicked = 0
                        glEnable(GL_TEXTURE_2D)


            glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
            self.setupLighting()    # Licht einschalten
            glMatrixMode(GL_MODELVIEW)

            glTranslate(0,0,0)
            glBindTexture(GL_TEXTURE_2D, self.texture_sonne)
            Sonne.createObject(5, 200, 400)
            glRotate(rotationSpeed, 0, 1, 0)

            glPushMatrix()
            glBindTexture(GL_TEXTURE_2D, self.texture_erde)
            glTranslate(20, 0, 0)
            Erde.createObject(2,200,400)
            glPopMatrix()

            # Noch ein Planet
            glPushMatrix()
            glBindTexture(GL_TEXTURE_2D, self.texture_erde)
            glTranslate(-15, 0, 0)
            Erde.createObject(1, 200,400)
            glPopMatrix()

            pygame.display.flip()
            pygame.time.wait(10)


    def setupLighting(self):
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


    def loadTexture(self, pfad):

        #Load texture file
        data = Image.open(pfad)
        ix = data.size[0]
        iy = data.size[1]
        data = data.tostring("raw", "RGBX", 0, -1)

        # Create textures
        textures = glGenTextures(1)

        # Select our current texture
        #glBindTexture(GL_TEXTURE_2D, int(textures[0]))   # 2d texture (x and y size)

        # Create a MipMapped Texture
        glBindTexture(GL_TEXTURE_2D, textures)

        glTexParameteri(GL_TEXTURE_2D,GL_TEXTURE_MAG_FILTER,GL_LINEAR)
        glTexParameteri(GL_TEXTURE_2D,GL_TEXTURE_MIN_FILTER,GL_LINEAR_MIPMAP_NEAREST)

        gluBuild2DMipmaps(GL_TEXTURE_2D, 3, ix, iy, GL_RGBA, GL_UNSIGNED_BYTE, data)


        return textures

if __name__ == '__main__':
     glutInit(sys.argv)
     s = Sphere()
     s.main()