from Veiculo import *


class Automovel(Veiculo):

    def __init__(self, marca, qtdRodas, modelo, velocidade, potenciaDoMotor):
        Veiculo.__init__(self, marca, qtdRodas, modelo, velocidade)
        self.potenciaDoMotor = potenciaDoMotor

    def imprimirinformacoes(self):
        Veiculo.imprimirinformacoes(self)
        print(
            "Potencia do Motor:", self.potenciaDoMotor
        )