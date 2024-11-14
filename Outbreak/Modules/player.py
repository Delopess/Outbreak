# player.py
import pygame
from settings import RED, GREEN

class Player:
    def __init__(self, x, y, size, color):
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.points = 0
        self.alive = True
        self.direction = (0, -1)
        self.base_speed = 5  # Velocidade base que pode ser ajustada

    def draw(self, screen, camera_x, camera_y, zoom):
        pygame.draw.circle(
            screen,
            self.color,
            (int((self.x - camera_x) * zoom), int((self.y - camera_y) * zoom)),
            int(self.size * zoom)
        )

    def move(self, camera_x, camera_y, zoom):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        target_x = (mouse_x / zoom) + camera_x
        target_y = (mouse_y / zoom) + camera_y
        dx = target_x - self.x
        dy = target_y - self.y
        distance = (dx**2 + dy**2)**0.5

        # Atualizando a velocidade baseada no tamanho do jogador
        speed = max(1, self.base_speed - 0.05 * self.size)  # Certifique-se que a velocidade não seja menor que 1

        if distance > 1:
            self.x += dx / distance * speed
            self.y += dy / distance * speed
            self.direction = (dx / distance, dy / distance)

    def limit_to_bounds(self, world_width, world_height):
        self.x = max(self.size, min(world_width - self.size, self.x))
        self.y = max(self.size, min(world_height - self.size, self.y))

class Zombie(Player):
    def __init__(self, x, y, size):
        super().__init__(x, y, size, RED)

class Survivor(Player):
    def __init__(self, x, y, size):
        super().__init__(x, y, size, GREEN)
