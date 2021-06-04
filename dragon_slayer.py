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
dragon_health_loss = 25  # the health loss by the dragon per hit of fireball

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
    Weapon.attacks.draw(screen)


myfont = pygame.font.SysFont("monospace", 16)


def checkInteractions():
    global swordPickedUp, gameOver, gio

    # checks the interactions of the fireballs with the player and with the attack
    for fb in dragon.fireball_group:
        if fb.rect.colliderect(gio.rect):
            gameLost()
        else:
            for at in sword.attacks.sprites():
                if fb.rect.colliderect(at) and fb.x_velocity < 0:
                    fb.x_velocity *= -1

        if fb.rect.colliderect(dragon.rect):
            dragon.decrease_health(dragon_health_loss)
            fb.kill()

    # check if fireball touch the dragon, if they do, decrease the health of the dragon.

    # checks if the player has picked up the sword
    if sword.rect.colliderect(gio.rect):
        swordPickedUp = True
        gio.setWeapon(sword)
        gio.setImage("playerWithSword.png")

    # checks if the player has touched the dragon
    if dragon.rect.colliderect(gio.rect):
        if swordPickedUp:
            gameWon()
        else:
            gameLost()


def gameLost():
    global gameOver
    #write("You lost the game!")
    gameOver = True


def gameWon():
    global gameOver
    #write("You lost the game!")
    gameOver = True



text = myfont.render(str(dragon.health), 1, (0, 0, 0))
screen.blit(text, (800, 100))
pygame.display.update()

# main game loop
while True:
    if not gameOver:
        gio.handle_keys()
        dragon.update()
        sword.update()

        checkInteractions()
        paintScreen()
        pygame.display.flip()
        clock.tick(framerate)
