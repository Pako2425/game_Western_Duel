from Model import game_config
from Model import GameData
from View import GameView
from Controller import Stoper
import pygame
import random


class GameController():
    def __init__(self):
        pygame.init()
        self.gameData = GameData.GameData()
        self.gameView = GameView.GameView()
        self.gameStoper = Stoper.Stoper()

        pygame.mouse.set_visible(False)
        self.mouse_xpos = 0
        self.mouse_ypos = 0
        self.mouse_dxpos = 0
        self.mouse_dypos = 0



    def readMousePos(self):
        self.mouse_xpos, self.mouse_ypos = pygame.mouse.get_pos()

    def readKeyboardInput(self):
        self.gameData.myFlags.fSpacePressed = False
        self.gameData.myFlags.fLPMPressed = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.gameData.myFlags.fGameRun = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.gameData.myFlags.fSpacePressed = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.gameData.myFlags.fLPMPressed = True

    def playerActionsRead(self):
        self.readMousePos()
        self.readKeyboardInput()

    def updateCrosshairPosition(self):
        self.gameData.myPlayer.crosshair_xpos = self.mouse_xpos - 28
        self.gameData.myPlayer.crosshair_ypos = self.mouse_ypos - 28

    def randMouseAndCrosshairPos(self):
        self.mouse_xpos = random.randint(100, game_config.GAME_WINDOW_WIDTH - 100)
        self.mouse_ypos = random.randint(50, game_config.GAME_WINDOW_HEIGHT - 50)
        pygame.mouse.set_pos(self.mouse_xpos, self.mouse_ypos)

    def checkIfEnemyHit(self):
        if self.mouse_ypos < 233 and self.mouse_ypos > 199:
            if self.mouse_xpos < 547 and self.mouse_xpos > 519:
                if self.gameData.myFlags.fLPMPressed:
                    self.gameData.myFlags.fWin = True
        elif self.mouse_ypos < 242 and self.mouse_ypos > 232:
            if self.mouse_xpos < 542 and self.mouse_xpos > 524:
                if self.gameData.myFlags.fLPMPressed:
                    self.gameData.myFlags.fWin = True
        elif self.mouse_ypos < 291 and self.mouse_ypos > 241:
            if self.mouse_xpos < 569 and self.mouse_xpos > 498:
                if self.gameData.myFlags.fLPMPressed:
                    self.gameData.myFlags.fWin = True
        elif self.mouse_ypos < 322 and self.mouse_ypos > 290:
            if (self.mouse_xpos < 525 and self.mouse_xpos > 514) or (
                    self.mouse_xpos < 553 and self.mouse_xpos > 542):
                if self.gameData.myFlags.fLPMPressed:
                    self.gameData.myFlags.fWin = True

        if self.mouse_ypos < 233 and self.mouse_ypos > 199:
            if self.mouse_xpos < 547 and self.mouse_xpos > 519:
                if self.gameData.myFlags.fLPMPressed:
                    self.gameData.myFlags.fWin = True
        elif self.mouse_ypos < 242 and self.mouse_ypos > 232:
            if self.mouse_xpos < 542 and self.mouse_xpos > 524:
                if self.gameData.myFlags.fLPMPressed:
                    self.gameData.myFlags.fWin = True
        elif self.mouse_ypos < 291 and self.mouse_ypos > 241:
            if self.mouse_xpos < 569 and self.mouse_xpos > 498:
                if self.gameData.myFlags.fLPMPressed:
                    self.gameData.myFlags.fWin = True
        elif self.mouse_ypos < 322 and self.mouse_ypos > 290:
            if (self.mouse_xpos < 525 and self.mouse_xpos > 514) or (
                    self.mouse_xpos < 553 and self.mouse_xpos > 542):
                if self.gameData.myFlags.fLPMPressed:
                    self.gameData.myFlags.fWin = True

    def runGame(self):
        self.state = "IDLE"

        while self.gameData.myFlags.fGameRun:
            if self.state == "IDLE":
                self.playerActionsRead()

                if self.gameData.myFlags.fSpacePressed:
                    self.state = "WAITING"
                    self.gameStoper.start()
                    self.waitingTime = random.randint(6, 12)
                    self.gameData.myFlags.fWin = False
                    self.gameData.myFlags.fLose = False
                    self.gameData.myFlags.fGunInHand = False
                    self.gameData.myEnemy.setWaitPose()

                self.gameView.drawBackground()
                self.gameView.drawGround()
                self.gameView.drawEnemy(self.gameData.myEnemy, game_config.ENEMY_XPOS, game_config.ENEMY_YPOS)
                self.gameView.displayText("PRESS SPACE TO CONTINUE", 200, 500, 22, game_config.WHITE_COLOUR)
                if self.gameData.myFlags.fGunInHand:
                    self.gameView.drawPlayerGun(self.gameData.myPlayer.revolver, game_config.PLAYER_GUN_XPOS,
                                                game_config.PLAYER_GUN_YPOS)
                if self.gameData.myFlags.fWin:
                    self.gameView.displayText("YOU WIN!", 482, 150, 22, game_config.GREEN_COLOUR)
                elif self.gameData.myFlags.fLose:
                    self.gameView.displayText("YOU LOSE!", 476, 150, 22, game_config.RED_COLOUR)

            elif self.state == "WAITING":
                self.playerActionsRead()
                if self.gameData.myFlags.fSpacePressed:
                    self.gameData.myFlags.fGunInHand = True
                    self.state = "IDLE"
                    self.gameData.myFlags.fLose = True

                if self.gameStoper.read() > self.waitingTime:
                    self.state = "DUEL"
                    self.randMouseAndCrosshairPos()
                    pygame.mouse.set_pos(self.mouse_xpos, self.mouse_ypos)
                    self.gameView.playClockBellSound()
                    self.gameStoper.reset()

                self.gameView.drawBackground()
                self.gameView.drawGround()
                self.gameView.drawEnemy(self.gameData.myEnemy, game_config.ENEMY_XPOS, game_config.ENEMY_YPOS)

            elif self.state == "DUEL":
                self.playerActionsRead()
                if self.gameData.myFlags.fSpacePressed:
                    self.gameData.myFlags.fGunInHand = True
                if self.gameData.myFlags.fLPMPressed:
                    self.gameView.playGunShotSound()
                self.updateCrosshairPosition()
                self.checkIfEnemyHit()


                timeAfterBell = self.gameStoper.read()
                if timeAfterBell <= self.gameData.myEnemy.shotTime / 2.0:
                    self.gameData.myEnemy.setWaitPose()
                elif timeAfterBell <= self.gameData.myEnemy.shotTime:
                    self.gameData.myEnemy.setAttackPose()
                else:
                    self.gameData.myEnemy.setShotPose()
                    self.gameView.playGunShotSound()
                    self.gameData.myFlags.fLose = True

                if self.gameData.myFlags.fLose or self.gameData.myFlags.fWin:
                    self.state = "IDLE"

                self.gameView.drawBackground()
                self.gameView.drawGround()
                self.gameView.drawEnemy(self.gameData.myEnemy, game_config.ENEMY_XPOS, game_config.ENEMY_YPOS)
                if self.gameData.myFlags.fGunInHand:
                    self.gameView.drawPlayerGun(self.gameData.myPlayer.revolver, game_config.PLAYER_GUN_XPOS,
                                                game_config.PLAYER_GUN_YPOS)
                    self.gameView.drawCrosshair(self.gameData.myPlayer.crosshair, self.mouse_xpos - 28,
                                                self.mouse_ypos - 28)

            pygame.display.update()