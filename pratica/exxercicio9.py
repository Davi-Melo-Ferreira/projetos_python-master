#Peça ao usuário uma citação famosa e mostre:
#A citação em letras maiúsculas e em letras minúsculas.
#Quantos caracteres ela possui (incluindo espaços).
#A quantidade de palavras na citação.
import os


os.system('cls')

frase = input('Diga uma citação famosa: ')

fraseM = frase.upper()
frasem = frase.lower()
contar = len(frase)

lista = frase.split()
contar2 = len(lista)

print(fraseM)
print(frasem)
print(contar)
print(lista)
print(contar)