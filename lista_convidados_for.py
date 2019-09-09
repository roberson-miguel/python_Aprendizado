convidados = int(input("Numero de convidados: "))
pessoas = []
for i in range(convidados):
        #nomes = input("digite um nome de convidado: ")
        pessoas.append(input("digite um nome de convidado: "))
        convidados = convidados - 1
print("Os convidados são: ", pessoas)