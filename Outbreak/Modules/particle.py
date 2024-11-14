# particle.py
import pygame
import random

class Particle:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.size = random.randint(2, 5)
        self.lifetime = random.randint(20, 40)
        self.speed_x = random.uniform(-1, 1)
        self.speed_y = random.uniform(-1, 1)

    def update(self):
        self.x += self.speed_x
        self.y += self.speed_y
        self.size = max(0, self.size - 0.1)
        self.lifetime -= 1

    def draw(self, screen, camera_x, camera_y, zoom):
        if self.size > 0:
            pygame.draw.circle(
                screen, 
                self.color, 
                (int((self.x - camera_x) * zoom), int((self.y - camera_y) * zoom)), 
                int(self.size * zoom)
            )

def create_explosion(particles, x, y, color, count=25):
    for _ in range(count):
        new_particle = Particle(x, y, color)
        particles.append(new_particle)
