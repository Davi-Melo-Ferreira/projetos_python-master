'''
Faça um programa que receba e divida 2 números.
A saída da divisão precisará ser formatada com 4 casas decimais.
'''
class Divisao:
    def __init__(self, a, b):
        self._a = a
        self._b = b
    
    @property
    def a(self):
        return self._a
    
    @a.setter
    def a(self, a):
        self._a = a

    @property
    def b(self):
        return self._b
    
    @b.setter
    def b(self, b):
            if b != 0:
                self._b = b
            else:
                self._b = None
    
    def calcular_divisao(self):
        if self.b is None:
            return None
        else:
            return self.a / self.b
    
    def get_divisao(self):
        resultado = self.calcular_divisao()
        if resultado is None:
            print('Indivisível por zero!')
        else:
            return f'{resultado:.4f}'

valor = Divisao(9, 0)

print(valor.get_divisao())