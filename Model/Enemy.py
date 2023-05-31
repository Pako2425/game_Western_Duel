import pygame
class Enemy():
    def __init__(self, xpos_enemy, ypos_enemy, shotTime):
        self.xpos_enemy = xpos_enemy
        self.ypos_enemy = ypos_enemy
        self.shotTime = shotTime
        self.enemyWait = pygame.image.load('rewolwerowiec_waiting.png')
        self.enemyAttack = pygame.image.load('rewolwerowiec_holding_guns.png')
        self.enemyShot = pygame.image.load('rewolwerowiec_shoting.png')
        self.enemyCowboy = self.enemyWait

    def setWaitPose(self):
        self.enemyCowboy = self.enemyWait

    def setAttackPose(self):
        self.enemyCowboy = self.enemyAttack

    def setShotPose(self):
        self.enemyCowboy = self.enemyShot
