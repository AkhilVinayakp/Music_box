import pygame
import os
import random

# setting up the path
print(os.getcwd())
# init pygame
pygame.init()
# creating screen
# creating the game window
screen = pygame.display.set_mode((800, 600))
# overriding the icon and title
pygame.display.set_caption("MUSIC BOX")
ico = pygame.image.load('./Music_box/icons/desktop.ico')
pygame.display.set_icon(ico)

# adding the player
playerImg = pygame.image.load('./Music_box/icons/search.ico')
#  initial coordinates of the player
pX = 370
pY = 480
pX_change = 0


def player(x, y):
    if x > 736:
        x = 736
    if x < 0:
        x = 0
    screen.blit(playerImg, (x, y))


# loading the enemy
enemyImg = pygame.image.load('./Music_box/icons/document.ico')
#  initial coordinates of the player
eX = random.randint(0, 736)
eY = random.randint(50, 350)
eX_change = 0


def enemy(x, y):
    screen.blit(enemyImg, (x, y))


#  adding the event for quiting the window
running = True
#  gaming loop
while running:
    for event in pygame.event.get():  # event.get will get all event happening
        if event.type == pygame.QUIT:  # pygame QUITE is an event happens when the close button is clicked
            running = False
        #         keystroke event
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print("key left pressed")
                pX_change = -0.1
            if event.key == pygame.K_RIGHT:
                print("key right pressed")
                pX_change = 0.1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                print("KEY released..")
                pX_change = 0

    #     anything stays all time should be here
    #     filling the screen at the beginning

    screen.fill((0, 128, 128))
    pX = pX + pX_change
    player(pX, pY)
    enemy(eX, eY)
    #     updating the window
    pygame.display.update()
