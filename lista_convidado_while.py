convidados = int(input("Numero de convidados: "))
pessoas = []

while convidados > 0:
    #nome = input("digite um nome de convidado: ")
    pessoas.append(input("digite um nome de convidado: "))
    convidados = convidados - 1

print("Os convidados são: ", pessoas)
