import pygame
from pygame import mixer
import time
import random
import threading

from Model import GameData
from View import GameView

pygame.init()
delay = 0
state = 4
pygame.mouse.set_visible(False)
myFlags.fDuelStop = True

state1 = "IDLE"
state2 = "WAITING"
state3 = "DUEL"

while(myFlags.fGameRun):


    pygame.display.update()


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
