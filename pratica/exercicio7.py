#Receba um nome completo no formato "Nome Sobrenome" e substitua o primeiro nome por "Dr." ou "Dra.", dependendo do gênero. Exiba o nome completo modificado.
import os

os.system('cls')

genero = input('Seu gênero é Masculino ou Feminino?: ')
nome = input('Diga seu nome e sobrenome: ')
generom = genero.lower()
nomem = nome.lower()
nomeM = nome.capitalize()
lista = nomeM.split()

if genero == 'feminino':
    print(f'Dra. {lista[1].capitalize()}')
else:
    if genero == 'masculino':
        print(f'Dr. {lista[1].capitalize()}')