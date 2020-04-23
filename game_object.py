import arcade




class GameObject(arcade.Sprite):
    FACING_RIGHT = 0
    FACING_LEFT = 1

    STATE_IDLE = 0
    STATE_MOVE = 1

    def __init__(self, game,  x, y, idle_textures=[], update_rate=30):
        super().__init__()

        self.game = game
        self.center_x = x
        self.center_y = y

        self.update_rate = update_rate

        self.scale = self.game.tile_size / 128
        self.state = GameObject.STATE_IDLE
        self.face_direction = GameObject.FACING_RIGHT

        self.idle_textures = []
        self.idle_textures_mirrored = []

        self.current_idle_texture = 0

        for texture in idle_textures:
            self.idle_textures.append(arcade.load_texture(texture))
            self.idle_textures_mirrored.append(arcade.load_texture(texture, mirrored=True))
        self.texture = self.idle_textures[0]

    def update_animation(self, delta_time: float = 1/60):
        if self.state == GameObject.STATE_IDLE:
            self.current_idle_texture += 1
            if self.current_idle_texture // self.update_rate > (len(self.idle_textures) - 1):
                self.current_idle_texture = 0
            if self.face_direction == GameObject.FACING_RIGHT:
                self.texture = self.idle_textures[self.current_idle_texture // self.update_rate]
            else:
                self.texture = self.idle_textures_mirrored[self.current_idle_texture // self.update_rate]
