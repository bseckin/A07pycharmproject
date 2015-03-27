from turtle import done

__author__ = 'nermin'

import pygame
from OpenGL.GLUT import *


class Tutorial():
    def test(self):

        black = (0,0,0)
        white = (255,255,255)

        pygame.init()
        size =(700,500)
        screen = pygame.display.set_mode(size)
        pygame.display.set_caption("TUTORIAL")
        done = False
        clock = pygame.time.Clock()

        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True


            screen.fill(black)

            font = pygame.font.Font(None,25)
            text = font.render("Rechte Pfeiltaste '->' ... schneller!", True, white)

            screen.blit(text,[100,100])
            text = font.render("Linke Pfeiltaste '<-'  ... laaangsamer", True, white)
            screen.blit(text,[100,150])
            pygame.display.flip()
            clock.tick(60)
    pygame.quit()



if __name__ == '__main__':
     glutInit(sys.argv)
     t = Tutorial()
     t.test()
