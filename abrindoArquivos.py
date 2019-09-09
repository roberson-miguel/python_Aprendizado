arq1 = open("D:/Users/Roberson/Google Drive/Python/Data Science Academy/Cap04/Notebooks/arquivos/arquivo1.txt", "r", encoding="utf8")

print(arq1.read())
print(arq1.tell()) #numero de caracteres no arquivo
print(arq1.seek(0, 0)) #primeira linha primeira coluna
print(arq1.read(12)) #ler e imprimi aparti do caracter XX


