import pygame
from pygame import mixer
import time
import random
import threading

from Model import GameData

pygame.init()

#------------INTERFACE------------#
class Interface():
    ground_level = 300
    #win = pygame.display.set_mode((myGameWindow.win_width, myGameWindow.win_height))
    win = pygame.display.set_mode((GameData.GAME_WINDOW_WIDTH, GameData.GAME_WINDOW_HEIGHT))
    font = pygame.font.SysFont('arial', 20)

    def displayText(self, text, xpos, ypos, size, colour):
        self.font = pygame.font.SysFont('arial', size)
        textForDisplay = self.font.render(text, True, colour)
        self.win.blit(textForDisplay, (xpos, ypos))

    def drawBackground(self):
        self.win.fill(myColours.blue)

    def drawGround(self):
        pygame.draw.rect(self.win, myColours.ground, (0, self.ground_level, myGameWindow.win_width, myGameWindow.win_height - self.ground_level))

    def showEnemy(self, enemy):
        self.win.blit(enemy, (myEnemy.xpos_enemy, myEnemy.ypos_enemy))

    def showCrosshair(self):
        self.win.blit(myPlayer.crosshair, (myPlayer.xpos_crosshair, myPlayer.ypos_crosshair))

    def showGun(self):
        self.win.blit(myPlayer.rewolwer, (724, 470))

    def playStartSound(self):
        mySounds.sound_clock_bell.play()

    def playGunShotSound(self):
        mySounds.sound_gun_shot.play()


myInterface = Interface()


#------------CONTROLLER-----------#



class Stoper():
    startTime = 0
    measureTime = 0
    def start(self):
        self.startTime = time.time()
        self.measureTime = 0

    def read(self):
        self.measureTime = time.time() - self.startTime


myStoper = Stoper()


def playerActionsRead():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            myFlags.fQuite = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                myFlags.fPressSpace = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                myFlags.fPressLPM = True

def readMousePos():
    myPlayer.xpos_mouse, myPlayer.ypos_mouse = pygame.mouse.get_pos()

def updateCrosshair():
    myPlayer.xpos_crosshair = myPlayer.xpos_mouse - 28
    myPlayer.ypos_crosshair = myPlayer.ypos_mouse - 28

def randMouseAndCrosshairPos():
    myPlayer.dxpos_mouse = random.randint(0 + 100, myGameWindow.win_width - 100)
    myPlayer.dypos_mouse = random.randint(0 + 50, myGameWindow.win_height - 50)
    pygame.mouse.set_pos(myPlayer.dxpos_mouse, myPlayer.dypos_mouse)

def checkEnemyHit():
    if myPlayer.ypos_mouse < 233 and myPlayer.ypos_mouse > 199:
        if myPlayer.xpos_mouse < 547 and myPlayer.xpos_mouse > 519:
            if myFlags.fFire:
                myFlags.fWin = True
    elif myPlayer.ypos_mouse < 242 and myPlayer.ypos_mouse > 232:
        if myPlayer.xpos_mouse < 542 and myPlayer.xpos_mouse > 524:
            if myFlags.fFire:
                myFlags.fWin = True
    elif myPlayer.ypos_mouse < 291 and myPlayer.ypos_mouse > 241:
        if myPlayer.xpos_mouse < 569 and myPlayer.xpos_mouse > 498:
            if myFlags.fFire:
                myFlags.fWin = True
    elif myPlayer.ypos_mouse < 322 and myPlayer.ypos_mouse > 290:
        if (myPlayer.xpos_mouse < 525 and myPlayer.xpos_mouse > 514) or (myPlayer.xpos_mouse < 553 and myPlayer.xpos_mouse > 542):
            if myFlags.fFire:
                myFlags.fWin = True

delay = 0
state = 4
pygame.mouse.set_visible(False)
myFlags.fDuelStop = True
while(myFlags.fGameRun):
    if state == 0:
        delay = random.randint(4, 8)
        myStoper.start()
        myEnemy.enemyCowboy = myEnemy.enemyWait
        myFlags.fDuelStart = True
        myFlags.fLose = False
        myFlags.fWin = False
        myFlags.fGunInHand = False
        state = 1
    elif state == 1:
        myFlags.fPressLPM = False
        myFlags.fPressSpace = False
        playerActionsRead()
        myInterface.drawBackground()
        myInterface.drawGround()
        myInterface.showEnemy(myEnemy.enemyCowboy)
        if myFlags.fPressSpace:
            myFlags.fGunInHand = True
        myStoper.read()
        if myStoper.measureTime > delay:
            myInterface.playStartSound()
            state = 2
        else:
            if myFlags.fGunInHand:
                myFlags.fLose = True
                myInterface.showGun()
                myFlags.fDuelStop = True
                state = 4
    elif state == 2:
        randMouseAndCrosshairPos()
        myInterface.playStartSound()
        myInterface.drawBackground()
        myInterface.drawGround()
        myInterface.showEnemy(myEnemy.enemyWait)
        myStoper.start()
        state = 3
    elif state == 3:
        myFlags.fPressLPM = False
        myFlags.fPressSpace = False
        myFlags.fFire = False
        playerActionsRead()
        if myFlags.fPressSpace:
            myFlags.fGunInHand = ~myFlags.fGunInHand
        if myFlags.fPressLPM:
            myFlags.fFire = True
        readMousePos()
        updateCrosshair()
        checkEnemyHit()
        myInterface.drawBackground()
        myInterface.drawGround()
        myStoper.read()
        if myStoper.measureTime < (myEnemy.shotTime / 2):
            myEnemy.enemyCowboy = myEnemy.enemyWait
            myInterface.showEnemy(myEnemy.enemyCowboy)
        elif myStoper.measureTime <= myEnemy.shotTime:
            myEnemy.enemyCowboy = myEnemy.enemyAttack
            myInterface.showEnemy(myEnemy.enemyCowboy)
        elif myStoper.measureTime > myEnemy.shotTime:
            myFlags.fLose = True
            myInterface.playGunShotSound()
            myEnemy.enemyCowboy = myEnemy.enemyShot
            myInterface.showEnemy(myEnemy.enemyCowboy)
        if myFlags.fGunInHand:
            myInterface.showGun()
            myInterface.showCrosshair()
            if myFlags.fFire:
                myInterface.playGunShotSound()
        if (myFlags.fWin or myFlags.fLose):
            myFlags.fDuelStop = True
            state = 4
    elif state == 4:
        myFlags.fPressSpace = False
        myFlags.fPressLPM = False
        playerActionsRead()
        myInterface.drawBackground()
        myInterface.drawGround()
        myInterface.showEnemy(myEnemy.enemyCowboy)
        if myFlags.fGunInHand:
            myInterface.showGun()
        if myFlags.fWin:
            myInterface.showCrosshair()
            myInterface.displayText("YOU WIN!", 482, 150, 22, myColours.green)
        elif myFlags.fLose:
            myInterface.displayText("YOU LOSE!", 476, 150, 22, myColours.red)
        if myFlags.fDuelStop:
            myInterface.displayText("Press SPACE to continue", 400, 600, 30, myColours.red)
        if myFlags.fPressSpace:
            state = 0

    if myFlags.fQuite:
        myFlags.fGameRun = False

    pygame.display.update()
