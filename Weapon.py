from MySprite import MySprite
import pygame

attack_offset = 15  # in pixels


class Weapon(MySprite):
    weapon_group = pygame.sprite.Group()

    def __init__(self, width=20, height=20, pos_x=200, pos_y=200, color=(255, 255, 255)):
        super().__init__(width, height, pos_x, pos_y)
        self.setImage("sword.png")
        Weapon.weapon_group.add(self)

    def attack(self, x_pos, y_pos):
        attacks = pygame.sprite.Group()
        attack = MySprite(10, 50, x_pos + attack_offset, y_pos)
