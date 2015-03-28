from PIL import Image
import pygame
import sys
from pygame.locals import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
from A07.Stern import Stern
from A07.Light import Light


name = 'ball_glut'

class Sphere:
    def main(self):
        """
        initialisiert pygame und erstellt opengl objekte
        :return:
        """
        pygame.init()
        display = (800, 600)
        pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
        pygame.display.set_caption("A07 - Welcome to our solar system")

        gluPerspective(33, (display[0]/display[1]), 0.1, 150.0)
        gluLookAt(0.0, 0.0, 10, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0);

        # Texturen laden
        glEnable(GL_TEXTURE_2D) # Texturierung aktivieren
        self.texture_sonne = self.loadTexture("sonne.jpg")
        self.texture_erde = self.loadTexture("erde.png")
        myLight = Light()

        # Objekte als Stern definieren
        Sonne = Stern()
        Erde = Stern()
        Mond = Stern()
        rotationSpeed = 1
        textureIsActive = True
        lightON = True

        glTranslate(0, 0, -50)
        while True:
            # --- EVENT HANDLING ---
            for event in pygame.event.get():
                #print(event)
                if event.type == pygame.QUIT:
                    # Pygame beenden, wenn Fenster geschlossen wird.
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        # Geschwind. von der Animation erhoehen
                        if(rotationSpeed > 5):
                            print("TOO FAST")
                        else:
                            rotationSpeed += 1
                    if event.key == pygame.K_LEFT:
                        # Geschwind. verlangsamen bzw. stoppen
                        if(rotationSpeed <= 0):
                            print("STOPPED ANIMATION")
                            print(rotationSpeed)
                            rotationSpeed = 0
                        else:
                            rotationSpeed -= 1
                    if event.key == pygame.K_l:
                        print("PRESSED KEY L")
                        if lightON == True:
                            myLight.disableLight()
                            lightON = False
                        else:
                            lightON = True


                if event.type == pygame.MOUSEBUTTONDOWN:
                    print("MOUSE PRESSED!")
                    if textureIsActive == True:        # Check ob Textur AN ist
                        glDisable(GL_TEXTURE_2D)
                        textureIsActive = False
                    else:
                        glEnable(GL_TEXTURE_2D)
                        textureIsActive = True


            glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
            # LICHT einschalten
            if lightON == True:
                myLight.setupLighting()

            #glMatrixMode(GL_MODELVIEW)
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
            #pygame.time.wait(10) #unnötig eigentlich

    def loadTexture(self, pfad):
        """
        Ladet eine Textur/Bild mit dem angegebenen Pfad
        :param pfad:
        :return:
        """
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
     s = Sphere()
     s.main()