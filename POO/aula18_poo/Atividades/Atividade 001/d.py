'''
Faça um programa que receba e divida 2 números.
A saída da divisão precisará ser formatada com 4 casas decimais.
'''
class Divisao:
    def __init__(self, a, b):
        self.set_a(a)
        self.set_b(b)
    
    def get_a(self):
        return self._a
    
    def set_a(self, a):
        self._a = a

    def get_b(self):
        return self._b
    
    def set_b(self, b):
        self._b = b
    
    def calcular_divisao(self):
        return self._a / self._b
    
    def get_divisao(self):
        resultado = self.calcular_divisao()
        return f'{resultado:.4f}'

valor = Divisao(9, 3)

print(valor.get_divisao())