import pygame
from sprite import Sprite

class Player(Sprite):
    def __init__(self, x, y):
        self.width = 20
        self.height = self.width
        super().__init__(x - self.width//2, y - self.height//2)  # Call the __init__ method of the parent class (Sprite)
        self.score = 0
        self.hp = 10
        
        
    def draw(self, surface):
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(surface, (255, 100, 100), self.rect)