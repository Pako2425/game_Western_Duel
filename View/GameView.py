import pygame
from pygame import mixer
from Model import game_config

class GameView():
    def __init__(self):
        pygame.init()
        #ground_level
        #win = pygame.display.set_mode((myGameWindow.win_width, myGameWindow.win_height))
        self.win = pygame.display.set_mode((game_config.GAME_WINDOW_WIDTH, game_config.GAME_WINDOW_HEIGHT))
        self.font = pygame.font.SysFont('arial', 20)

    def displayText(self, text, (xpos, ypos), size, colour):
        font = pygame.font.SysFont('arial', size)
        textForDisplay = font.render(text, True, colour)
        self.win.blit(textForDisplay, (xpos, ypos))

    def drawBackground(self):
        self.win.fill(game_config.BLUE_COLOUR)

    def drawGround(self, groundColour, groundLevel):
        pygame.draw.rect(self.win, game_config.GROUND_COLOUR, (0, game_config.GROUND_LEVEL, game_config.GAME_WINDOW_WIDTH, game_config.GAME_WINDOW_HEIGHT - game_config.GROUND_LEVEL))

    def drawEnemy(self, enemy, (enemy_xpos, enemy_ypos)):
        self.win.blit(enemy, (enemy_xpos, enemy_ypos))

    def drawCrosshair(self, crosshair, (crosshair_xpos, crosshair_ypos)):
        self.win.blit(crosshair, (crosshair_xpos, crosshair_ypos))

    def drawPlayerGun(self, gun, (playerGun_xpos, playerGun_ypos)):
        self.win.blit(gun, (playerGun_xpos, playerGun_ypos))

    def playClockBellSound(self, soundPath):
        mixer.Sound(soundPath).play()

    def playGunShotSound(self, soundPath):
        mixer.Sound(soundPath).play()