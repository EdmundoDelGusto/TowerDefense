import arcade

class GameObject(arcade.Sprite):
    FACING_RIGHT = 0
    FACING_LEFT = 1

    def __init__(self, game,  x, y):
        super().__init__()

        self.game = game
        self.center_x = x
        self.center_y = y

        """
        textures should be a list where each element represents a state and is a list of the state-animation.
        Example:
        [
            [(tex_0_1, tex_0_1_mirrored), (tex_0_2, tex_0_2_mirrored), ...],    # for state = 0 (could be idle-state)
            [(tex_1_1, tex_1_1_mirrored), (tex_1_2, tex_1_2_mirrored), ...],    # for state = 1 (could be moving-state)
        ]
        """
        self.textures = None

        """
        update_rate should be a list where each element represents the update_rate of a state
        Example:
        [
            30,
            20
        ]
        """
        self.update_rates = None
        self.face_direction = None
        self.state = None

        self.scale = 1* self.game.tile_size / 128

        self.frame_count_texture = 0

        self.validated = False

    def update_animation(self, delta_time: float = 1/60):
        self.validate()

        self.frame_count_texture += 1
        if self.frame_count_texture // self.update_rates[self.state] > (len(self.textures[self.state]) - 1):
            self.frame_count_texture = 0
        self.texture = self.textures[self.state][self.frame_count_texture // self.update_rates[self.state]][self.face_direction]

    def load_texture_pair(self, file_name, name=""):
        return (arcade.load_texture(file_name), arcade.load_texture(file_name, mirrored=True))


    def update_state(self, state):
        if self.state != state:
            self.state = state
            # restart animation if state changes
            self.current_texture = 0

    def validate(self):
        if self.validated:
            return

        if self.textures is None:
            raise NotImplementedError("No textures set.")
        if self.update_rates is None:
            raise NotImplementedError("No update_rates set.")
        if self.face_direction is None:
            raise NotImplementedError("No face_direction set.")
        if self.state is None:
            raise NotImplementedError("No state set.")

        self.validated = True
