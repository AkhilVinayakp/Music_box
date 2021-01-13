import pygame
import os
from player.pablo import Pablo
pygame.init()
screen = pygame.display.set_mode((800, 600))
pablo = Pablo(screen)
print(pablo)
# overriding the icon and title
pygame.display.set_caption("MUSIC BOX")
ico = pygame.image.load('./Music_box/icons/desktop.ico')
pygame.display.set_icon(ico)

running = True
while running:
    screen.fill((0, 128, 128))
    for event in pygame.event.get():  # event.get will get all event happening
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()
