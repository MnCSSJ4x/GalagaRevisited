import pygame
import random

# initialising the module
pygame.init()

screen = pygame.display.set_mode((800, 600))


class enemy:
    def __init__(self):
        self.enemylooks = pygame.image.load('spaceship.png')
        self.enemyX = random.randint(0, 736)
        self.enemyY = random.randint(50, 108)
        self.enemy_changeX = 0.3
        self.enemy_changeY = 0.3

    def enemy(self, x, y):
        screen.blit(self.enemylooks, (x, y))


class small_enemies:
    def __init__(self):
        self.enemylooks = pygame.image.load('battleship.png')
        self.enemyX = random.randint(0, 736)
        self.enemyY = random.randint(50, 108)
        self.enemy_changeX = 0.3
        self.enemy_changeY = 0.3

    def enemy(self, x, y):
        screen.blit(self.enemylooks, (x, y))


def rungame(list_of_object):
    # game loop. all game functions inside this
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((0, 0, 0))

        # we fill the background and then we call the enemy it is drawn
        # and now we update the display to reflect the new change
        for object in list_of_object:

            object.enemyX += object.enemy_changeX
            object.enemyY += object.enemy_changeY

            # boundary detection
            if object.enemyX <= 0:
                object.enemy_changeX = 0.3
            elif object.enemyX >= 736:
                object.enemy_changeX = -0.3

            if object.enemyY <= 0:
                object.enemy_changeY = 0.3
            elif object.enemyY >= 108:
                object.enemy_changeY = -0.3

            object.enemy(object.enemyX, object.enemyY)
        pygame.display.update()


if __name__ == '__main__':
    boss = enemy()
    chindi = small_enemies()
    chindi2 = small_enemies()
    chindi3 = small_enemies()
    chindi4 = small_enemies()

    rungame([boss,boss, chindi,chindi2,chindi3,chindi4])
