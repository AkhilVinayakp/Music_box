import pygame
import random
import os


# creating player class
class Pablo:
    def __init__(self, screen):
        self.screen = screen
        self.pablo_img = pygame.image.load("../../icons/search.ico")
        self.screen.blit(self.pablo_img, (370, 480))

    def move(self, x, y):
        if x > 736:
            x = 0
        elif x < 0:
            x = 736
        elif y > 736:
            y = 0
        elif y < 0:
            y = 736
        self.screen.blit(self.pablo_img, (x, y))
