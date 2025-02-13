'''
Faça um programa que peça o ano do seu nascimento e calcule a sua idade.
'''
import os
import datetime

class Pessoa:
    def __init__(self, ano_nascimento):
        
        self.set_ano_nascimento(ano_nascimento)
    
    def calcular_idade(self):
        ano_atual = datetime.now()
        
        pass