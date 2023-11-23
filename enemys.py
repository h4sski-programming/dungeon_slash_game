import pygame
import random

from settings import Settings_dungeon_slach_game
from sprite import Sprite


settings = Settings_dungeon_slach_game()


class Enemy_global(Sprite):
    def __init__(self, x, y, move_speed, hp):
        self.hp = hp
        self.width = 10
        self.height = self.width
        super().__init__(x=x, y=y, move_speed=move_speed)
    
    def draw(self, surface):
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(surface, (100, 100, 255), self.rect)


class Enemy_A(Enemy_global):
    def __init__(self):
        x, y = 0, 0
        super().__init__(x=x, y=y, move_speed=50, hp=2)
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
            