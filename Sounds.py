#import pygame
#from pygame import mixer

class Sounds():
    def __init__(self):
        #pygame.init()
        self.sound_clock_bell = mixer.Sound('clock_strick.wav')
        self.sound_gun_shot = mixer.Sound('gun_shot.wav')