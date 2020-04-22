import arcade
from map import *
import datetime
from datetime import timedelta


class Player:

    def __init__(self, game, player_nr):
        self.game = game
        self.player_nr = player_nr
        self.x_movement = None
        self.y_movement = None
        self.movement_timer = datetime.datetime.now()
        self.movement_delay = timedelta(milliseconds=500)
        self.movement_delta = timedelta(milliseconds=450)
        self.x = (self.game.width / self.game.player_count) * player_nr + (self.game.width / (2 * self.game.player_count))
        self.y = self.game.height/2
        self.pos = (int(self.y / 40), int(self.x / 40))
        self.colors = [
            arcade.color.RED,
            arcade.color.BLUE,
            arcade.color.YELLOW,
            arcade.color.PURPLE,
        ]

    def update(self, delta_time):
        now = datetime.datetime.now()
        if now - self.movement_timer > self.movement_delay:
            if self.x_movement is not None:
                if self.x_movement is 'right':
                    self.move_right()
                if self.x_movement is 'left':
                    self.move_left()

            if self.y_movement is not None:
                if self.y_movement is 'up':
                    self.move_up()
                if self.y_movement is 'down':
                    self.move_down()
            self.movement_timer = now - self.movement_delta

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
        if self.x_movement is None and self.y_movement is None and int(value) != 0:
            self.movement_timer = datetime.datetime.now()

        if axis == 'x':
            if value == 1.0:
                self.x_movement = 'right'
                #self.movement_timer = datetime.datetime.now()
                self.move_right()
            elif value == -1.0:
                self.x_movement = 'left'
                #self.movement_timer = datetime.datetime.now()
                self.move_left()
            else:
                self.x_movement = None
        elif axis == 'y':
            if value == 1.0:
                self.y_movement = 'down'
                #self.movement_timer = datetime.datetime.now()
                self.move_down()
            elif value == -1.0:
                self.y_movement = 'up'
                #self.movement_timer = datetime.datetime.now()
                self.move_up()
            else:
                self.y_movement = None


    def move_right(self):
        if self.game.map.in_map_boundaries(self.pos[0], self.pos[1] + 1):
            self.pos = (self.pos[0], self.pos[1] + 1)
            self.update_coordinates()

    def move_left(self):
        if self.game.map.in_map_boundaries(self.pos[0], self.pos[1] - 1):
            self.pos = (self.pos[0], self.pos[1] + -1)
            self.update_coordinates()

    def move_up(self):
        if self.game.map.in_map_boundaries(self.pos[0] + 1, self.pos[1]):
            self.pos = (self.pos[0] + 1, self.pos[1])
            self.update_coordinates()

    def move_down(self):
        if self.game.map.in_map_boundaries(self.pos[0] - 1, self.pos[1]):
            self.pos = (self.pos[0] - 1, self.pos[1])
            self.update_coordinates()

    def draw(self):
        arcade.draw_rectangle_outline(self.x, self.y,
                                     self.game.tile_size, self.game.tile_size,
                                     self.colors[self.player_nr])
