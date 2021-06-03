import pygame, sys

class Crosshair(pygame.sprite.Sprite):
    def __init__(self, width, height, pos_x, pos_y, color):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]


pygame.init()
clock = pygame.time.Clock()

screen_width = 1000
screen_height = 500
framerate = 60

screen = pygame.display.set_mode((screen_width, screen_height))

crosshair = Crosshair(50, 50 , 100, 100, (255, 255, 255))

crosshair_group = pygame.sprite.Group()
crosshair_group.add(crosshair)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    crosshair.rect.center = [crosshair.pos_x, crosshair.pos_x]

    pygame.display.flip()
    crosshair_group.draw(screen)
    clock.tick(framerate)
