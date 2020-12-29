import pygame
import os


print(os.getcwd())
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Find MUSIC BOX")
ico = pygame.image.load('./Music_box/icons/desktop.ico')
pygame.display.set_icon(ico)
running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False