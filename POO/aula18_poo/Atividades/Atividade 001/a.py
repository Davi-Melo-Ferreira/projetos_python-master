'''
Faça um programa que peça 3 valores,
depois calcule e imprima  a soma e a multiplicação desses valores
'''
import os

class Equacao:
    def __init__(self, a, b, c):
        # Chama o setter para definir o valor a
        self.set_a(a)
        # Chama o setter para definir o valor b
        self.set_b(b)
        # Chama o setter para definir o valor c
        self.set_c(c)

    def get_a(self):
        return self._a
    
    def set_a(self, a):
        self._a = a
    
    def get_b(self):
        return self._b
    
    def set_b(self, b):
        self._b = b
    
    def get_c(self):
        return self._c
    
    def set_c(self, c):
        self._c = c
    
    def calcular_soma(self): 
        self._somatorio = self._a + self._b + self._c
    
    def get_somatorio(self):
        self.calcular_soma()
        return self._somatorio
    
    def calcular_multiplicacao(self):
        self._multiplicado = self._a * self._b * self._c
    
    def get_multiplicacao(self):
        self.calcular_multiplicacao()
        return self._multiplicado

    def printar(self):
        print(f'A soma dos valores {self._a} + {self._b} + {self._c} = {self.get_somatorio()}')
        print(f'A multiplicação dos valores {self._a} x {self._b} x {self._c} = {self.get_multiplicacao()}')
    
os.system('cls')

a = int(input('Digite o valor de a: '))
b = int(input('Digite o valor de b: '))
c = int(input('Digite o valor de c: '))

equacao = Equacao(a, b, c)

equacao.printar()