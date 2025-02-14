'''
Faça um programa que converta metros em centímetros e milímetros.
1m = 100cm = 1000mm
'''
class Medida:
    def __init__(self, a):
        self.set_a(a)
        
    def get_a(self):
        return self._a
    
    def set_a(self, a):
        self._a = a

    def converter_em_centimetros(self):
        return self._a * 100
    
    def get_centimetros(self):
        self.centimetros = self.converter_em_centimetros()
        return f'{self._a} metro em centímetros é {self.centimetros}'

    def converter_em_milimetros(self):
        return self._a * 100

    def get_milimtetros(self):
        self.milimetros = self.converter_em_milimetros()
        return f'{self._a} metro em milímetros é {self.milimetros}'

metro = Medida(1)

centimetros, milimetros = metro.get_centimetros(), metro.get_milimtetros()
print(centimetros)
print(milimetros)