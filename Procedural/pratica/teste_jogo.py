import os

class Vinho:
    def __init__(self, nome, tipo, teor_alcoolico, safra):
        self.nome = nome
        self.tipo = tipo
        self.teor_alcoolico = teor_alcoolico
        self.safra = safra

nome = input('Digite o nome: ')
tipo = input('Digite o nome: ')
teor_alcoolico = input('Digite o nome: ')
safra = input('Digite o nome: ')

vinho1 = Vinho(nome, tipo, teor_alcoolico, safra)