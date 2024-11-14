# point.py
import pygame
import random
from settings import WORLD_WIDTH, WORLD_HEIGHT

class Point:
    def __init__(self):
        self.x = random.randint(20, WORLD_WIDTH - 20)
        self.y = random.randint(20, WORLD_HEIGHT - 20)
        self.size = 5
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    def draw(self, screen, camera_x, camera_y, zoom):
        pygame.draw.circle(
            screen,
            self.color,
            (int((self.x - camera_x) * zoom), int((self.y - camera_y) * zoom)),
            max(1, int(self.size * zoom))
        )
