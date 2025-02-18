# Uma Academia deseja fazer uma pesquisa entre seus clientes para descobrir
# a média de altura  e peso de seus clientes.
# Faça um programa que pergunte a cada um dos clientes da academia seu
# código, nome, altura e peso.
# Após esse cadastramento, seu programa deverá listar os dados dos clientes e a média.
# Para sair do programa o usuário deverá digitar o valor zero(0).
# O número de clientes é indefinido. Veja a saída no próximo slide.

# class Cliente:
#     def __init__(self, codigo, nome, altura, peso):
#         self.codigo = codigo
#         self.nome = nome
#         self.altura = altura
#         self.peso = peso
#         self.dicionario = {}
#         self.peso_total = 0
#         self.altura_total = 0
#         self.media_peso = 0
#         self.media_altura = 0
        
#     def cadastrar(self):
#         self.dicionario[self.codigo] = {'nome': self.nome, 'altura': self.altura, 'peso': self.peso}
#         return self.dicionario
    
#     def gerar_somas(self):
#         for valor in self.dicionario.values():
#             self.peso_total += valor['peso']
#             self.altura_total += valor['altura']
    
#     def gerar_media(self):
#         self.gerar_somas()
#         self.media_altura = self.altura_total / len(self.dicionario)
#         self.media_peso = self.peso_total / len(self.dicionario)
#         return self.media_altura, self.media_peso

#     def printar(self):
#         for chave, valor in self.dicionario.items():
#             print(f'{chave}: {valor}')
# # programa Main

# opcao = 's'
# while opcao == 's' or opcao != '0':
#     # entrada de dados
#     codigo = int(input('Digite seu código: '))
#     nome = input('Digite seu nome: ')
#     altura = float(input('Digite sua altura: '))
#     peso = float(input('Digite seu peso: '))
    
#     # criando objeto cadastro
#     cadastro = Cliente(codigo, nome, altura, peso)

#     # aplicando método cadastrar
#     cadastro.cadastrar()
    
#     opcao = input('Deseja continuar?(s/0): ').lower()

# altura, peso = cadastro.gerar_media()
# cadastro.printar()
# print()
# print(f'Média Altura: {altura}, Média Peso: {peso}')


class Cliente:
    def __init__(self, codigo, nome, altura, peso):
        self.codigo = codigo
        self.nome = nome
        self.altura = altura
        self.peso = peso

class CadastroClientes:
    def __init__(self):
        self.clientes = []

    def adicionar_cliente(self, cliente):
        self.clientes.append(cliente) # adiciona cliente a lista clientes

    def calcular_medias(self):
        if not self.clientes: # se lista estiver vazia
            return 0, 0 # retorna zero
        total_altura = sum(cliente.altura for cliente in self.clientes) # soma altura
        total_peso = sum(cliente.peso for cliente in self.clientes) # soma peso
       
         # retorna média
        return total_altura / len(self.clientes), total_peso / len(self.clientes)
    
    def listar_clientes(self):
        print()

# classe que executa o programa
class Aplicacao:
    def __init__(self):
        self.cadastro = CadastroClientes()

    def executar(self):
        opcao = 's'
        while opcao == 's' or opcao != '0':
            codigo = int(input('Digite seu código: '))
            nome = input('Digite seu nome: ')
            altura = float(input('Digite sua altura: '))
            peso = float(input('Digite seu peso: '))
           
            # Criação do objeto Cliente com os dados fornecidos
            cliente = Cliente(codigo, nome, altura, peso)

            # Adiciona o cliente ao cadastro
            self.cadastro.adicionar_cliente(cliente)

            opcao = input('Deseja continuar? (s/0): ').lower()

        media_altura, media_peso = self.cadastro.calcular_medias() # unpacking
        print(f'Média Altura: {media_altura:.2f}, Média Peso: {media_peso:.2f}')
print()