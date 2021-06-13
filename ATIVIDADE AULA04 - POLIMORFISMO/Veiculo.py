
class Veiculo:

    def __init__(self, marca, qtdRodas, modelo, velocidade):
        self.marca = marca
        self.qtdRodas = qtdRodas
        self.modelo = modelo
        self.velocidade = velocidade

    def imprimirinformacoes(self):
        print(
            'Marca:', self.marca, "\n"
            'Quantidade de Rodas:', self.qtdRodas, "\n"
            'Modelo:', self.modelo, "\n"
            'Velocidade:', self.velocidade
        )

    def acelerar(self, valor):
        self.velocidade = self.velocidade + valor
        return "Acelerando..."

    def freiar(self, valor):
        self.velocidade = self.velocidade - valor
        return "Freiando..."
