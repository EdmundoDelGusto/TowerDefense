import numpy as np
import arcade
class Map:
    def __init__(self, game, file):
        self.game = game
        self.rows = int(self.game.height / self.game.tile_size)
        self.cols = int(self.game.width / self.game.tile_size)

        self.tile_scaling_factor = self.game.tile_size / 128

        # row, col, (tile_type, tile_skin)
        file = open(file)
        lines = file.readlines()
        self.map = np.zeros((self.rows, self.cols, 2))
        for row in range(len(lines)):
            for col in range(len(lines[row])-1): # ignore  \n
                self.map[row][col][0] = int(lines[row][col])

    def setup(self):
        self.map_sprites = arcade.SpriteList()

        for row in range(len(self.map)):
            for col in range(len(self.map[row])):
                x = col * self.game.tile_size + self.game.tile_size / 2
                y = row * self.game.tile_size + self.game.tile_size / 2
                if self.is_buildable(row, col):
                    sprite = arcade.Sprite("resources/images/tiles/dirt_center.png", self.tile_scaling_factor)
                elif self.is_way(row, col):
                    sprite = arcade.Sprite("resources/images/tiles/stone_center.png", self.tile_scaling_factor)
                elif self.is_obstacle(row, col):
                    sprite = arcade.Sprite("resources/images/tiles/water.png", self.tile_scaling_factor)
                sprite.center_x = x
                sprite.center_y = y
                self.map_sprites.append(sprite)


    def draw(self):
        self.map_sprites.draw()

    def in_map_boundaries(self, row, col):
        return row >= 0 and row < self.rows and col >= 0 and col < self.cols

    def is_buildable(self, row, col):
        if self.in_map_boundaries(row, col):
            return self.map[row][col][0] == 0

    def is_way(self, row, col):
        if self.in_map_boundaries(row, col):
            return self.map[row][col][0] == 1
        return False

    def is_obstacle(self, row, col):
        if self.in_map_boundaries(row, col):
            return self.map[row][col][0] == 2
        return False

    def get_row(self, y):
        if y > self.game.height or y < 0:
            raise ValueError("y out of bounds")
        return y // self.game.tile_size

    def get_col(self, x):
        if x > self.game.width or x< 0:
            raise ValueError("x out of bounds")
        return x // self.game.tile_size

    def get_position(self, col, row):
        """
            returns (x, y) tuple of tile center

            NOTE: Use *my_sprite_class*.center_x, *my_sprite_class*.center_y if possible
        """
        if col > self.cols - 1:
            raise ValueError("col out of bounds")
        if row > self.rows - 1:
            raise ValueError("row out of bounds")
        x = col * self.game.tile_size + self.game.tile_size // 2
        y = row * self.game.tile_size + self.game.tile_size // 2
        return x, y
