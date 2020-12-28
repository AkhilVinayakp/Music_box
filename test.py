import pygame
# init pygame
pygame.init()
# creating screen
# creating the game window
screen = pygame.display.set_mode((800,600))

#  adding the event for quiting the window
running = True
#  gaming loop
while running:
    for event in pygame.event.get():   # event.get will get all event happening
        if event.type == pygame.QUIT:  # pygame QUITE is an event happens when the close button is clicked
            running = False


