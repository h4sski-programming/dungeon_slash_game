import pygame

from settings import Settings_player
from character import Character

settings_player = Settings_player()

class Player(Character):
    def __init__(self, x, y):
        self.width = 20
        self.height = self.width
        # Call the __init__ method of the parent class (Sprite)
        super().__init__(x = x - self.width//2, y = y - self.height//2,
                         move_speed = settings_player.move_speed,
                         hp = 1, colour = (255, 100, 100),
                         width = 20, height = 20)
        self.score = 0
        self.exp = 0
        self.previous_level_exp = 0
        self.next_level_exp = 2
        self.next_level_exp_multiplicator = 2
        self.level = 0
        self.fire_rate = 1
        self.fire_range = 300
        self.bullet_move_speed = 200
        self.bullet_aoe = 20
        self.bullet_dmg = 2
        
    
    def get_dmg(self, dmg, time):
        super().get_dmg(dmg)
        # if 
        
        
    def draw(self, surface):
        self.draw_rect(surface=surface)
    
    
    def update(self):
        if self.exp >= self.next_level_exp:
            self.previous_level_exp = self.next_level_exp
            self.next_level_exp *= self.next_level_exp_multiplicator
            self.level += 1
            print(f'Level up')
            return True
        
        if self.hp <= 0:
            print(f'game over')
            self.alive = False
    
    