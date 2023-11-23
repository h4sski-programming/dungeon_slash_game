import pygame

from sprite import Sprite


class Bullet(Sprite):
    def __init__(self, x, y, move_speed, angle=0):
        super().__init__(x, y, move_speed, angle)
        
    
    def draw(self, surface):
        self.rect = pygame.Rect(self.x, self.y, 5, 5)
        pygame.draw.rect(surface, (100, 255, 100), self.rect)
        
    
    def update(self, *args, **kwargs):
        pass