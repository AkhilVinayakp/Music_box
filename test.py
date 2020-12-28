import pygame
import os

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
pX = 370
pY = 480


def player():
    screen.blit(playerImg, (pX, pY))


#  adding the event for quiting the window
running = True
#  gaming loop
while running:
    for event in pygame.event.get():   # event.get will get all event happening
        if event.type == pygame.QUIT:  # pygame QUITE is an event happens when the close button is clicked
            running = False

#     anything stays all time should be here
#     filling the screen at the beginning

    screen.fill((0, 128, 128))
    player()
#     updating the window
    pygame.display.update()


