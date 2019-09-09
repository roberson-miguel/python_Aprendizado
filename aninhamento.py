minutos = int(input("minutos usados:"))
if minutos < 200:
    preco = 0.20
else:
    if minutos <= 400:
        preco = 0.18
    else:
        if minutos <= 800:
            preco = 0.15
        else:
            preco = 0.08
print("Conta telefonica: {:.2f}" .format(minutos * preco))
