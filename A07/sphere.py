from PIL import Image
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
        self.texture_sonne = self.loadTexture("sonne.jpg")
        self.texture_erde = self.loadTexture("erde.png")



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
            #color = [0.9, 0.6, 0.01]
            #glColor3d(0.9, 0.6, 0.01)
            #glMaterialfv(GL_FRONT, GL_DIFFUSE, color)


            glEnable(GL_TEXTURE_2D)
            glBindTexture(GL_TEXTURE_2D, self.texture_sonne)
            sphere = gluNewQuadric()
            gluQuadricNormals(sphere,GLU_SMOOTH)
            gluQuadricTexture(sphere,GL_TRUE)

            gluSphere(sphere,5, 200, 400)




            self.setupLighting()
            glPopMatrix()

            glPushMatrix()
            glColor3d(0, 0, 1)
            glRotate(1,0,1,0)
            glTranslate(20,0,0)


            glBindTexture(GL_TEXTURE_2D, self.texture_erde)
            sphere2 = gluNewQuadric()
            gluQuadricNormals(sphere2,GLU_SMOOTH)
            gluQuadricTexture(sphere2,GL_TRUE)

            gluSphere(sphere2,2, 200, 400)


            glPopMatrix()


            glRotatef(1, 0, 1, 0)
            pygame.display.flip()
            pygame.time.wait(10)




    def setupLighting(self):
        glClearColor(0.,0.,0.,1.)
        glShadeModel(GL_SMOOTH)
        glEnable(GL_CULL_FACE)
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_LIGHTING)
        lightZeroPosition = [0, 4., 10., 1.]
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