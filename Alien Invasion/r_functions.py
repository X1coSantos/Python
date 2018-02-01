import sys

import pygame

def criar_ecra(defs):
    """ Cria ecra! """
    screen = pygame.display.set_mode(
        (defs.screen_largura, defs.screen_altura)
    )
    pygame.display.set_caption("Rocket Game v0.0")
    return screen

def checkar_eventos_pressionar_tecla(event, nave):
    """ Checka os eventos quando as teclas sao pressionadas"""
    if event.key == pygame.K_RIGHT:
        nave.mover_direita = True
    elif event.key == pygame.K_LEFT:
        nave.mover_esquerda = True
    elif event.key == pygame.K_UP:
        nave.mover_cima = True
    elif event.key == pygame.K_DOWN:
        nave.mover_baixo = True

def checkar_eventos_levantar_tecla(event, nave):
    """ Checka os eventos quando as teclas sao levantadas """
    if event.key == pygame.K_RIGHT:
        nave.mover_direita = False
    elif event.key == pygame.K_LEFT:
        nave.mover_esquerda = False
    elif event.key == pygame.K_UP:
        nave.mover_cima = False
    elif event.key == pygame.K_DOWN:
        nave.mover_baixo = False

def checkar_eventos(nave):
    """ Checka os eventos """

    for event in pygame.event.get():
        # Caso o evento seja para sair
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            checkar_eventos_pressionar_tecla(event, nave)

        elif event.type == pygame.KEYUP:
            checkar_eventos_levantar_tecla(event, nave)

def atualizar_tela(screen, defs, nave):
    # Atualiza a tela

    # Background
    screen.fill(defs.cor_background)

    # Desenha a nave
    nave.desenhar_nave()

    #

    nave.informacoes_coordenadas()

    # Faz o screen ser mostrado
    pygame.display.flip()
