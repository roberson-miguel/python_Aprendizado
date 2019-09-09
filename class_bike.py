class Bike:
    quadro = 1
    banco = 1
    guidao = 1
    pedais = 2
    rodas = 2

    def __init__(self, cor, tam, dono):
        self.cor = cor
        self.tam = tam
        self.dono = dono

# bike1_quadro = Bike.quadro - na primeira vez atribui as variaveis e não é necessário
# bike1_pedais = Bike.pedais - na primeira vez atribui as variaveis e não é necessário

bike1_det = Bike('preta', 19, 'Roberson')

print('A bike1 tem {} quadro tamanho {}, {} pedais, sua cor é {} e pertence ao {}'
      .format(
                Bike.quadro,
                bike1_det.tam,
                Bike.pedais,
                bike1_det.cor,
                bike1_det.dono
              ))