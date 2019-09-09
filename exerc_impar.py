#usuario digita um num e o print dos numeros impares até o numero digitado


num = int(input('Digite o ultimo numero: '))
x = 0
while x <= num:
    if x % 2 != 0:
        print(x)
    x = x + 1
