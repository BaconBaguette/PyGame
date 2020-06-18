
import pygame

from time import sleep

pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([500,500])

running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    screen.fill((255, 255, 255))
    
    pygame.draw.circle(screen, (180, 0, 255), (125, 250), 150)
    
    pygame.display.flip()
    
    
pygame.quit()