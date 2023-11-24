import math

class Sprite():
    def __init__(self, x, y, angle=0.0, width=0, height=0,):
        self.x = x
        self.y = y
        self.angle = angle
        self.width = width
        self.height = height
    
    
    def move(self, dt, x, y):
        self.x += x * dt
        self.y += y * dt
    
    
    def update(self, position):
        self.angle = self.get_angle(position)
        
        
    def get_position_int(self):
        return [self.x, self.y]
    
    
    def get_distance(self, position):
        return math.sqrt((position[0] - self.x)**2 + (position[1] - self.y)**2 )
    
    
    def get_angle(self, position):
        return math.atan2(position[1] - self.y,
                          position[0] - self.x)