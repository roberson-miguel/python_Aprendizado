'''
Programa pede o tamanho da parede a ser pintada, consideramos que 1 litro de tinta cobre 3 metros quadrados de parede,
e a tinta é vendia em latas de 18 litros e custa R$ 80,00, informamos ao usuario quantidade de tinta  a serem compradas
e o total a ser gasto.
Somente são vendidos um numero inteiro da latas.
'''
m = int(input('Metros: '))
if m % 54 != 0:
    latas = int(m / 54) + 1
else:
    latas = m / 54

valor = latas * 80

print('{} lata(s) de tinta, o custo total é R$ {:.2f}'. format(latas, valor))
