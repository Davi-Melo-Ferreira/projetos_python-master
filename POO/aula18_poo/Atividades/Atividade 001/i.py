'''
Faça um programa que receba um valor em reais,
depois calcule quantos dólares daria para comprar com esse valor.
'''
class Convercao:
    def __init__(self, real):
        self.set_real(real)
    
    def get_real(self):
        return self._real
    
    def set_real(self, real):
        self._real = real
    
    def converter_real(self):
        self._dolar = self._real / 5.00
        return self._dolar
    
    def get_conversao(self):
        return f'R${self._real} equivale a {self.converter_real():.2f}$'

real = Convercao(5)

print(real.get_conversao())