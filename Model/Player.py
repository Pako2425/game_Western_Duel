import pygame
class Player():
    def __init__(self):
        self.crosshair_xpos = 0
        self.crosshair_ypos = 0
        self.crosshair = pygame.image.load('crosshair.png')
        self.revolver = pygame.image.load('rewolwer.png')
