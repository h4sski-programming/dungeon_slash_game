import pygame

from settings import Settings_player
from sprite import Sprite

settings_player = Settings_player()

class Player(Sprite):
    def __init__(self, x, y):
        self.width = 20
        self.height = self.width
        # Call the __init__ method of the parent class (Sprite)
        super().__init__(x - self.width//2, y - self.height//2, move_speed = settings_player.move_speed)  
        self.score = 0
        self.hp = 10
        self.fire_rate = 1
        self.bullet_move_speed = 200
        
        
    def draw(self, surface):
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(surface, (255, 100, 100), self.rect)