from MySprite import MySprite
import pygame

screen_height = 500
fireball_velocity = -3  # in pixels
fireball_delay = 120  # in frames


class Dragon(MySprite):
    boss_group = pygame.sprite.Group()

    def __init__(self, width, height, pos_x, pos_y, color=(255, 255, 255)):
        super().__init__(width, height, pos_x, pos_y)
        self.setImage("dragon.png")
        Dragon.boss_group.add(self)

    yVelocity = 1
    timer = 0
    fireball_group = pygame.sprite.Group()

    def shootFireBall(self):
        fb = FireBall(10, 10, self.xPosition - 40, self.yPosition)
        fb.setImage("fireball.png")
        self.fireball_group.add(fb)

    def updateFireBalls(self):
        fire_balls_group_copy = self.fireball_group.copy()
        for fireBall in fire_balls_group_copy:
            if fireBall.xPosition < 0:
                self.fireball_group.remove(fireBall)
            else:
                fireBall.update()

    def update(self):
        self.timer += 1
        self.yPosition += self.yVelocity

        if self.yPosition > screen_height and self.yVelocity > 0:
            self.yVelocity *= -1
        elif self.yPosition < 0 and self.yVelocity < 0:
            self.yVelocity *= -1
        self.rect.center = (self.xPosition, self.yPosition)
        if self.timer % fireball_delay == 0:
            self.shootFireBall()
        self.updateFireBalls()


class FireBall(MySprite):
    # TODO what the heck is going on here? why is fireball_velocity not working?
    x_velocity = fireball_velocity

    def update(self):
        self.xPosition += self.x_velocity
        self.rect.center = (self.xPosition, self.yPosition)
