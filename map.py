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
            for col in range(len(lines[row])):
                if col != len(lines[row]) -1:
                    self.map[row][col][0] = int(lines[row][col])

    def setup(self):
        self.dirt_list = arcade.SpriteList()
        self.stone_list = arcade.SpriteList()
        self.water_list = arcade.SpriteList()
        self.way_list = arcade.SpriteList()

        for row in range(len(self.map)):
            for col in range(len(self.map[row])):
                x = col * self.game.tile_size + self.game.tile_size / 2
                y = row * self.game.tile_size + self.game.tile_size / 2
                if self.is_buildable(row, col):
                    dirt = arcade.Sprite("resources/images/tiles/dirt_center.png", self.tile_scaling_factor)
                    dirt.center_x = x
                    dirt.center_y = y
                    self.dirt_list.append(dirt)
                elif self.is_way(row, col):
                    way = arcade.Sprite("resources/images/tiles/stone_center.png", self.tile_scaling_factor)
                    way.center_x = x
                    way.center_y = y
                    self.way_list.append(way)
                elif self.is_obstacle(row, col):
                    way = arcade.Sprite("resources/images/tiles/water.png", self.tile_scaling_factor)
                    way.center_x = x
                    way.center_y = y
                    self.water_list.append(way)


    def draw(self):
        self.dirt_list.draw()
        self.stone_list.draw()
        self.water_list.draw()
        self.way_list.draw()

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

    def get_rectangle_points(self, row, col):
        x = col * self.game.tile_size + self.game.tile_size / 2
        y = row * self.game.tile_size + self.game.tile_size / 2
        half_square_size = self.game.tile_size / 2

        top_left = (x - half_square_size, y + half_square_size)
        top_right = (x + half_square_size, y + half_square_size)
        bottom_right = (x + half_square_size, y - half_square_size)
        bottom_left = (x - half_square_size, y - half_square_size)

        return (top_left, top_right, bottom_right, bottom_left)
