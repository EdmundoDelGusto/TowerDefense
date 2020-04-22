import arcade
from map import *


class Player:

    def __init__(self, game, player_nr):
        self.game = game
        self.player_nr = player_nr
        self.x = (self.game.width / self.game.player_count) * player_nr + (self.game.width / (2 * self.game.player_count))
        self.y = self.game.height/2
        self.pos = (int(self.y / 40), int(self.x / 40))
        self.colors = [
            arcade.color.RED,
            arcade.color.BLUE,
            arcade.color.YELLOW,
            arcade.color.PURPLE,
        ]

    def update_coordinates(self):
        self.x = 20 + self.pos[1] * 40
        self.y = 20 + self.pos[0] * 40

    def on_joybutton_press(self, _joystick, button):
        print('on_joybutton_press')
        print(self.player_nr, button)

    def on_joybutton_release(self, _joystick, button):
        print('on_joybutton_release')
        print("Button {} up".format(button))

    def on_joyaxis_motion(self, _joystick, axis, value):
        print("Cross ({}, {})".format(axis, value), self.player_nr)
        update = False
        if axis == 'x':
            if value == 1.0:
                new_pos = (self.pos[0], self.pos[1] + 1)
                update = True
            elif value == -1.0:
                new_pos = (self.pos[0], self.pos[1] - 1)
                update = True
        elif axis == 'y':
            if value == 1.0:
                new_pos = (self.pos[0] - 1, self.pos[1])
                update = True
            elif value == -1.0:
                new_pos = (self.pos[0] + 1, self.pos[1])
                update = True
        if update and self.game.map.in_map_boundaries(new_pos[0], new_pos[1]):
            self.pos = new_pos
            self.update_coordinates()

    def draw(self):
        arcade.draw_rectangle_filled(self.x, self.y,
                                     self.game.tile_size, self.game.tile_size,
                                     self.colors[self.player_nr])
