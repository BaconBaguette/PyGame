
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

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 670

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.walkSequence = ["1.png", "2.png", "3.png", "2.png", "4.png", "5.png", "6.png", "5.png"]
        self.currentStep = 0
        self.surf = pygame.image.load(".\PlayerSprite\\" + self.walkSequence[self.currentStep]).convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect(
            center = (300, 340)
        )

    def changeStep(self):
        if self.currentStep < 7:
            self.currentStep += 1
        else:
            self.currentStep = 0
        self.surf = pygame.image.load(".\PlayerSprite\\" + self.walkSequence[self.currentStep]).convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)

    def update(self, pressedKeys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)

        if self.rect.left < -10:
            self.rect.left = -10
        if self.rect.right > SCREEN_WIDTH + 10:
            self.rect.right = SCREEN_WIDTH + 10
        if self.rect.bottom < 330:
            self.rect.bottom = 330
        if self.rect.bottom > SCREEN_HEIGHT + 20:
            self.rect.bottom = SCREEN_HEIGHT + 20


class MiddleLine(pygame.sprite.Sprite):
    def __init__(self):
        super(MiddleLine, self).__init__()
        self.surf = pygame.image.load("middleLine.png").convert()
        self.rect = self.surf.get_rect(
            center = (SCREEN_WIDTH + 20, 640)
        )
        
    def update(self):
        self.rect.move_ip(-5, 0)
        if self.rect.right < 0:
            self.kill()
            

class PavementLine(pygame.sprite.Sprite):
    def __init__(self):
        super(PavementLine, self).__init__()
        self.surf = pygame.image.load("pavementLine.png").convert()
        self.rect = self.surf.get_rect(
            center = (SCREEN_WIDTH + 20, 367)
        )
        
    def update(self):
        self.rect.move_ip(-5, 0)
        if self.rect.right < 0:
            self.kill()
            

class RoadSpatter(pygame.sprite.Sprite):
    def __init__(self):
        super(RoadSpatter, self).__init__()
        self.surf = pygame.image.load("spatter.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect(
            center=(SCREEN_WIDTH * 1.5, 570)
        )
    
    def update(self):
        self.rect.move_ip(-5, 0)
        if self.rect.right < 0:
            self.kill()
            

class House(pygame.sprite.Sprite):
    def __init__(self):
        super(House, self).__init__()
        self.images = ["house1.png", "house2.png", "house3.png"]
        self.surf = pygame.image.load(self.images[random.randint(0, 2)]).convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect(
            center = (SCREEN_WIDTH + 200, 145)
        )
        
    def update(self):
        self.rect.move_ip(-5, 0)
        if self.rect.right < 0:
            self.kill()
            
           
pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
bgImage = pygame.image.load('background.png').convert()
doubleYellow = pygame.image.load("doubleYellow.png").convert()
doubleYellow.set_colorkey((255, 255, 255), RLEACCEL)

ADDMIDDLELINE = pygame.USEREVENT + 1
pygame.time.set_timer(ADDMIDDLELINE, 1000)

ADDPAVEMENTLINE = pygame.USEREVENT + 2
pygame.time.set_timer(ADDPAVEMENTLINE, 400)

ADDROADSPATTER = pygame.USEREVENT + 3
pygame.time.set_timer(ADDROADSPATTER, 2000)

ADDHOUSE = pygame.USEREVENT + 4
pygame.time.set_timer(ADDHOUSE, 900)

CHANGESTEP = pygame.USEREVENT + 5
pygame.time.set_timer(CHANGESTEP, 100)

backgroundSprites = pygame.sprite.Group()

player = Player()

running = True

clock = pygame.time.Clock()

while running:

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == ADDMIDDLELINE:
            newMiddleLine = MiddleLine()
            backgroundSprites.add(newMiddleLine)
        if event.type == ADDPAVEMENTLINE:
            newPavementLine = PavementLine()
            backgroundSprites.add(newPavementLine)
        if event.type == ADDROADSPATTER:
            newRoadSpatter = RoadSpatter()
            backgroundSprites.add(newRoadSpatter)
        if event.type == ADDHOUSE:
            newHouse = House()
            backgroundSprites.add(newHouse)
        if event.type == CHANGESTEP:
            player.changeStep()
            
    pressed_keys = pygame.key.get_pressed()

    player.update(pressed_keys)

    backgroundSprites.update()
          
    backgroundSprites.update()
    
    screen.blit(bgImage, [0,0])
    for entity in backgroundSprites:
        screen.blit(entity.surf, entity.rect)

    screen.blit(doubleYellow, [0, 450])

    screen.blit(player.surf, player.rect)

    pygame.display.flip()
    
    clock.tick(60)
    
    
    
    
    
    
    
    
    
    
    
    
    
