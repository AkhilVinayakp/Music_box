import pygame
import os

# initializing pygame
pygame.init()
# setting up the screen
screen = pygame.display.set_mode((800, 600))


# creating class for the character
class Character:
    def __init__(self, image, pos=(370, 480)):
        self.image = image
        screen.blit(image, pos)

    def move_ch(self, x, y):
        screen.blit(self.image, (x, y))


class Player(Character):
    def __init__(self):
        image = pygame.image.load("./Music_box/icons/search.ico")
        super().__init__(image)

    def move(self, x, y):
        if x < 0:
            x = 0
        elif x > 756:
            x = 756
        super().move_ch(x, y)
        return x, y


pablo = Player()
# creating the title and icon
pygame.display.set_caption("music box")
icon = pygame.image.load("./Music_box/icons/document.ico")
pygame.display.set_icon(icon)
pX = 370
pY = 480
px_c = 0
py_c = 0
# creating game loop
running = True
while running:
    # cdf
    screen.fill((0, 127, 129))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #     movement controlling of the player
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print('left')
                px_c = -0.1
            if event.key == pygame.K_RIGHT:
                print('right')
                px_c = 0.1
            if event.key == pygame.K_UP:
                print('up')
                py_c = -0.1
            if event.key == pygame.K_DOWN:
                print('down')
                py_c = 0.1
        if event.type == pygame.KEYUP:
            if event.key in[pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT]:
                px_c = 0
                py_c = 0

    pX = pX + px_c
    pY = pY + py_c
    pX, pY = pablo.move(pX, pY)
    pygame.display.update()
