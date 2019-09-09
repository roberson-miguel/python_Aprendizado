convidados = int(input("Numero de convidados: "))
pessoas = []
for i in range(convidados):
    pessoas.append(input("digite um nome de convidado: "))
    convidados = convidados - 1
print("Os convidados são: ", pessoas)