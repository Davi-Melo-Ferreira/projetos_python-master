'''
Faça um programa que peça o ano do seu nascimento e calcule a sua idade.
'''

import datetime

class Pessoa:
    def __init__(self, data_nascimento):
        
        self.set_data_nascimento(data_nascimento)

    def get_data_nascimento(self):
        return self._data_nascimento
    
    def set_data_nascimento(self, data_nascimento):
        self._ano_nascimento = data_nascimento

        hoje = datetime.datetime.now()

        nascimento = datetime.datetime.strptime(data_nascimento, '%d/%m/%Y')

        self._idade = hoje.year - nascimento.year -\
            ((hoje.month, hoje.day) < (nascimento.month, nascimento.day))
    
    def get_idade(self):
        return self._idade

data_nascimento = input('Digite sua data de nascimento: ')

pessoa = Pessoa(data_nascimento)

print(pessoa.get_idade())