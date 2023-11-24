import pygame
import math

from settings import Settings_dungeon_slach_game
from sprite import Sprite


settings = Settings_dungeon_slach_game()


class Character(Sprite):
    def __init__(self, x, y, move_speed, hp, colour,
                 width=10, height=False,
                 destroyable=True, moveable=True):
        if not height:
            height = width
        super().__init__(x=x, y=y, width=width, height=height)
        self.move_speed = move_speed
        self.hp = hp
        self.colour = colour
        self.destroyable = destroyable
        self.moveable = moveable
        self.alive = True
    
    
    def walk(self, dt):
        if self.moveable:
            self.x += self.move_speed * math.cos(self.angle) * dt
            self.y += self.move_speed * math.sin(self.angle) * dt
    
    
    def get_dmg(self, dmg):
        self.hp -= dmg
        if self.hp <= 0:
            self.alive = False
    
    
    def draw_rect(self, surface):
        self.update_draw()
        pygame.draw.rect(surface, self.colour, self.rect)
        
        
    def draw_circle(self, surface):
        self.update_draw()
        pygame.draw.circle(surface, self.colour, self.get_position_int(),
                           radius = self.width/2)
        
    def draw_oval(self, surface, radius, width):
        self.update_draw()
        pygame.draw.circle(surface, self.colour, self.get_position_int(),
                           radius = radius, width=width)


    def update_draw(self):
        self.rect = pygame.Rect(self.x - self.width//2,
                                self.y - self.height//2,
                                self.width, self.height)
    

