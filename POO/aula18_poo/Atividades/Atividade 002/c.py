'''
Obrigatório: Entrada de dados, decorator property, herança
Crie um sistema para calcular os gastos com tinta ao pintar diferentes tipos de superfícies.
A classe base Superficie deve conter os atributos nome, area (em metros quadrados) e tipo de superfície.
Ela deve ter um método calcular_tinta() que será sobrescrito nas subclasses.
A classe Parede usa 1 litro de tinta para cobrir 10 m²,
a classe Teto usa 1 litro para cobrir 8 m², e a classe Porta usa 1 litro para cobrir 4 m².
O sistema deve permitir o cadastro de múltiplas superfícies, armazená-las em uma lista,
e usar um laço for para calcular o gasto de tinta e exibir os dados de cada superfície.
Também deve ser possível filtrar as superfícies por tipo.
O objetivo é praticar o uso de listas, loops, condicionais e herança.
'''
class Superficie:
    def __init__(self, nome, area, tipo_superficie):
        self._nome = nome
        self._area = area
        self._tipo_superficie = tipo_superficie
        
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, nome):
        self._nome = nome
        
    @property
    def area(self):
        return self._area
    
    @area.setter
    def area(self, area):
        self._area = area
    
    @property
    def tipo_superficie(self):
        return self._tipo_superficie
    
    @tipo_superficie.setter
    def tipo_superficie(self, tipo_superficie):
        self._tipo_superficie = tipo_superficie
    
    def calcular_tinta(self):
        pass
    
    
class Parede(Superficie):
    def __init__(self, nome, area, tipo_superficie):
        super().__init__(nome, area, tipo_superficie)
        
    def calcular_tinta(self):
        self._litros = (self._area / 10) * 4
        self._valor = self._litros * 46.50
        return f'{self._litros} litros para {self._area}m² equivalem a {self._valor}R$'

class Teto(Superficie):
    def __init__(self, nome, area, tipo_superficie):
        super().__init__(nome, area, tipo_superficie)
        
    def calcular_tinta(self):
        self._litros = (self._area / 8) * 4
        self._valor = self._litros * 46.50
        return f'{self._litros} litros para {self._area}m² equivalem a {self._valor}R$'


class Porta(Superficie):
    def __init__(self, nome, area, tipo_superficie):
        super().__init__(nome, area, tipo_superficie)
        
    def calcular_tinta(self):
        self._litros = (self._area / 4) * 4
        self._valor = self._litros * 46.50
        return f'{self._litros} litros para {self._area}m² equivalem a {self._valor}R$'

nome = input('Nome: ').lower()
area = float(input('Area: '))
tipo_superficie = input('Tipo de superfície(porta, parede, teto): ').lower()

if tipo_superficie == 'parede':
    obj = Parede(nome, area, tipo_superficie)
    print(obj.calcular_tinta())
elif tipo_superficie == 'porta':
    obj = Porta(nome, area, tipo_superficie)
    print(obj.calcular_tinta())
elif tipo_superficie == 'teto':
    obj = Teto(nome, area, tipo_superficie)
    print(obj.calcular_tinta())

superficies = []
    
superficies.append(Porta(nome, area))
superficies.append(Teto(nome, area))

for superficie in superficies:
    print(superficie)