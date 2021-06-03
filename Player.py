from MySprite import MySprite
import pygame
import sys


# The definition of the directions
up = (0, -10)
down = (0, 10)
left = (-10, 0)
right = (10, 0)


# The player class
class Player(MySprite):
    weapon = None
    player_group = pygame.sprite.Group()
    x_vel = 0
    y_vel = 0

    def __init__(self, width, height, pos_x, pos_y, color=(255, 255, 255)):
        super().__init__(width, height, pos_x, pos_y)
        self.setImage("player.png")
        Player.player_group.add(self)

    def setWeapon(self, weaponIn):
        self.weapon = weaponIn

    def attack(self):
        if self.weapon is None:
            print("Player has no weapon")
        else:
            self.weapon.attack(self.xPosition, self.yPosition)

    def move(self):
        self.xPosition += self.x_vel
        self.yPosition += self.y_vel
        self.rect.center = [self.xPosition, self.yPosition]

    def handle_keys(self):
        self.move()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.y_vel -= (1 + abs(self.x_vel))
                    self.x_vel = 0
                elif event.key == pygame.K_DOWN:
                    self.y_vel += (1 + abs(self.x_vel))
                    self.x_vel = 0
                elif event.key == pygame.K_LEFT:
                    self.x_vel -= (1 + abs(self.y_vel))
                    self.y_vel = 0
                elif event.key == pygame.K_RIGHT:
                    self.x_vel += (1 + abs(self.y_vel))
                    self.y_vel = 0
                elif event.key == pygame.K_SPACE:
                    self.attack()
