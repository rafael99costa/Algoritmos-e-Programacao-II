from Bicicleta import *
from Moto import *
from Carro import *



bike = Bicicleta("Caloi", 2, "Caloi Cross", 6, "Não")
print(bike.acelerar(10))
print(bike.freiar(2))
bike.imprimirinformacoes()


# moto = Moto("Honda", 2, "Elite 125", "9,34 cv", "Sim")
# print(moto.acelerar(30))
# print(moto.freiar(5))
# moto.imprimirinformacoes()


# carro = Carro("BMW", 4, "BMW Série 4 Cabrio", "258 cv", 4)
# print(carro.acelerar(60))
# print(carro.freiar(10))
# carro.imprimirinformacoes()