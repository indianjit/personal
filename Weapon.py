import MySprite
from dragon_slayer import *


class Weapon(MySprite):
    def makeWeapon(self, file_name):
        self.setImage(file_name)
        # self = Weapon(10, 10, 200, 200, (255, 255, 255))

    def attack(self, x_pos, y_pos):
        attacks = pygame.sprite.Group()
        attack = MySprite(10, 50, x_pos + attack_offset, y_pos)
