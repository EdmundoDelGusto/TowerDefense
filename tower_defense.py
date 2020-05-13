
"""
Starting Template

Once you have learned how to use classes, you can begin your program with this
template.

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.starting_template
"""
import arcade
import numpy as np
from player import *
from map import *
from tower_class import *
from tower import *
from loader import *
from game_object import *


import time

SCREEN_WIDTH = 1920         # / 40 = 48
SCREEN_HEIGHT = 1080        # / 40 = 27
TILE_SIZE = 30
SCREEN_TITLE = "Tower Defense"

class MyGame(arcade.Window):
    """
    Main application class.

    NOTE: Go ahead and delete the methods you don't need.
    If you do need a method, delete the 'pass' and replace it
    with your own code. Don't leave 'pass' in this program.
    """
    PLAYER_WIDTH = 40
    PLAYER_HEIGHT = 40
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.AMAZON)
        joysticks = arcade.get_joysticks()
        self.loader = Loader("game_data.json")
        self.FPS = self.loader.fps

        self.set_update_rate(1 / self.FPS)
        self.player_count = len(joysticks)
        self.players = arcade.SpriteList()
        self.tile_size = TILE_SIZE
        self.map = Map(self, self.loader.map)
        self.tower_classes = [TowerClass(self, tower_class_data) for tower_class_data in self.loader.tower_classes]
        self.towers = arcade.SpriteList()

        """
        self.game_objects.append(
            GameObject(
                self, 500, 500,
                [
                    "resources/images/items/flagGreen1.png",
                    "resources/images/items/flagGreen2.png",
                ]
            )
        )
        self.game_objects[0].face_direction = GameObject.FACING_LEFT
        """

        if joysticks:
            for i in range(len(joysticks)):
                player_imgs = [
                                    "resources/tutorial/images/alien/alienBlue_front.png",
                                    "resources/tutorial/images/alien/alienBlue_jump.png"
                            ]
                player_sprite = Player(self, i, player_imgs)
                joysticks[i].open()
                #joysticks[i].on_joybutton_press = player_sprite.on_joybutton_press
                #joysticks[i].on_joybutton_release = player_sprite.on_joybutton_release
                joysticks[i].on_joyaxis_motion = player_sprite.on_joyaxis_motion
                self.players.append(player_sprite)
        else:
            print("There are no Joysticks")
            self.joystick = None
        # If you have sprite lists, you should create them here,
        # and set them to None

    def setup(self):
        self.towers.append(self.tower_classes[0].create_tower(self.players[0], 0, 600, 600))
        self.towers.append(self.tower_classes[0].create_tower(self.players[0], 0, 200, 800))
        self.towers.append(self.tower_classes[0].create_tower(self.players[0], 1, 550, 555))
        self.towers.append(self.tower_classes[0].create_tower(self.players[0], 1, 331, 222))
        self.map.setup()
        # Create your sprites and sprite lists here
        pass

    def on_draw(self):
        """
        Render the screen.
        """

        # This command should happen before we start drawing. It will clear
        # the screen to the background color, and erase what we drew last frame.
        arcade.start_render()

        self.map.draw()

        self.towers.draw()

        self.players.draw()
        # Call draw() on all your sprite lists below

    def on_update(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
        Normally, you'll call update() on the sprite lists that
        need it.
        """
        for player in self.players:
            player.update()

        for tower in self.towers:
            tower.update_animation(delta_time)

    def on_key_press(self, key, key_modifiers):
        if key == arcade.key.F:
            # User hits f. Flip between full and not full screen.
            self.set_fullscreen(not self.fullscreen)

            # Get the window coordinates. Match viewport to window coordinates
            # so there is a one-to-one mapping.
            width, height = self.get_size()
            self.set_viewport(0, width, 0, height)

        if key == arcade.key.S:
            # User hits s. Flip between full and not full screen.
            self.set_fullscreen(not self.fullscreen)

            # Instead of a one-to-one mapping, stretch/squash window to match the
            # constants. This does NOT respect aspect ratio. You'd need to
            # do a bit of math for that.
            self.set_viewport(0, SCREEN_WIDTH, 0, SCREEN_HEIGHT)
        pass

    def on_key_release(self, key, key_modifiers):
        """
        Called whenever the user lets off a previously pressed key.
        """
        pass

    def on_mouse_motion(self, x, y, delta_x, delta_y):
        """
        Called whenever the mouse moves.
        """
        pass

    def on_mouse_press(self, x, y, button, key_modifiers):
        print(x, y, button, key_modifiers)
        """
        Called when the user presses a mouse button.
        """
        pass

    def on_mouse_release(self, x, y, button, key_modifiers):
        """
        Called when a user releases a mouse button.
        """
        pass

    def get_scale(self, texture):
        assert isinstance(texture, arcade.Texture), "wrong type"
        max_dim = max(texture.width, texture.height)
        return self.tile_size/max_dim

def main():
    """ Main method """
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
