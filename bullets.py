import pygame

from character import Character


class Bullet(Character):
    def __init__(self, x, y, move_speed, aoe, dmg, angle=0):
        super().__init__(x, y, move_speed, hp=1, colour=(100, 255, 100),
                         width=10)
        self.aoe = aoe
        self.dmg = dmg
        self.angle = angle
        self.detonated = False
        self.detonation_duration = 100
    
    
    def detonate(self, time):
        self.detonated = True
        self.moveable = False
        self.detonation_time = time
    
    
    def draw(self, surface):
        if self.detonated:
            pygame.draw.circle(surface, self.colour, self.get_position_int(),
                           radius = self.aoe)
        else:
            self.draw_circle(surface=surface)
        
    
    def update(self, time, *args, **kwargs):
        if self.detonated:
            self.alive = False
                