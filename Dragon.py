import pygame
from dragon_slayer import *
import MySprite


class Dragon(MySprite):
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
    x_velocity = fireball_velocity

    def update(self):
        self.xPosition += self.x_velocity
        self.rect.center = (self.xPosition, self.yPosition)
