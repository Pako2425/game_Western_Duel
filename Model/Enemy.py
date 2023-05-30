import pygame
class Enemy():
    def __init__(self, (xpos_enemy, ypos_enemy)):
        self.xpos_enemy = xpos_enemy
        self.ypos_enemy = ypos_enemy
        self.shotTIme = 1.3
        self.enemyWait = pygame.image.load('rewolwerowiec_waiting.png')
        self.enemyAttack = pygame.image.load('rewolwerowiec_holding_guns.png')
        self.enemyShot = pygame.image.load('rewolwerowiec_shoting.png')
        self.enemyCowboy = enemyWait
    #xpos_enemy = 498
    #ypos_enemy = 200
    #shotTime = 1.3
    #enemyWait = pygame.image.load('rewolwerowiec_waiting.png')
    #enemyAttack = pygame.image.load('rewolwerowiec_holding_guns.png')
    #enemyShot = pygame.image.load('rewolwerowiec_shoting.png')
    #enemyCowboy = enemyWait