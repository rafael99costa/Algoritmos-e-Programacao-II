from Pessoa import *

class Juridica(Pessoa):
    
    def __init__(self, codigo, nome, endereco, telefone, cnpj, inscricaoEstadual, quantidadeFuncionarios):
        Pessoa.__init__(self, codigo, nome, endereco, telefone)
        self.__cnpj = cnpj
        self.__inscricaoEstadual = inscricaoEstadual
        self.quantidadeFuncionarios = quantidadeFuncionarios


    def imprimeCNPJ(self):
        return self.__cnpj

    def __emitirNotaFiscal(self):
        return 'Nota Fiscal emitida..'