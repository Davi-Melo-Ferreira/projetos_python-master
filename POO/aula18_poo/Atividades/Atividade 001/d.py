'''
Faça um programa que receba e divida 2 números.
A saída da divisão precisará ser formatada com 4 casas decimais.
'''
class Divisao:
    def __init__(self, a, b):
        self._a = a
        self._b = b
    
    def get_a(self):
        return self._a

    def get_b(self):
        return self._b
    
    def set_a(self, a):
        self._a = a
    
    def set_b(self, b):
        self._b = b
    
    def calcular_divisao(self):
        if self._b != 0:
            divisao = self._a / self._b
            return divisao
        else:
            return None
    
    def get_divisao(self):
        self._resultado = self.calcular_divisao()
        if self._resultado is None:
            print('Indivisível por zero!')
        else:
            return f'{self._resultado:.4f}'

valor = Divisao(9, 0)

print(valor.get_divisao())