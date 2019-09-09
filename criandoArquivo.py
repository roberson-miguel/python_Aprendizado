fileName = input("Digite um nome para o arquivo: ")
fileName = fileName + ".txt" #concatenando a string digitada pelo usuário para ter a extensão .txt
arq3 = open(fileName, "w") #abrindo arquivo nomeado pelo usuario no input para escrita 'wirte'
arq3.write(input("Digite algum texto: ")) #recebendo texto para gravar no arquivo
arq3.close()


