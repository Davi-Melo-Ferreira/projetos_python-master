# Crie uma lista com 6 nomes, depois verifique se o nome ‘Pedro’ está nessa lista.
import os


os.system('cls')
num = int
lista_n = []
while len(lista_n) < 6:
    for i in range(1, 6):
        print(len(lista_n))
        entrada = input('Digite um nome: ').lower()
        lista_n.append(entrada)       
    break
print(lista_n)