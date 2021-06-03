import MySprite
from dragon_slayer import *


# The player class
class Player(MySprite):
    weapon = None

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
