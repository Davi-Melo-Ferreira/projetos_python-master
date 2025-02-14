'''
Faça um programa que receba um número inteiro e mostre o sucessor e antecessor.
'''
class Numero:
    def __init__(self, a):
        self.set_a(a)

    
    def get_a(self):
        return self._a
    
    def set_a(self, a):
        self._a = a
    
    def mostrar_sucessor_antecessor(self):
        return self._a + 1, self._a - 1

    def get_sucessor_antecessor(self):
        sucessor, antecessor = self.mostrar_sucessor_antecessor()
        return f'antecessor: {antecessor}, sucessor: {sucessor}'

valor = Numero(2)

print(f'{valor.get_sucessor_antecessor()}')