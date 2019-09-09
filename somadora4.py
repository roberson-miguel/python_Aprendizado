#somadora4 - somado infinita, tratando excessão

print('Digite os valores seguidos de enter')
print('Para encerrar apenas tecle ENTER')
total = 0
while 1:
    try:
        linha = input('Digite um valor? :')
        n = float(linha)
        total = total + n
    except:
        if len(linha) == 0:
            break
        elif ',' in linha:
            print('Use .(ponto) como separador decimal')
        else:
            print('Digite apenas números')
print('Total: {}' .format(total))