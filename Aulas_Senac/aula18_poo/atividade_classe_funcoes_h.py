# Uma Academia deseja fazer uma pesquisa entre seus clientes para descobrir
# a média de altura  e peso de seus clientes.
# Faça um programa que pergunte a cada um dos clientes da academia seu
# código, nome, altura e peso.
# Após esse cadastramento, seu programa deverá listar os dados dos clientes e a média.
# Para sair do programa o usuário deverá digitar o valor zero(0).
# O número de clientes é indefinido. Veja a saída no próximo slide.
import os

class Cliente:
    def __init__(self, codigo, nome, altura, peso, dicionario):
        self.codigo = codigo
        self.nome = nome
        self.altura = altura
        self.peso = peso
        self.dicionario = dicionario
        self.peso_total = 0
        self.altura_total = 0
        self.media_peso = 0
        self.media_altura = 0
        
    def cadastrar(self):
        self.dicionario[self.codigo] = {'nome': self.nome, 'altura': self.altura, 'peso': self.peso}
        return self.dicionario
    
    def gerar_somas(self):
        for valor in self.dicionario.values():
            self.peso_total += valor['peso']
            self.altura_total += valor['altura']
    
    def gerar_media(self):
        self.gerar_somas()
        self.media_altura = self.altura_total / len(self.dicionario)
        self.media_peso = self.peso_total / len(self.dicionario)
        return self.media_altura, self.media_peso


# programa Main
dicionario_clientes = {}
opcao = 's'
while opcao == 's' or opcao != '0':
    # entrada de dados
    codigo = int(input('Digite seu código: '))
    nome = input('Digite seu nome: ')
    altura = float(input('Digite sua altura: '))
    peso = float(input('Digite seu peso: '))
    
    # criando objeto cadastro
    cadastro = Cliente(codigo, nome, altura, peso, dicionario_clientes)
    
    # aplicando método cadastrar
    cadastro.cadastrar()
    
    # printa o dicionário
    print(dicionario_clientes)
    
    opcao = input('Deseja continuar?(s/0): ').lower()

os.system('cls')
altura, peso = cadastro.gerar_media()
print(f'Média Altura: {altura}, Média Peso: {peso}')