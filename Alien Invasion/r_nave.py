import pygame

class Nave():
    """ Classe principal da nave """

    def __init__(self, screen, defs):
        """ Inicializa as informações da nave """

        # Informaçoes
        self.screen = screen
        self.defs = defs

        # Load da imagem e define lados
        self.imagem = pygame.image.load('imagens/ship.bmp')
        self.pos_imagem = self.imagem.get_rect()
        self.pos_screen = self.screen.get_rect()

        # Define posição inicial
        self.pos_imagem.centerx = self.pos_screen.centerx
        self.pos_imagem.centery = self.pos_screen.centery
        self.pos_imagem.bottom = self.pos_screen.centery


        # Movimento
        self.mover_direita = False
        self.mover_esquerda = False
        self.mover_cima = False
        self.mover_baixo = False

        # Eixos
        self.x = float(self.pos_imagem.centerx)
        self.y = float(self.pos_imagem.centery)

    def desenhar_nave(self):
        """ Desenha a nave """
        self.screen.blit(self.imagem, self.pos_imagem)

    def atualiza_movimento(self):
        """ Atualiza o movimento da nave! """

        if self.mover_direita and self.pos_imagem.right < self.pos_screen.right:
            self.x += self.defs.velocidade_final
            if self.mover_cima and self.pos_imagem.top > self.pos_screen.top:
                self.y -= self.defs.velocidade_final
            if self.mover_baixo and self.pos_imagem.bottom < self.pos_screen.bottom:
                self.y += self.defs.velocidade_final
        elif self.mover_direita and self.mover_cima and self.pos_imagem.top > self.pos_screen.top:
            self.y -= self.defs.velocidade_final
        elif self.mover_direita and self.mover_baixo and self.pos_imagem.bottom < self.pos_screen.bottom:
            self.y += self.defs.velocidade_final

        if self.mover_esquerda and not self.mover_direita and self.pos_imagem.left > self.pos_screen.left:
            self.x -= self.defs.velocidade_final
            if self.mover_cima and self.pos_imagem.top > self.pos_screen.top:
                self.y -= self.defs.velocidade_final
            if self.mover_baixo and self.pos_imagem.bottom < self.pos_screen.bottom:
                self.y += self.defs.velocidade_final
        elif self.mover_esquerda and not self.mover_direita and self.mover_baixo \
                and self.pos_imagem.bottom < self.pos_screen.bottom:
            self.y += self.defs.velocidade_final
        elif self.mover_esquerda and not self.mover_direita and self.mover_cima \
                and self.pos_imagem.top > self.pos_screen.top:
            self.y -= self.defs.velocidade_final

        if self.mover_cima and not self.mover_esquerda and not self.mover_direita \
                and self.pos_imagem.top > self.pos_screen.top:
            self.y -= self.defs.velocidade_final
        if self.mover_baixo and not self.mover_esquerda and not self.mover_direita\
                and self.pos_imagem.bottom < self.pos_screen.bottom:
            self.y += self.defs.velocidade_final

        self.pos_imagem.centerx = self.x
        self.pos_imagem.centery = self.y

    def informacoes_coordenadas(self):
        """ Mostra as informações das coordenadas! """

        # texto
        texto = str(f"(x: {self.x:.0f},y: {self.y:.0f})")
        texto2 = str(f"Direita: {self.mover_direita}")
        texto3 = str(f"Esquerda: {self.mover_esquerda}")
        texto4 = str(f"Cima: {self.mover_cima}")
        texto5 = str(f"Baixo: {self.mover_baixo}")
        fonte = pygame.font.SysFont('Arial', 15)
        layer_fonte1 = fonte.render(texto, True, (0, 0, 0))
        layer_fonte2 = fonte.render(texto2, True, (0, 0, 0))
        layer_fonte3 = fonte.render(texto3, True, (0, 0, 0))
        layer_fonte4 = fonte.render(texto4, True, (0, 0, 0))
        layer_fonte5 = fonte.render(texto5, True, (0, 0, 0))
        layer_fonte1_pos = (self.pos_screen.left + 25, self.pos_screen.top + 25)
        layer_fonte1_pos1 = (self.pos_screen.left + 25, self.pos_screen.top + 50)
        layer_fonte1_pos2 = (self.pos_screen.left + 25, self.pos_screen.top + 75)
        layer_fonte1_pos3 = (self.pos_screen.left + 25, self.pos_screen.top + 100)
        layer_fonte1_pos4 = (self.pos_screen.left + 25, self.pos_screen.top + 125)
        self.screen.blit(layer_fonte1, layer_fonte1_pos)
        self.screen.blit(layer_fonte2, layer_fonte1_pos1)
        self.screen.blit(layer_fonte3, layer_fonte1_pos2)
        self.screen.blit(layer_fonte4, layer_fonte1_pos3)
        self.screen.blit(layer_fonte5, layer_fonte1_pos4)

