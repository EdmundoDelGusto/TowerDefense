import arcade
from map import *
from tower_defense import*

LEFT = -1.0
RIGHT = 1.0
DOWN = 1.0
UP = -1.0
MOVEMENT_SPEED = 40

class Player(arcade.Sprite):

    def __init__(self, game, player_nr, textures):
        super().__init__()

        self.up_pressed = False
        self.down_pressed = False
        self.right_pressed = False
        self.left_pressed = False
        self.game = game
        self.player_nr = player_nr
        self.center_x = 300
        self.center_y = 300
        self.change_x = 0
        self.center_y = 0
        self.textures = []
        for texture in textures:
            self.textures.append(arcade.load_texture(texture))
        self.texture = self.textures[0]
        self.scale = self.game.get_scale(self.texture)
        self.framecount = 0
        self.movement_action = False
        self.diagonal = 1


    def on_joyaxis_motion(self, joystick, axis, value):
        print("Cross ({}, {})".format(axis, value))
        if axis == 'x':
            if value == RIGHT:
                self.right_pressed = True
                if not self.up_pressed and not self.down_pressed:
                    self.movement_action = True
            elif value == LEFT:
                self.left_pressed = True
                if not self.up_pressed and not self.down_pressed:
                    self.movement_action = True
            else:
                self.right_pressed = False
                self.left_pressed = False
                self.change_x = 0
                if not self.up_pressed and not self.down_pressed:
                    self.framecount = 0
        elif axis == 'y':
            if value == RIGHT:
                self.down_pressed = True
                if not self.right_pressed and not self.left_pressed:
                    self.movement_action = True
            elif value == LEFT:
                self.up_pressed = True
                if not self.right_pressed and not self.left_pressed:
                    self.movement_action = True
            else:
                self.down_pressed = False
                self.up_pressed = False
                self.change_y = 0
                if not self.right_pressed and not self.left_pressed:
                    self.framecount = 0

    def movement(self):
        if self.right_pressed and not self.left_pressed:
            self.change_x = MOVEMENT_SPEED
        if self.left_pressed and not self.right_pressed:
            self.change_x = -MOVEMENT_SPEED
        if self.up_pressed and not self.down_pressed:
            self.change_y = MOVEMENT_SPEED
        if self.down_pressed and not self.up_pressed:
            self.change_y = -MOVEMENT_SPEED
        if (self.right_pressed or self.left_pressed) and (self.up_pressed or self.down_pressed):
            self.diagonal = 1.5
        else:
            self.diagonal = 1

    def update(self):
        self.movement()
        if self.movement_action:
            self.center_x += self.change_x
            self.center_y += self.change_y
            self.movement_action = False
            self.framecount = 0

        if self.framecount >= 30:
            self.center_x += self.change_x
            self.center_y += self.change_y
            self.framecount -= 2 * self.diagonal

        if self.left < 0:
            self.left = 0
        elif self.right > SCREEN_WIDTH - 1:
            self.right = SCREEN_WIDTH - 1

        if self.bottom < 0:
            self.bottom = 0
        elif self.top > SCREEN_HEIGHT - 1:
            self.top = SCREEN_HEIGHT - 1

        self.center_x, self.center_y = self.game.map.get_position(
                                                self.game.map.get_col(self.center_x),
                                                self.game.map.get_row(self.center_y)
                                                )
        self.framecount += 1
