import arcade
from game_object import *
from attack import *
from loader import *

class Tower(GameObject):
    """
    [{
        "idle": {
            "file_names": ["...", "..."],
            "update_rate": 30
        },
        "moving":{
            "file_names": ["...", "..."],
            "update_rate": 50
        }
    },
    {
        "idle": {
            "file_names": ["...", "..."],
            "update_rate": 30
        },
        "moving":{
            "file_names": ["...", "..."],
            "update_rate": 50
        }
    },
    ]
    """
    COUNT_STATE = 3

    # how many times you can upgrade towers
    COUNT_UPGRADE_LEVELS = 3

    STATE_IDLE = 0
    STATE_SHOOTING = 1
    STATE_DESTRUCTION = 2

    ATTACK_TYPE_NORMAL = 0
    ATTACK_TYPE_SPLASH = 1
    ATTACK_TYPE_SLOW = 2

    def __init__(self, game, player, x, y, loader, level_textures, level_update_rates):
        super().__init__(game, x, y)
        self.player = player
        self.level_textures = level_textures
        # since towers can upgrade, we have as many textures as levels
        #self.level_textures = [[[] for _ in range(self.COUNT_STATE)] for _ in range(self.COUNT_UPGRADE_LEVELS)]
        self.level_update_rates = level_update_rates
        self.state = self.STATE_IDLE
        self.face_direction = self.FACING_LEFT

        self.name = loader.name
        self.level_count = loader.level_count
        self.costs = loader.costs
        self.attacks = []

        for attack_data in loader.attacks:
            self.attacks.append(Attack(self, attack_data))

        self.level = 0  # start at level 0
        self.textures = self.level_textures[self.level]
        self.update_rates = self.level_update_rates[self.level]
        print(self.update_rates)

    def is_upgradable(self):
        return self.level < self.COUNT_UPGRADE_LEVELS - 1

    def upgrade(self):
        if self.is_upgradable():
            self.level += 1

            # update textures & update_rate
            self.textures = self.level_textures[self.level]
            self.update_rates = self.level_update_rates[self.level]
        else:
            raise ValueError("Tower is not upgradable")
