
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

SCREEN_WIDTH = 1920         # / 40 = 48
SCREEN_HEIGHT = 1080        # / 40 = 27
TILE_SIZE = 40
PLAYER_WIDTH = 40
PLAYER_HEIGHT = 40
SCREEN_TITLE = "Starting Template"

class MyGame(arcade.Window):
    """
    Main application class.

    NOTE: Go ahead and delete the methods you don't need.
    If you do need a method, delete the 'pass' and replace it
    with your own code. Don't leave 'pass' in this program.
    """

    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.AMAZON)
        joysticks = arcade.get_joysticks()
        self.player_count = len(joysticks)
        self.tile_size = TILE_SIZE
        self.map = Map(self, "")
        self.players = []
        if joysticks:
            for i in range(len(joysticks)):
                player = Player(self, i)
                joysticks[i].open()
                joysticks[i].on_joybutton_press = player.on_joybutton_press
                joysticks[i].on_joybutton_release = player.on_joybutton_release
                joysticks[i].on_joyaxis_motion = player.on_joyaxis_motion
                self.players.append(player)
        else:
            print("There are no Joysticks")
            self.joystick = None
        # If you have sprite lists, you should create them here,
        # and set them to None

    def setup(self):
        # Create your sprites and sprite lists herea
        #
        pass

    def on_draw(self):
        """
        Render the screen.
        """

        # This command should happen before we start drawing. It will clear
        # the screen to the background color, and erase what we drew last frame.
        arcade.start_render()

        for player in self.players:
            player.draw()
        # Call draw() on all your sprite lists below

    def on_update(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
        Normally, you'll call update() on the sprite lists that
        need it.
        """
        self.players[0].x += 0.1
        pass

    def on_key_press(self, key, key_modifiers):
        print(key)
        """
        Called whenever a key on the keyboard is pressed.

        For a full list of keys, see:
        http://arcade.academy/arcade.key.html
        """
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

def main():
    """ Main method """
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
