from random import *

frase = ("Se acelera nem é bike")
print(frase)
print()
lista_frase = frase.split() #transformo a frase numa lista
print(lista_frase)
print()
palavra_lista = lista_frase[1] #atribuo a palavra na posição 1 da lista a variavel
print("Palavra na posição 1 da lista: ", palavra_lista)
print()
print("Print da frase substituindo a palavra da posição 1 por palavra invertida de frase: ")
print("*****", frase.replace(palavra_lista, frase[9:2:-1])) #substituindo palavra usando variavel
print()
tam_lista_frase = len(lista_frase)
print("Numero de palavras na frase: ", tam_lista_frase)
print()

print("Frase exibida já com randômico variavel")

sort_palavra = randrange(0, tam_lista_frase) # atribuo a variavel um numero randomico de zero até o tamanho da frase
palavra_lista = lista_frase[sort_palavra] #atribuo a palavra na posição 1 da lista a variavel
print(frase.replace(palavra_lista, palavra_lista[::-1])) #substituindo palavra usando variavel

items = [1, 2, 3, 20, 10, 4, 5, 6, 7]
print(sorted(items))
