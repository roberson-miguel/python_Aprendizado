#incrementando uma variavel
#imprimindo uma repetição
#usuario digita um num e o print dos numeros pares até o numero digitado

#modelo 1 usando o IF
num = int(input('Digite o ultimo numero: '))
x = 0
while x <= num:
    if x % 2 == 0:
        print(x)
    x = x + 1

#modelo 1 sem usar o IF

num = int(input('Digite o ultimo numero: '))
x = 0
while x <= num:
    print(x)
    x = x + 2
