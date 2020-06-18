
import pygame
import sys
import random
from pygame.locals import (
    QUIT, 
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN
)

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720


## ---------------------------------------- ##
                # CLASSES #

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        
        self.surf = pygame.image.load("./Assets/player0.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect(center=(640, 450))
        


## ---------------------------------------- ##

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen.fill([182, 204, 240])

road = pygame.image.load("./Assets/road.png").convert()

player = Player()









running = True

while running:
    for e in pygame.event.get():
        if e.type == QUIT:
            running = False



    screen.blit(road, [0, 323])
    screen.blit(player.surf, player.rect)


    pygame.display.flip()