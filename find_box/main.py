import pygame
import os
from .player import pablo
print(os.getcwd())
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Find MUSIC BOX")
ico = pygame.image.load('./Music_box/icons/desktop.ico')
pygame.display.set_icon(ico)
running = True

#  creating the player
player = pablo.Pablo(screen=screen)

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                px_c = -.1
            if event.key == pygame.K_RIGHT:
                px_c = .1
            if event.key == pygame.K_UP:
                py_c = -.1
            if event.key == pygame.K_DOWN:
                py_c = .1
        if event.type == pygame.KEYUP:
            if event.key in [pygame.K_LEFT, pygame.K_UP, pygame.K_DOWN, pygame.K_RIGHT] :
                px_c, py_c = 0

        # filling the screen with background color
        screen.fill((0, 128, 128))


