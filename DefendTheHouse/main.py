
import pygame
import sys
import random
from classes import Player, Projectile
from pygame.locals import (
    QUIT, 
    RLEACCEL,
    K_SPACE,
    KEYDOWN,
    MOUSEBUTTONUP
)

SCREENWIDTH = 1600
SCREENHEIGHT = 800

playerPos = (1240, 433)

pygame.init()

screen = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
bgImage = pygame.image.load(".\Assets\Background.png").convert()

player = Player(playerPos)

bulletSprites = pygame.sprite.Group()

running = True

clock = pygame.time.Clock()




while running:

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == MOUSEBUTTONUP:
            newBullet = Projectile(playerPos)
            bulletSprites.add(newBullet)
            mouseX, mouseY = pygame.mouse.get_pos()

    pressedKeys = pygame.key.get_pressed()

    
    
    screen.blit(bgImage, (0, 0))
    screen.blit(player.surf, player.rect)

    if len(bulletSprites) > 0:
        for bullet in bulletSprites:
            bullet.update(mouseX, mouseY)

    for bullet in bulletSprites:
        screen.blit(bullet.surf, bullet.rect)

    pygame.display.flip()

    clock.tick(144)

