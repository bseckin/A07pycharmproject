__author__ = 'nermin'

from A07.solarsystem import Solarsystem
import pygame
from OpenGL.GLUT import *


class Tutorial():
    def startTutorial(self):
        """
        Startet ein PygameFenster in dem eine Anleitung zur Benutzung des Spiels ist
        :return:
        """
        tyrkis = (0, 255, 255)
        black = (0, 0, 0)

        pygame.init()
        size = (700, 500)
        screen = pygame.display.set_mode(size)
        pygame.display.set_caption("TUTORIAL")
        done = False
        clock = pygame.time.Clock()

        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        """ Zur Animation kommen"""
                        s = Solarsystem()
                        s.main()

            screen.fill(tyrkis)

            font = pygame.font.Font(None, 25)
            text = font.render("Rechte Pfeiltaste --> Animation wird schneller", True, black)

            screen.blit(text, [100, 100])
            text = font.render("Linke Pfeiltaste -->  Animation wird langsamer", True, black)
            screen.blit(text, [100, 150])
            text = font.render("Mausklick --> Textur Ein/Ausblenden", True, black)
            screen.blit(text, [100, 200])
            text = font.render("L --> Licht Ein/Ausschalten", True, black)
            screen.blit(text, [100, 250])
            text = font.render("Space --> Zur Animation", True, black)
            screen.blit(text, [100, 350])

            pygame.display.flip()
            clock.tick(60)


if __name__ == '__main__':
    glutInit(sys.argv)
    t = Tutorial()
    t.startTutorial()
