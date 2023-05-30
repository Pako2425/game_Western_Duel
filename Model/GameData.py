from Model.Colours import Colours
from Model.GameWindow import GameWindow
from Model.Enemy import Enemy
from Model.Player import Player
from Sounds import Sounds
from Model.Flags import Flags

import game_config

class GameData():
    def __init__(self):
        self.myEnemy = Enemy((game_config.ENEMY_XPOS, game_config.ENEMY_YPOS))
        self.myPlayer = Player()
        self.mySounds = Sounds()
        self.myFlags = Flags()
