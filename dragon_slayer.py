import pygame
import Weapon
import Player
import Dragon
import sys

# parameter which can be set
screen_width = 1000
screen_height = 500
framerate = 60
fireball_velocity = -3  # in pixels
fireball_delay = 120  # in frames
attack_offset = 15  # in pixels

# The definition of the directions
up = (0, -10)
down = (0, 10)
left = (-10, 0)
right = (10, 0)

# initializing stuff, ignore it
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((screen_width, screen_height))

background = pygame.image.load("background.png")








# initializes the player
gio = Player(50, 50, 100, 100)
gio.setImage("player.png")
player_group = pygame.sprite.Group()
player_group.add(gio)

# initializes the sword
sword = Weapon.Weapon.makeWeapon("sword.png")
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
