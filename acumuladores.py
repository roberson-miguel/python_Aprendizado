n = 1
soma = 0
while n <= 10:
    x = int(input('Digite o {} numero: '.format(n)))
    soma = soma + x
    n = n + 1
print('Soma: {}'.format(soma))
print('Media: {}'.format(soma / n))
