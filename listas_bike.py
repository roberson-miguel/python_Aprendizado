peca1 = input('Digite acessório do guidão: ')
bike = {}
bike['guidao'] = peca1
print(bike)
peca2 = input('Digite acessório do quadro: ')
bike2 = {}
bike2['quadro'] = peca2
bike.update(bike2)
print(bike)
print(bike.keys())
print(bike.values())





