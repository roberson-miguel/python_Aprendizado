# inserindo repetidamente. for w in words:biosbuginformatica
words = ['teste', 'casas', 'biosbuginformatica']

for w in words[:]:  #looping na lista inteira procurando os valores de tamanho acima de 6 para W
    if len(w) > 6:
        words.insert(0, w) #inserindo a palavra maior que 6 na posição indicada
print(words)

