#Peça ao usuário uma citação famosa e mostre:
#A citação em letras maiúsculas e em letras minúsculas.
#Quantos caracteres ela possui (incluindo espaços).
#A quantidade de palavras na citação.
import os


os.system('cls')

frase = input('Diga uma citação famosa: ')

fraseM = frase.upper() # tudo em maiúsculo
frasem = frase.lower() # tudo em minúsculo
contar = len(frase) # conta quantos índices tem na frase

lista = frase.split() # transforma as palavras em lista
contar2 = len(lista) # conta os índices na lista

print(fraseM)
print(frasem)
print(contar)
print(lista)
print(contar)
