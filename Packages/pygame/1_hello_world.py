import pygame
import sys
from pygame.locals import *

# Pygame Initialization
pygame.init()

screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Hello World")
colour = (70, 60, 40)

while True:
    screen.fill((255, 255, 255))
    for each_event in pygame.event.get():
        if each_event.type == QUIT:
            pygame.quit()
            sys.exit()
    # pygame.display.update()
    pygame.draw.rect(screen, colour, pygame.Rect(10, 10, 100, 50),500)
    pygame.display.flip()
