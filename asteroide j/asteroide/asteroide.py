import pygame
from pygame.locals import *
import sys
from ship import *

size = width, height= 800, 600

screen = pygame.display.set_mode (size)

def main():
    pygame.init()

    background_imagen =pygame.image.load("imagenes\espacio 1.jpeg")
    background_rect = background_imagen.get_rect()

    pygame.display.set_caption("Asteroids")

    ship = Ship(size)

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exist()
        ship.update()
        screen.blit(background_imagen,background_rect)
        screen.blit(ship.imagen, ship.rect)
        pygame.display.update()
        pygame.time.delay(10)
if __name__=="__main__":
    main()
