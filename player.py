import arcade
class Player:

    def __init__(self, game, player_nr):
        self.game = game
        self.player_nr = player_nr
        self.x = (self.game.width / self.game.player_count) * player_nr + (
                self.game.width / (2 * self.game.player_count))
        self.y = self.game.height / 2

        self.colors = [
            arcade.color.RED,
            arcade.color.BLUE,
            arcade.color.YELLOW,
            arcade.color.PURPLE,
        ]

    def on_joybutton_press(self, _joystick, button):
        print(self.player_nr, button)

    def on_joybutton_release(self, _joystick, button):
        print("Button {} up".format(button))

    def on_joyaxis_motion(self, _joystick, axis, value):
        print("Cross ({}, {})".format(axis, value), _joystick)

    def draw(self):
        arcade.draw_rectangle_filled(self.x, self.y,
                                     self.game.tile_size, self.game.tile_size,
                                     self.colors[self.player_nr])
