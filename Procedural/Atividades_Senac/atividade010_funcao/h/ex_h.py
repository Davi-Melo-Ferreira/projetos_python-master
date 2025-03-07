# Uma Academia deseja fazer uma pesquisa entre seus clientes para descobrir
# a média de altura  e peso de seus clientes.
# Faça um programa que pergunte a cada um dos clientes da academia seu
# código, nome, altura e peso.
# Após esse cadastramento, seu programa deverá listar os dados dos clientes e a média.
# Para sair do programa o usuário deverá digitar o valor zero(0).
# O número de clientes é indefinido. Veja a saída no próximo slide.
import os

from modulo_h import cadastrar, gerar_somas
os.system('cls')

dicionario = {}
opcao = 's'
while opcao == 's':
    
    codigo = int(input('Digite seu código: '))
    nome = input('Digite seu nome: ')
    altura = float(input('Digite sua altura: '))
    peso = float(input('Digite seu peso: '))

    cadastrados = cadastrar(codigo, nome, altura, peso, dicionario)

    opcao = input('Digite "s" para adicionar um cliente ou "0" para sair: ')
    
    # limpar o codigo
    os.system('cls')
    
    if opcao == '0':
        break

soma_altura, soma_peso = gerar_somas(cadastrados)

media_altura = soma_altura / len(cadastrados)
media_peso = soma_peso / len(cadastrados)

for codigo, dicionario in cadastrados.items():
    print(f'Cliente de código {codigo}:\n Nome: {nome} - Altura: {altura} - Peso: {peso}.\n')

print(f'A média de altura dos clientes é de {media_altura:.2f}')
print(f'A média do peso dos clientes é de {media_peso:.2f}\n')
