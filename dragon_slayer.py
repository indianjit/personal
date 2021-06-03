# be able to restart the game if won or lost
# make the


import pygame
from Weapon import Weapon
from Player import Player
from Dragon import Dragon

# parameter which can be set
screen_width = 1000
screen_height = 500
framerate = 60

# initializing stuff, ignore it
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((screen_width, screen_height))

background = pygame.image.load("background.png")

# initializes the player
gio = Player(50, 50, 100, 100)

# initializes the sword
sword = Weapon()

# initializes the dragon
dragon = Dragon(10, 10, 900, 300)

# boolean which are kept track of
swordPickedUp = False
gameOver = False

# useful tools
point_rect = pygame.Surface([0, 0]).get_rect()


def paintScreen():
    global swordPickedUp
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    Player.player_group.draw(screen)
    if not swordPickedUp:
        Weapon.weapon_group.draw(screen)
    Dragon.boss_group.draw(screen)
    dragon.fireball_group.draw(screen)


def write(message):
    myfont = pygame.font.SysFont("monospace", 16)
    text = myfont.render(message, 1, (0, 0, 0))
    screen.blit(text, (400, 300))
    pygame.display.update()


def checkInteractions():
    global swordPickedUp, gameOver, gio

    for fb in dragon.fireball_group:
        if fb.rect.colliderect(gio.rect):
            gameLost()

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
    write("You lost the game!")
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
        checkInteractions()
        paintScreen()
        pygame.display.flip()
        clock.tick(framerate)
