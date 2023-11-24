class Settings_dungeon_slach_game():
    def __init__(self):
        self.WIDTH = 1200
        self.HEIGHT = 900
        self.resolution = (self.WIDTH, self.HEIGHT)
        self.title = 'Dungeon slash game'
        self.DPS = 60
        
        self.score_surface_height = 50
        self.score_surface_text_margin = 10
        self.score_surface_text_font_size = int(self.score_surface_height - self.score_surface_text_margin / 1.5)
        self.player_level_surface_text_margin_x = 250
        self.player_hp_surface_text_margin_x = 500
        self.player_exp_surface_text_margin_x = 750
        self.player_exp_bar_height = self.score_surface_text_margin // 1.2


class Settings_player():
    def __init__(self):
      self.move_speed = 100
      self.bollet_speed = 20