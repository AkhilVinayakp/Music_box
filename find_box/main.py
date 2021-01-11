import pygame
import os
from player import pablo
print(os.getcwd())
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Find MUSIC BOX")
ico = pygame.image.load('./Music_box/icons/desktop.ico')
pygame.display.set_icon(ico)
running = True

pX = 370
pY = 480
px_c = 0
py_c = 0
#  creating the player
player = pablo.Pablo(screen=screen)

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print('left key down')
                px_c = -.1
            if event.key == pygame.K_RIGHT:
                px_c = .1
                print('right key down')
            if event.key == pygame.K_UP:
                py_c = -.1
                print('up key down')
            if event.key == pygame.K_DOWN:
                py_c = .1
                print('down key down')
        if event.type == pygame.KEYUP:
            if event.key in [pygame.K_LEFT, pygame.K_UP, pygame.K_DOWN, pygame.K_RIGHT] :
                px_c = 0
                py_c = 0
                print('key up')
        pX = px_c + pX
        pY = pY + py_c
        # filling the screen with background color
        screen.fill((0, 128, 128))
        player.move(pX, pY)
        pygame.display.update()

