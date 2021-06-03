import pygame, sys

pygame.init()
clock = pygame.time.Clock()

screen_width = 1000
screen_height = 500
framerate = 60

screen = pygame.display.set_mode((screen_width, screen_height))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.flip()
    clock.tick(framerate)