'''
Comentario de varias linhas usasse as 3 aspas
'''

a = int(input('primeiro: '))
b = int(input('segundo: '))
c = int(input('terceiro: '))

if a >= b and a >= c:
    print('Maior é: {}'.format(a))
elif b >= c:
    print('Maior é : {}'.format(b))
else:
    print('Maior é : {}'.format(c))
