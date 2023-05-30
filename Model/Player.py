import pygame
class Player():
    def __init__(self):
        self.xpos_mouse = 0
        self.ypos_mouse = 0
        self.dxpos_mouse = 0
        self.dypos_mouse = 0
        self.xpos_crosshair = 0
        self.ypos_crosshair = 0
        self.crosshair = pygame.image.load('crosshair.png')
        self.rewolwer = pygame.image.load('rewolwer.png')
