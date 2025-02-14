'''
Faça um programa que receba um número inteiro, depois imprima sua tabuada de multiplicação.
'''
class Numero:
    def __init__(self, a):
        self.set_a(a)
    
    def get_a(self):
        return self._a

    def set_a(self, a):
        try:
            self._a = int(a)
        except ValueError:
            print(f'Número {self._a} não é inteiro.')
            self._a = None

    def gerar_tabuada(self):
         for num in range(1, 11):
            print(f'{num} x {self._a} = {num * self._a}')

numero = Numero(1)

numero.gerar_tabuada()