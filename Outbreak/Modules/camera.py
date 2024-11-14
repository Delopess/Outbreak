# camera.py
import pygame
from settings import WIDTH, HEIGHT, GRAY, GRID_SIZE, FONT, WHITE, WORLD_HEIGHT, WORLD_WIDTH

def draw_grid(screen, camera_x, camera_y, zoom):
    # Função para desenhar a grade no mapa
    for x in range(0, WORLD_WIDTH, GRID_SIZE):
        pygame.draw.line(screen, GRAY, ((x - camera_x) * zoom, 0), ((x - camera_x) * zoom, HEIGHT))
    for y in range(0, WORLD_HEIGHT, GRID_SIZE):
        pygame.draw.line(screen, GRAY, (0, (y - camera_y) * zoom), (WIDTH, (y - camera_y) * zoom))
        
def display_score(screen, player):
    score_text = FONT.render(f"Pontuação: {int(player.points)}", True, WHITE)
    screen.blit(score_text, (WIDTH - score_text.get_width() - 20, 10))
