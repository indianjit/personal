import pygame


# default class off of which other classes will be built
class MySprite(pygame.sprite.Sprite):
    def __init__(self, width, height, pos_x, pos_y, color=(255, 255, 255)):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.xPosition = pos_x
        self.yPosition = pos_y
        self.rect.center = [pos_x, pos_y]

    def setImage(self, fileName):
        self.image = pygame.image.load(fileName)
        self.rect = self.image.get_rect()
        self.rect.center = (self.xPosition, self.yPosition)
