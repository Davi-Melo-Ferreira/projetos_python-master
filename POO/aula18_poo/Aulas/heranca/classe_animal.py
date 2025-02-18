import os

# class Animal:
#     def __init__(self, nome):
#         self.nome = nome
    
#     def latir(self):
#         return 'Isto está no método latir()'
    
#     def miar(self):
#         return 'Isto está no método miar()'

# class Cachorro(Animal):
#     def latir(self):
#         return f'{self.nome} está latindo!'

# class Gato(Animal):
#     def miar(self):
#         return f'{self.nome} está miando!' 

# os.system('cls')
# cao = Cachorro('Rex')
# gato = Gato('Tobias')
# print(cao.latir())
# print(gato.miar())

import os

class Animal:  # Definição da classe "Animal" - Classe base ou superclasse
    def __init__(self, nome):  # Método construtor (initializer) que define o atributo 'nome'
        self.nome = nome  # Atributo de instância que armazena o nome do animal
    
    def latir(self):  # Método 'latir' na classe Animal - Método da superclasse
        return 'Isto está no método latir()'  # Retorna um comportamento padrão de latido
    
    def miar(self):  # Método 'miar' na classe Animal - Método da superclasse
        return 'Isto está no método miar()'  # Retorna um comportamento padrão de miado

class Cachorro(Animal):  # "Cachorro" herda de "Animal" - Herança (subclasse de Animal)
    def latir(self):  # Sobrescrita do método latir() - Polimorfismo
        return f'{self.nome} está latindo!'  # Sobrescreve o método latir com comportamento específico para Cachorro

class Gato(Animal):  # "Gato" herda de "Animal" - Herança (subclasse de Animal)
    def miar(self):  # Sobrescrita do método miar() - Polimorfismo
        return f'{self.nome} está miando!'  # Sobrescreve o método miar com comportamento específico para Gato

os.system('cls')  # Limpa o terminal (para Windows, no Linux seria 'clear')
cao = Cachorro('Rex')  # Criação de uma instância (objeto) da classe Cachorro
gato = Gato('Tobias')  # Criação de uma instância (objeto) da classe Gato

print(cao.latir())  # Chama o método latir() da classe Cachorro, que foi sobrescrito
print(gato.miar())  # Chama o método miar() da classe Gato, que foi sobrescrito
