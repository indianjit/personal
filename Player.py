from MySprite import MySprite
import pygame
import sys

step_size = 20

# The definition of the directions
up = (0, -step_size)
down = (0, step_size)
left = (-step_size, 0)
right = (step_size, 0)


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

    def move(self, direction):
        self.xPosition += direction[0]
        self.yPosition += direction[1]
        self.rect.center = [self.xPosition, self.yPosition]

    def handle_keys(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.move(up)
                elif event.key == pygame.K_DOWN:
                    self.move(down)
                elif event.key == pygame.K_LEFT:
                    self.move(left)
                elif event.key == pygame.K_RIGHT:
                    self.move(right)
                elif event.key == pygame.K_SPACE:
                    self.attack()
