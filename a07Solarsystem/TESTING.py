
__author__ = 'seckin und nermin'

import a07Solarsystem.GLObject
from a07Solarsystem.Light import *
from a07Solarsystem.solarsystem import *
from a07Solarsystem.GLObject import *
import unittest
import pygame.tests

class Test_GLObject(unittest.TestCase):
        def test_erstelleObjektMitNegativenRadius(self):
            #pass
            #self.o = GLObject().erstelleObjekt(-10, 30, 20)
            with self.assertRaises(TypeError):
                self.o = GLObject().erstelleObjekt(-10, 30, 20)

        def test_erstelleObjektKorrektenEingaben(self):
            self.o = GLObject().erstelleObjekt(5, 30, 20)
            self.assertRaises(TypeError, None)

class Test_Light(unittest.TestCase):
        def test_LightsetUp(self):
            with self.assertRaises(GLError):
                self.b = Light.setupLighting(self)


class Test_Solarsystem(unittest.TestCase):
        def test_loadTexturpfad(self):
            pass
            #with self.assertRaises(error):
            #    self.solar = Solarsystem().loadTexture(1234)

if __name__ == "__main__":
    unittest.main()
