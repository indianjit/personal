# have a player rectangle/sprite. when that sprite touches a sword sprite and then touches
# a dragon sprite, the game is won. If the player touches the dragon before the sword, the game is lost.

# Objective 1:
# draw a player sprite to the screen. Complete!

# Objective 2:
# draw a sword and dragon onto the screen (dragon is red, sword is blue, player is green). Complete

# Objective 3:
# be able to move the player sprite. Complete!

# Objective 3.5:
# Rework the current system to use pygame sprites.

# Objective 4:
# Be able to pick up the sword and kill the dragon!

import pygame
import sys
import time

# parameter which can be set
screen_width = 1000
screen_height = 500
framerate = 60

# The definition of the directions
up = (0, -10)
down = (0, 100)
left = (-10, 0)
right = (100, 0)

# initializing stuff, ignore it
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((screen_width, screen_height))

background = pygame.image.load("background.png")


# default class off of which other classes will be built
class mySprite(pygame.sprite.Sprite):
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


# The player class
class Player(mySprite):
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


class FireBall(mySprite):
    x_velocity = -1

    def update(self):
        self.xPosition += self.x_velocity
        self.rect.center = (self.xPosition, self.yPosition)


class Dragon(mySprite):
    yVelocity = 1
    activeFireBalls = []

    def shootFireBall(self):
        fb = FireBall(10, 10, self.xPosition - 40, self.yPosition)
        fb.setImage("fireball.png")
        self.activeFireBalls.add(fb)

    def updateFireBalls(self):
        active_fire_balls_copy = self.activeFireBalls.copy();
        for fireBall in active_fire_balls_copy:
            if fireBall.xPosition < 0:
                self.activeFireBalls.remove(fireBall)

    def update(self):
        self.yPosition += self.yVelocity

        if self.yPosition > screen_height and self.yVelocity > 0:
            self.yVelocity *= -1
        elif self.yPosition < 0 and self.yVelocity < 0:
            self.yVelocity *= -1
        self.rect.center = (self.xPosition, self.yPosition)

        self.updateFireBalls()


# initializes the player
gio = Player(50, 50, 100, 100)
gio.setImage("player.png")
player_group = pygame.sprite.Group()
player_group.add(gio)

# initializes the sword
sword = mySprite(10, 10, 200, 200)
sword.setImage("sword.png")
weapon_group = pygame.sprite.Group()
weapon_group.add(sword)

# initializes the dragon
dragon = Dragon(10, 10, 900, 300)
dragon.setImage("dragon.png")
boss_group = pygame.sprite.Group()
boss_group.add(dragon)

# boolean which are kept track of
swordPickedUp = False
gameOver = False

# useful tools
point_rect = pygame.Surface([0, 0]).get_rect()


def paintScreen():
    global swordPickedUp
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    player_group.draw(screen)
    if not swordPickedUp:
        weapon_group.draw(screen)
    boss_group.draw(screen)


def write(message):
    myfont = pygame.font.SysFont("monospace", 16)
    text = myfont.render(message, 1, (0, 0, 0))
    screen.blit(text, (400, 300))
    pygame.display.update()


def checkInteractions():
    global swordPickedUp, gameOver, gio
    if sword.rect.colliderect(gio.rect):
        swordPickedUp = True
        gio.setImage("playerWithSword.png")

    if dragon.rect.colliderect(gio.rect):
        if swordPickedUp:
            gameWon()
        else:
            gameLost()


def gameLost():
    global gameOver
    write("You won the game!")
    gameOver = True


def gameWon():
    global gameOver
    write("You lost the game!")
    gameOver = True


# main game loop
while True:
    if not gameOver:
        gio.handle_keys()
        dragon.update()
        paintScreen()
        pygame.display.flip()
        clock.tick(framerate)
        checkInteractions()
