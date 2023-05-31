from Model import game_config
from Model import GameData
from View import GameView
import Stoper

class GameController():
    def __init__(self):
        self.gameData = GameData.GameData()
        self.gameView = GameView.GameView()
        self.gameStoper = Stoper.Stoper()

        self.mouse_xpos = 0
        self.mouse_ypos = 0
        self.mouse_dxpos = 0
        self.mouse_dypos = 0




    def playerActionsRead(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.gameData.myFlags.fQuite = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.gameData.myFlags.fPressSpace = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.gameData.myFlags.fPressLPM = True

    def readMousePos(self):
        self.mouse_xpos, self.mouse_ypos = pygame.mouse.get_pos()

    def updateCrosshair(self):
        self.gameData.myPlayer.crosshair_xpos = self.mouse_xpos - 28
        self.gameData.myPlayer.crosshair_ypos = self.mouse_ypos - 28

    def randMouseAndCrosshairPos(self):
        self.mouse_dxpos = random.randint(0 + 100, game_config.GAME_WINDOW_WIDTH - 100)
        self.mouse_dypos = random.randint(0 + 50, myGameWindow.win_height - 50)
        pygame.mouse.set_pos(myPlayer.dxpos_mouse, myPlayer.dypos_mouse)

    def checkEnemyHit(self):
        if self.mouse_ypos < 233 and self.mouse_ypos > 199:
            if self.mouse_xpos < 547 and self.mouse_xpos > 519:
                if self.gameData.myFlags.fFire:
                    self.gameData.myFlags.fWin = True
        elif self.mouse_ypos < 242 and self.mouse_ypos > 232:
            if self.mouse_xpos < 542 and self.mouse_xpos > 524:
                if self.gameData.myFlags.fFire:
                    self.gameData.myFlags.fWin = True
        elif self.mouse_ypos < 291 and self.mouse_ypos > 241:
            if self.mouse_xpos < 569 and self.mouse_xpos > 498:
                if self.gameData.myFlags.fFire:
                    self.gameData.myFlags.fWin = True
        elif self.mouse_ypos < 322 and self.mouse_ypos > 290:
            if (self.mouse_xpos < 525 and self.mouse_xpos > 514) or (
                    self.mouse_xpos < 553 and self.mouse_xpos > 542):
                if self.gameData.myFlags.fFire:
                    self.gameData.myFlags.fWin = True

    def gameRun(self):
        pygame.init()
        delay = 0
        state = 4
        pygame.mouse.set_visible(False)
        myFlags.fDuelStop = True

        state1 = "IDLE"
        state2 = "WAITING"
        state3 = "DUEL"

        while (gameData.myFlags.fGameRun):
            
            pygame.display.update()