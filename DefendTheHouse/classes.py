
import pygame
import math
from pygame.locals import (
    RLEACCEL
)

x, y, dx, dy = 1240, 433, 0, 0
bulletX, bulletY = 1240, 433
speed = 8

class Player(pygame.sprite.Sprite):
    def __init__(self, playerPos):
        super(Player, self).__init__()
        self.playerCenter = playerPos
        self.surf = pygame.image.load(".\Assets\Player.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect(
            center = self.playerCenter
        )


class Projectile(pygame.sprite.Sprite):
    def __init__(self, playerPos):
        super(Projectile, self).__init__()
        self.spawnPoint = playerPos
        self.surf = pygame.image.load(".\Assets\Bullet.png").convert()
        self.rect = self.surf.get_rect(
            center = self.spawnPoint
        )

    def update(self, mouseX, mouseY):
        global x, y, dx, dy, bulletX, bulletY
        dx = mouseX - x
        dy = mouseY - y
        angle = math.atan2(dy, dx)
        bulletX += speed * math.cos(angle)
        bulletY += speed * math.sin(angle)