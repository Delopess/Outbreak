# ui.py
import pygame 
import math
from settings import WHITE, GRAY, BLACK, WIDTH, HEIGHT
from Modules.star import draw_star_field


# Menu principal
# Esta função renderiza o menu principal do jogo e retorna botões de seleção para os modos de jogo
# e configurações.
def menu(screen, star_field):
    screen.fill((0, 0, 0))

    # Renderiza o título principal
    title_font = pygame.font.Font("Resources/Fonts/Outbreak.ttf", 120)
    title_text = "Outbreak"
    title = title_font.render(title_text, True, WHITE)
    # Centraliza o título na parte superior da tela
    screen.blit(title, (screen.get_width() // 2 - title.get_width() // 2, 100))
    
    # Subtítulo com animação de desvanecimento
    subtitle_font = pygame.font.Font(None, 30)
    subtitle_text = "Selecione o modo de jogo"
    alpha = 150 + int(105 * abs(math.sin(pygame.time.get_ticks() / 500)))
    subtitle = subtitle_font.render(subtitle_text, True, GRAY)
    subtitle.set_alpha(alpha)
    screen.blit(subtitle, (WIDTH // 2 - subtitle.get_width() // 2, HEIGHT // 3.1 + 100))

    # Criação dos botões do menu principal
    survival_tdm_button = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2, 200, 50)  # Botão para "Sobrevivência"
    horde_button = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 + 70, 200, 50)  # Botão para "Horda"
    horde_label = subtitle_font.render("Em Breve ->", True, GRAY)
    screen.blit(horde_label, (horde_button.x  // 1.2 - horde_label.get_width() // 5, horde_button.y + 20))
    flag_button = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 + 140, 200, 50)  # Botão para "Capture the flag"
    flag_label = subtitle_font.render("Em Breve ->", True, GRAY)
    screen.blit(flag_label, (flag_button.x  // 1.2 - flag_label.get_width() // 5, flag_button.y + 20))
    settings_button = pygame.Rect(WIDTH - 70, HEIGHT - 70, 60, 60)      # Botão para "Configurações"
    mouse_pos = pygame.mouse.get_pos()

    # Desenha os botões e aplica os efeitos
    if survival_tdm_button.collidepoint(mouse_pos):
        pygame.draw.rect(screen, (100, 100, 255), survival_tdm_button, border_radius=10)
        pygame.draw.rect(screen, WHITE, survival_tdm_button, 3, border_radius=10)
    else:
        pygame.draw.rect(screen, (100, 100, 255), survival_tdm_button, border_radius=10)  
        pygame.draw.rect(screen, BLACK, survival_tdm_button, 3, border_radius=10)
        
    if horde_button.collidepoint(mouse_pos):
        pygame.draw.rect(screen, (GRAY), horde_button, border_radius=10)
        pygame.draw.rect(screen, WHITE, horde_button, 3, border_radius=10)
    else:
        pygame.draw.rect(screen, (GRAY), horde_button, border_radius=10)  
        pygame.draw.rect(screen, BLACK, horde_button, 3, border_radius=10)

    if flag_button.collidepoint(mouse_pos):
        pygame.draw.rect(screen, (GRAY), flag_button, border_radius=10)
        pygame.draw.rect(screen, WHITE, flag_button, 3, border_radius=10)
    else:
        pygame.draw.rect(screen, (GRAY), flag_button, border_radius=10)  
        pygame.draw.rect(screen, BLACK, flag_button, 3, border_radius=10)

    if settings_button.collidepoint(mouse_pos):
        pygame.draw.rect(screen, (BLACK), settings_button, border_radius=10)
        pygame.draw.rect(screen, WHITE, settings_button, 3, border_radius=10)
    else:
        pygame.draw.rect(screen, (BLACK), settings_button, border_radius=10)  
        pygame.draw.rect(screen, BLACK, settings_button, 3, border_radius=10)

    # Renderiza o texto dos botões
    button_font = pygame.font.Font(None, 36)
    survival_text = button_font.render("Sobrevivência", True, (0, 0, 0))
    horde_text = button_font.render("Horda", True, (0, 0, 0))
    flag_text = button_font.render("Capture the flag", True, (0, 0, 0))

    gear_image = pygame.image.load("Resources/Images/gear.png")  # Substitua pelo caminho correto da imagem
    # Desenhar a imagem no botão de configurações
    gear_image_resized = pygame.transform.scale(gear_image, (45, 45))  # Ajuste o tamanho da imagem
    

    # Posiciona o texto centralizado dentro dos botões
    screen.blit(survival_text, (survival_tdm_button.x + survival_tdm_button.width // 2 - survival_text.get_width() // 2, survival_tdm_button.y + 10))
    screen.blit(horde_text, (horde_button.x + horde_button.width // 2 - horde_text.get_width() // 2, horde_button.y + 10))
    screen.blit(flag_text, (flag_button.x + flag_button.width // 2 - flag_text.get_width() // 2, flag_button.y + 10))
    screen.blit(gear_image_resized, (settings_button.x + (settings_button.width - 1) // 9, settings_button.y + (settings_button.height - 45) // 2))
    
    draw_star_field(screen, star_field)  # Fundo de estrelas

    # Atualiza o display
    pygame.display.flip()
    return survival_tdm_button, settings_button, horde_button, flag_button

# Tela de configurações
# Esta função exibe a tela de configurações com uma opção para voltar ao menu principal.
def settings_menu(screen, star_field):
    # Preenche a tela com preto
    screen.fill((0, 0, 0))

    # Renderiza o título da tela de configurações
    title_font = pygame.font.Font(None, 60)
    title = title_font.render("Configurações", True, WHITE)
    screen.blit(title, (screen.get_width() // 2 - title.get_width() // 2, 100))

    # Criação do botão para voltar
    back_button = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 + 140, 200, 50)
    mouse_pos = pygame.mouse.get_pos()

    # Desenha o botão na tela e aplica os efeitos
    if back_button.collidepoint(mouse_pos):
        pygame.draw.rect(screen, (100, 100, 100), back_button, border_radius=10)
        pygame.draw.rect(screen, WHITE, back_button, 3, border_radius=10)
    else:
        pygame.draw.rect(screen, (50, 50, 50), back_button, border_radius=10)  # Ajuste de translucidez
        pygame.draw.rect(screen, BLACK, back_button, 3, border_radius=10)

    # Renderiza o texto do botão
    button_font = pygame.font.Font(None, 36)
    back_text = button_font.render("Voltar", True, (0, 0, 0))

    # Posiciona o texto dentro do botão
    screen.blit(back_text, (back_button.x + back_button.width // 2 - back_text.get_width() // 2, back_button.y + 10))
    
    draw_star_field(screen, star_field)  # Fundo de estrelas

    # Atualiza o display
    pygame.display.flip()
    return back_button

# Tela de seleção de personagem
# Esta função permite ao jogador escolher entre os personagens "Sobrevivente" e "Zumbi",
# com a opção de voltar ao menu principal.
def character_selection(screen, star_field):
    screen.fill((0, 0, 0))

    # Renderiza o título da tela de seleção
    title_font = pygame.font.Font(None, 60)
    title = title_font.render("Escolha seu Personagem", True, WHITE)
    screen.blit(title, (screen.get_width() // 2 - title.get_width() // 2, 100))

    # Criação dos botões para seleção de personagens e voltar
    survivor_button = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2, 200, 50)
    zombie_button = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 + 70, 200, 50)
    back_button = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 + 140, 200, 50)
    mouse_pos = pygame.mouse.get_pos()      # Botão "Voltar"

    # Desenha os botões na tela e aplica os efeitos
    if survivor_button.collidepoint(mouse_pos):
        pygame.draw.rect(screen, (0, 180, 0), survivor_button, border_radius=10)  # Translucidez no botão
        pygame.draw.rect(screen, WHITE, survivor_button, 3, border_radius=10)
    else:
        pygame.draw.rect(screen, (0, 180, 0), survivor_button, border_radius=10)  # Translucidez no botão
        pygame.draw.rect(screen, BLACK, survivor_button, 3, border_radius=10)

    if zombie_button.collidepoint(mouse_pos):
        pygame.draw.rect(screen, (180, 0, 0), zombie_button, border_radius=10)  # Translucidez no botão
        pygame.draw.rect(screen, WHITE, zombie_button, 3, border_radius=10)
    else:
        pygame.draw.rect(screen, (180, 0, 0), zombie_button, border_radius=10)  # Translucidez no botão
        pygame.draw.rect(screen, BLACK, zombie_button, 3, border_radius=10)

    if back_button.collidepoint(mouse_pos):
        pygame.draw.rect(screen, (100, 100, 100), back_button, border_radius=10)  # Translucidez no botão
        pygame.draw.rect(screen, WHITE, back_button, 3, border_radius=10)
    else:
        pygame.draw.rect(screen, (50, 50, 50), back_button, border_radius=10)  # Translucidez no botão
        pygame.draw.rect(screen, BLACK, back_button, 3, border_radius=10)


    # Renderiza o texto dos botões
    button_font = pygame.font.Font(None, 36)
    survivor_text = button_font.render("Sobrevivente", True, (0, 0, 0))
    zombie_text = button_font.render("Zumbi", True, (0, 0, 0))
    back_text = button_font.render("Voltar", True, (0, 0, 0))

    # Posiciona o texto centralizado dentro de cada botão
    screen.blit(survivor_text, (survivor_button.x + survivor_button.width // 2 - survivor_text.get_width() // 2, survivor_button.y + 10))
    screen.blit(zombie_text, (zombie_button.x + zombie_button.width // 2 - zombie_text.get_width() // 2, zombie_button.y + 10))
    screen.blit(back_text, (back_button.x + back_button.width // 2 - back_text.get_width() // 2, back_button.y + 10))
    
    draw_star_field(screen, star_field)  # Fundo de estrelas no menu de seleção de personagem

    # Atualiza o display
    pygame.display.flip()
    return survivor_button, zombie_button, back_button
