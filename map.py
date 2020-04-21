import numpy as np
class Map:
    def __init__(self, game, file):
        self.game = game
        self.rows = int(self.game.height / self.game.tile_size)
        self.cols = int(self.game.width / self.game.tile_size)
        self.map = np.zeros((self.rows, self.cols))

    def draw(self):
        pass
