from Automovel import *

class Moto(Automovel):


    def __init__(self, marca, qtdRodas, modelo, potenciaDoMotor, partidaEletrica , velocidade = 0):
        Automovel.__init__(self, marca, qtdRodas, modelo, velocidade, potenciaDoMotor)
        self.partidaEletrica = partidaEletrica

    def imprimirinformacoes(self):
        Automovel.imprimirinformacoes(self)
        print(
            "Partida elétrica:", self.partidaEletrica
        )
