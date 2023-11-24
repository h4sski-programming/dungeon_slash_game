import pygame
import random

from settings import Settings_dungeon_slach_game
from character import Character


settings = Settings_dungeon_slach_game()


def generate_enemy(player_level):
    enemy_type = random.randint(0, player_level)
    enemy = 0
    if enemy_type >= 3:
        enemy = Enemy_C()
    elif enemy_type == 2:
        enemy = Enemy_B()
    else:
        enemy = Enemy_A()
    return enemy


class Enemy_global(Character):
    def __init__(self, x, y, move_speed, hp, colour=(100, 100, 255),
                 exp_value=1):
        super().__init__(x=x, y=y, move_speed=move_speed, 
                         hp=hp, colour=colour, 
                         width=10, height=10)
        self.exp_value = exp_value
        # select wall when enemy spawn
        # 0=N, 1=E, 2=S, 3=W
        wall = random.randint(0, 3)
        # spawn range in x and y directions
        width = settings.WIDTH - self.width
        height = settings.HEIGHT - settings.score_surface_height - self.height
        
        # update x and y coords based on the wall to spawn
        if wall == 0:
            self.x = random.randint(0, width)
        elif wall == 1:
            self.x = width
            self.y = random.randint(0, height)
        elif wall == 2:
            self.x = random.randint(0, width)
            self.y = height
        elif wall == 3:
            self.y = random.randint(0, height)
    
    
    def draw(self, surface):
        self.draw_rect(surface=surface)


class Enemy_A(Enemy_global):
    def __init__(self):
        x, y = 0, 0
        super().__init__(x=x, y=y, move_speed=50, hp=3, exp_value=1) 


class Enemy_B(Enemy_global):
    def __init__(self):
        x, y = 0, 0
        super().__init__(x=x, y=y, move_speed=40, hp=5, exp_value=2,
                         colour=(50, 200, 255))


class Enemy_C(Enemy_global):
    def __init__(self):
        x, y = 0, 0
        super().__init__(x=x, y=y, move_speed=60, hp=8, exp_value=3,
                         colour=(200, 50, 255))