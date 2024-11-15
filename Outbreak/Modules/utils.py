import random

def random_safe_position(world_width, world_height, is_position_occupied):
    while True:
        x = random.randint(0, world_width)
        y = random.randint(0, world_height)
        if not is_position_occupied(x, y):  # Verifique se a posição está livre
            return x, y