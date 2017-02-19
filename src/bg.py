import pygame
from pygame.locals import *

pygame.init()
pygame.display.set_caption('Test')
screen = pygame.display.set_mode((800, 600))
bg = pygame.image.load('resources/bg.png')
screen.fill(0)
screen.blit(bg, (0, 0))

while True:
    pygame.display.flip()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
