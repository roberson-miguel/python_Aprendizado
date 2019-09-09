#multar velocidade acima de 110km/h em R$ 5.00 por km/h acima do limite
v = int(input('Digite a velocidade:'))
if v > 110:
    print()
    print('Voce foi multado')
    multa = (v-110)*5
    print("Multa a pagar no valor de R$ {:.2f}".format(multa))
else:
    print("voce não foi multado")

