from loader import *
from tower import *

import arcade
class TowerClass:
    def __init__(self, game, tower_class_data):
        self.name = tower_class_data["name"]
        self.game = game
        self.info_text = tower_class_data["info_text"]
        self.towers_preview = []
        self.tower_loaders = []
        self.tower_textures = []

        self.idle_textures = {}
        self.shooting_textures = {}
        self.destruction_textures = {}
        self.all_textures = {}

        self.idle_update_rates = {}
        self.shooting_update_rates = {}
        self.destruction_update_rates = {}
        self.all_update_rates = {}

        for id in range(len(tower_class_data["towers"])):
            file_name = tower_class_data["towers"][id]
            loader = Loader(file_name)
            self.tower_loaders.append(loader)
            tower_preview = {
                "id": id,
                "name": loader.name,
                "costs": loader.costs,
                "texture": arcade.load_texture(loader.idle_textures[0][0])
            }
            self.towers_preview.append(tower_preview)

            self.idle_textures[id] = {}
            self.shooting_textures[id] = {}
            self.destruction_textures[id] = {}
            self.all_textures[id] = [[] for _ in range(3)]
            self.all_update_rates[id] = [loader.idle_update_rates, loader.shooting_update_rates, loader.destruction_update_rates]

            for lvl in range(len(loader.idle_textures)):
                self.idle_textures[id][lvl] = [(arcade.load_texture(file_name), arcade.load_texture(file_name, mirrored=True)) for file_name in loader.idle_textures[lvl]]
                self.shooting_textures[id][lvl] = [(arcade.load_texture(file_name), arcade.load_texture(file_name, mirrored=True)) for file_name in loader.shooting_textures[lvl]]
                self.destruction_textures[id][lvl] = [(arcade.load_texture(file_name), arcade.load_texture(file_name, mirrored=True)) for file_name in loader.destruction_textures[lvl]]

            self.all_textures[id][Tower.STATE_IDLE] = self.idle_textures[id]
            self.all_textures[id][Tower.STATE_SHOOTING] = self.shooting_textures[id]
            self.all_textures[id][Tower.STATE_DESTRUCTION] = self.destruction_textures[id]

    def get_available_towers(self):
        return self.towers_preview

    def create_tower(self, player, id, x, y):
        return Tower(self.game, player, x, y, self.tower_loaders[id], self.all_textures[id], self.all_update_rates[id])

