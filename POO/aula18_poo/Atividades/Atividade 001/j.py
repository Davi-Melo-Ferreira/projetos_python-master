'''
Faça um programa com entrada de dados para calcular o perímetro de um retângulo.
'''

class Retangulo:
    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c
        
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
    
    def calcular_perimetro(self):
        self._perimetro = self._a + self._b + self._c

    def get_perimetro(self):
        self.calcular_perimetro()
        return self._perimetro

def main():
    import os
    a = int(input('Digite o primeiro valor: '))
    b = int(input('Digite o segundo valor: '))
    c = int(input('Digite o terceiro valor: '))
 
    perimetro = Retangulo(a, b, c)
    
    os.system('cls')
    print(f'O perímetro de {a}, {b} e {c} é: {perimetro.get_perimetro()}')

if __name__ == '__main__':
    main()