print("\n****************Calculadora em Python***************")
print()
print("-----------Menu----------")
print()
print("Selecione a opção desejada:")
print("1- Somar")
print("2- Subtrair")
print("3- Multiplicar")
print("4- Dividir")
print()


def soma(num1, num2):
    return num1 + num2

def div(num1, num2):
    resultado = num1 / num2
    return resultado


def sub(num1, num2):
    resultado = num1 - num2
    return resultado

def mul(num1, num2):
    resultado = num1 * num2
    return resultado

opcao = int(input("Digite a uma das opções: (1/2/3/4: "))
num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digiete o segundo numero: "))

if opcao == 1:
    print("O resultado é: ", soma(num1, num2))
elif opcao == 2:
    print("O resultado é: ", sub(num1, num2))
elif opcao == 3:
    print("O resultado é: ", mul(num1, num2))
elif opcao == 4:
    print("O resultadoé: ", div(num1, num2))
else:
    print("Opção inválida!!!!")



