#somadora3 - somado infinita

print('Digite os valores seguidos de enter')
print('Para encerrar apenas tecle ENTER')
total = 0
while 1:
    try:
            n = float(input('Digite um valor? :'))
            total = total + n
    except:
        break
print('Total: {}' .format(total))
