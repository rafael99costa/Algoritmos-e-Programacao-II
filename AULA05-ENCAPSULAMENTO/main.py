from Fisica import *
from Juridica import *

f = Fisica(1, "Rafael", "Rua Tal", "99999-9998", "06698446539", 21, 60, 1.74)
print("Nome: ", f.imprimeNome())
print("CPF: ",f.imprimeCPF())

j = Juridica(1, "Rafael Costa", "Rua Tal", "99999-9998", "54.654.128/0001-99", "Inscriçãoo estadual", 1500)
print("Nome: ", j.imprimeNome())
print("CNPJ: ",j.imprimeCNPJ())