class Definicoes():
    """ Classe das definicoes do jogo! """

    def __init__(self):
        """ Inicializa as definicoes do jogo """

        # Define dimensoes do ecra
        self.screen_largura = 1200
        self.screen_altura = 700

        # Define cor do background
        self.cor_background = (230, 230, 230)

        # Definições da nave
        self.velocidade_inicial = 1.2
        self.velocidade_factor = 2
        self.velocidade_final = self.velocidade_factor * self.velocidade_inicial