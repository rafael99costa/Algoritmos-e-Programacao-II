from Veiculo import *


class Bicicleta(Veiculo):

    def __init__(self, marca, qtdRodas, modelo, nunMarchas, bagageiro, velocidade = 0):
        Veiculo.__init__(self, marca, qtdRodas, modelo, velocidade)
        self.nunMarchas = nunMarchas
        self.bagageiro = bagageiro
                


    def imprimirinformacoes(self):
        Veiculo.imprimirinformacoes(self)
        print(
            "Numero de Marchas:", self.nunMarchas, "\n"
            "Bagageiro:", self.bagageiro
        )

