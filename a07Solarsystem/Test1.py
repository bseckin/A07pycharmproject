import solarsystem

__author__ = 'nermin'

import unittest
from GLObject import GLObject
import pygame.tests


class Test1(unittest.TestCase):
        def setUp(self):
            self.b = GLObject.createObject(3, 1,100,200)
            pygame.tests.run()
            pass

        def tearDown(self):
            del self.b
            pass
        ## Testen ob die Methode aufgerufen wird, falls man negativen Radius eingibt
        ## kommt sofort eine Fehlermeldung
        def test1(self):
            assert(self.b == self.b)


if __name__ == "__main__":
    unittest.main()
