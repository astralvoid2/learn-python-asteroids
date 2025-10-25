from circleshape import CircleShape
from constants import *
import random
import pygame

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)        

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), (int(self.position.x), int(self.position.y)), self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
        
    def kill(self):
        self.radius = 0  # mark as dead
        return super().kill()
        
    def split(self):        
        if self.radius <= ASTEROID_MIN_RADIUS:
            self.kill()            
            return []        
        random_angle = random.uniform(ASTEROID_SPLIT_ANGLE_MIN, ASTEROID_SPLIT_ANGLE_MAX)
        
        new_vector1 = self.velocity.rotate(random_angle) * ASTEROID_SPLIT_SPEED_MULTIPLIER
        new_vector2 = self.velocity.rotate(-random_angle) * ASTEROID_SPLIT_SPEED_MULTIPLIER
        
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid1.velocity = new_vector1

        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2.velocity = new_vector2
        # kill this asteroid since new ones were created.    
        self.kill()
        return [asteroid1, asteroid2]       
        
        