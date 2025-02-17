import os

class ContaBancaria:
    def __init__(self, numero_conta, nome_titular, saldo, agencia, tipo_conta):
        self.numero_conta = numero_conta
        self.nome_titular = nome_titular
        self.saldo = saldo
        self.agencia = agencia
        self.tipo_conta = tipo_conta

# Entrada de dados
print('-'*70)
os.system('cls')
numero_conta = input('Digite o número da conta: ')
nome_titular = input('Digite o nome do titular: ')
saldo = input('Digite o saldo inicial: ')
agencia = input('Digite a agência: ')
tipo_conta = input('Digite o tipo de conta: ')

# Criando um objeto da classe ContaBancaria com os dados fornecidos pelo usuário
conta = ContaBancaria(numero_conta, nome_titular, saldo, agencia, tipo_conta)

# Saída dos dados
print('-'*70)
print('\nInformações da Conta Bancária:')
print('='*70)
print(f'Número da conta: {conta.numero_conta} ')
print(f'Nome do titular: {conta.nome_titular} ')
print(f'Saldo inicial: {conta.saldo} ')
print(f'Agência: {conta.agencia} ')
print(f'Tipo de conta: {conta.tipo_conta} ')
print('-'*70)