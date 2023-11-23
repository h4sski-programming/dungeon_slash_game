import math

class Sprite():
    def __init__(self, x, y, move_speed, angle=0.0):
        self.x = x
        self.y = y
        self.move_speed = move_speed
        self.angle = angle
    
    
    def walk(self, dt):
        self.x += self.move_speed * math.cos(self.angle) * dt
        self.y += self.move_speed * math.sin(self.angle) * dt
    
    
    def move(self, dt, x, y):
        self.x += x * dt
        self.y += y * dt
    
    
    def update(self, player_x, player_y):
        self.angle = math.atan2(player_y-self.y, player_x-self.x)