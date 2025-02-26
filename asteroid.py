import pygame
import random
from constants import *
from circleshape import CircleShape
from player import Player

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
    def draw(self, surface):
        pygame.draw.circle(surface,"white",(self.position), self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return False
        
        random_angle = random.uniform(20, 50)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        velocities = [
            self.velocity.rotate(random_angle),
            self.velocity.rotate(-random_angle)
        ]
        
        for velocity in velocities:
            asteroid = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid.velocity = velocity * 1.2
            
            

