from Automovel import *

class Carro(Automovel):


    def __init__(self, marca, qtdRodas, modelo, potenciaDoMotor, qtdPortas, velocidade = 0):
        Automovel.__init__(self, marca, qtdRodas, modelo, velocidade, potenciaDoMotor)
        self.qtdPortas = qtdPortas

    def imprimirinformacoes(self):
        Automovel.imprimirinformacoes(self)
        print(
            "Quantidade de portas:", self.qtdPortas
        )