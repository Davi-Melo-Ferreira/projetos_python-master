'''
Faça um programa que receba um número qualquer e calcule o dobro e o triplo desse número.
'''
class Numero:
    def __init__(self, a):
        self.set_a(a)

    def get_a(self):
        return self._a
    
    def set_a(self, a):
        self._a = a
    
    def calcular_dobro(self):
        return self._a * 2

    def get_dobro(self):
        dobro = self.calcular_dobro()
        return dobro

    def calcular_triplo(self):
        return self._a * 3

    def get_triplo(self):
        triplo = self.calcular_triplo()
        return triplo

numero = Numero(3)

print(f'Dobro de {numero.get_a()} = {numero.get_dobro()}\n'
      f'Triplo de {numero.get_a()} = {numero.get_triplo()}')