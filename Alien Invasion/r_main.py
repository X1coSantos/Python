import sys

import pygame

from r_nave import Nave
from r_definicoes import Definicoes
import r_functions as rf

def executar_jogo():

    # Inicializar pygame e as definicoes
    pygame.init()
    defs = Definicoes()

    # Criar ecra e fonte
    screen = rf.criar_ecra(defs)

    # Cria objeto da nave
    nave = Nave(screen, defs)

    # Loop principal do jogo
    while True:
        # Checkar Eventos
        rf.checkar_eventos(nave)
        nave.atualiza_movimento()

        # Atualizar tela
        rf.atualizar_tela(screen, defs, nave)



executar_jogo()
