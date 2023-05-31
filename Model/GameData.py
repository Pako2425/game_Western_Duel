from Model.GameWindow import GameWindow
from Model.Enemy import Enemy
from Model.Player import Player
from Model.Flags import Flags

from Model import game_config

class GameData():
    def __init__(self):
        self.myEnemy = Enemy(game_config.ENEMY_XPOS, game_config.ENEMY_YPOS, 1.3)
        self.myPlayer = Player()
        self.myFlags = Flags()
