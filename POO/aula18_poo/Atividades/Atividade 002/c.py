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
        self.porta = {}
        self.parede = {}
        self.teto = {}
        self.chao = {}
        
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
    
    def cadastrar(self):
        pass


class Parede(Superficie):
    def __init__(self, nome, area, tipo_superficie):
        super().__init__(nome, area, tipo_superficie)
        
    def calcular_tinta(self):
        self._litros = (self._area / 10) * 4
        self._valor = self._litros * 46.50
        return f'{self._litros} litros para {self._area}m² equivalem a {self._valor}R$'

    def cadastrar(self):
        self.parede[f'Parede - {self._nome}'] = {'área' : self._area}
        return self.parede


class Teto(Superficie):
    def __init__(self, nome, area, tipo_superficie):
        super().__init__(nome, area, tipo_superficie)
        
    def calcular_tinta(self):
        self._litros = (self._area / 8) * 4
        self._valor = self._litros * 46.50
        return f'{self._litros} litros para {self._area}m² equivalem a {self._valor}R$'

    def cadastrar(self):
        self.teto[f'Teto - {self._nome}'] = {'área' : self._area}
        return self.teto


class Chao(Superficie):
    def __init__(self, nome, area, tipo_superficie):
        super().__init__(nome, area, tipo_superficie)
        
    def calcular_tinta(self):
        self._litros = (self._area / 8) * 4
        self._valor = self._litros * 46.50
        return f'{self._litros} litros para {self._area}m² equivalem a {self._valor}R$'

    def cadastrar(self):
        self.chao[f'Chão - {self._nome}'] = {'área' : self._area}
        return self.chao

class Porta(Superficie):
    def __init__(self, nome, area, tipo_superficie):
        super().__init__(nome, area, tipo_superficie)
        
    def calcular_tinta(self):
        self._litros = (self._area / 4)
        self._valor = self._litros * 46.50
        return f'{self._litros} litros para {self._area}m² equivalem a {self._valor}R$'
    
    def cadastrar(self):
        self.porta[f'Porta - {self._nome}'] = {'área' : self._area}
        return self.porta


class Cadastro(Parede, Porta, Teto, Chao): # Herança múltipla
    def __init__(self, nome, area, tipo_superficie):
        super().__init__(nome, area, tipo_superficie)
        self.dicionario = {}
    
    def cadastrar(self):
        self.dicionario[1] = self.parede
        self.dicionario[2] = self.teto
        self.dicionario[3] = self.chao
        self.dicionario[4] = self.porta
        return self.dicionario
    
    def printar(self):
        for i in self.dicionario.items():
            print(i)

def main():
    while True:
        print('\n.Porta',
            '\n.Parede',
            '\n.Teto',
            '\n.Chão'
            )
        
        tipo_superficie = input('Escolha a superfície: ').lower()
        
        print('\n.Quarto',
        '\n.Banheiro',
        '\n.Sala',
        '\n.Cozinha',
        )
        
        nome = input('De qual cômodo desejas adicionar?: ').lower()
        area = float(input('Digite a área da superfície do cômodo desejado em metros: '))
        
        if tipo_superficie == 'porta':
            obj = Porta(nome, area, tipo_superficie)
            obj.cadastrar()
        if tipo_superficie == 'parede':
            obj = Parede(nome, area, tipo_superficie)
            obj.cadastrar()
        if tipo_superficie == 'teto':
            obj = Teto(nome, area, tipo_superficie)
            obj.cadastrar()
        if tipo_superficie == 'chão' or tipo_superficie == 'chao':
            obj = Chao(nome, area, tipo_superficie)
            obj.cadastrar()
        
        opcao = input('Desejas continuar?(s/n): ').lower()
        
        if opcao == 's':
            continue
        elif opcao == 'n':
            break
        else:
            print('Inválido!!')

            

if __name__ == '__main__':
    main()