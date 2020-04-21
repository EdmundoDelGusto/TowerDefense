import numpy as np
import arcade
class Map:
    def __init__(self, game, file):
        self.game = game
        self.rows = int(self.game.height / self.game.tile_size)
        self.cols = int(self.game.width / self.game.tile_size)
        # row, col, (tile_type, tile_skin)
        self.map = np.zeros((self.rows, self.cols, 2))
        self.map[20][20] = 1
        print(self.rows)

    def draw(self):
        for row in range(len(self.map)):
            for col in range(len(self.map[row])):
                x = col * self.game.tile_size + self.game.tile_size / 2
                y = row * self.game.tile_size + self.game.tile_size / 2
                if self.is_buildable(row, col):
                    arcade.draw_rectangle_outline(x, y,
                                             self.game.tile_size, self.game.tile_size,
                                             arcade.color.AERO_BLUE)
                if self.is_way(row, col):
                    arcade.draw_rectangle_filled(x, y,
                                                 self.game.tile_size, self.game.tile_size,
                                                 arcade.color.LIGHT_GRAY)
        pass

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
