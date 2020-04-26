import arcade
from game_object import *

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


    def __init__(self, game, x, y, textures):
        super().__init__(game, x, y)


        # since towers can upgrade, we have as many textures as levels
        self.level_textures = [[[] for _ in range(self.COUNT_STATE)] for _ in range(self.COUNT_UPGRADE_LEVELS)] #[[[], [], []], [[], [], []], [[], [], []]]
        self.level_update_rates = [[None] * self.COUNT_STATE] * self.COUNT_UPGRADE_LEVELS
        self.state = self.STATE_IDLE
        self.face_direction = self.FACING_LEFT
        print(self.level_textures)
        if not isinstance(textures, list) and len(textures) == self.COUNT_UPGRADE_LEVELS:
            raise ValueError("texture is not correctly formatted. Needs to be list of {} dictionaries".format(self.COUNT_UPGRADE_LEVELS))

        for lvl in range(len(textures)):
            for key, state in [("idle", self.STATE_IDLE), ("shooting", self.STATE_SHOOTING), ("destruction", self.STATE_DESTRUCTION)]:
                if key not in textures[lvl]:
                    raise ValueError("texture not correctly formatted. Index {} has no '{}' textures given".format(lvl, key))

                if "file_names" not in textures[lvl][key] or not isinstance(textures[lvl][key]["file_names"], list) or len(textures[lvl][key]["file_names"]) == 0:
                    raise ValueError("texture dict not correctly formatted. (Index: {}) '{}' has no non-empty 'file_names' array".format(lvl, key))

                if "update_rate" not in textures[lvl][key]:
                    raise ValueError("texture dict not correctly formatted. (Index: {}) '{}' has no 'update_rate'".format(lvl, key))

                for file_name in textures[lvl][key]["file_names"]:
                    if self.level_textures[lvl][state] is None:
                        self.level_textures[lvl][state] = []
                    #print(len(self.level_textures[lvl][state]))
                    self.level_textures[lvl][state].append(self.load_texture_pair(file_name))

                self.level_update_rates[lvl][state] = textures[lvl][key]["update_rate"]
                #print(self.level_textures)

        self.level = 0  # start at level 0

        self.textures = self.level_textures[self.level]
        print(self.level_textures)
        self.update_rates = self.level_update_rates[self.level]

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
