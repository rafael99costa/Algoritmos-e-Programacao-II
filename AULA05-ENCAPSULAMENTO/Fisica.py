from Pessoa import *

class Fisica(Pessoa):

    def __init__(self, codigo, nome, endereco, telefone, cpf, idade, peso, altura):
        Pessoa.__init__(self, codigo, nome, endereco, telefone)
        self.__cpf = cpf
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def imprimeCPF(self):
        return self.__cpf

    def __calculaIMC(self):
        # IMC = Peso ÷ (Altura × Altura)
        imc = self.peso / (self.altura * self.altura)
        return float(imc)