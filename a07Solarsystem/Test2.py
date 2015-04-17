__author__ = 'nermin'

__author__ = 'nermin'

import unittest
from Light import Light

class Test2(unittest.TestCase):
        def setUp(self):
            self.b = Light.setupLighting(self)
            pass

        def tearDown(self):
            del self.b
            pass

        def test1(self):
            assert(self.b == self.b)

if __name__ == "__main__":
    unittest.main()
