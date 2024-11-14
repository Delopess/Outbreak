# star.py
import pygame
import random
from settings import WIDTH, HEIGHT

class Star:
    def __init__(self, x, y, size, speed):
        self.x = x
        self.y = y
        self.size = size
        self.speed = speed
        self.brightness = 255
        self.brightness_change = random.uniform(-5, 5)

    def update(self):
        self.x -= self.speed
        if self.x < 0:
            self.x = WIDTH
            self.y = random.randint(0, HEIGHT)

        self.brightness += self.brightness_change
        if self.brightness >= 255 or self.brightness <= 150:
            self.brightness_change = -self.brightness_change
        self.brightness = max(150, min(255, self.brightness))

    def draw(self, screen):
        color = (self.brightness, self.brightness, self.brightness)
        pygame.draw.circle(screen, color, (int(self.x), int(self.y)), self.size)

def create_star_field():
    layers = {
        "near": [Star(random.randint(0, WIDTH), random.randint(0, HEIGHT), 2, 1) for _ in range(50)],
        "mid": [Star(random.randint(0, WIDTH), random.randint(0, HEIGHT), 1, 0.5) for _ in range(70)],
        "far": [Star(random.randint(0, WIDTH), random.randint(0, HEIGHT), 0.25, 0.1) for _ in range(100)]
    }
    return layers

def draw_star_field(screen, star_field):
    for layer in star_field.values():
        for star in layer:
            star.update()
            star.draw(screen)
