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
    
    def __str__(self):
        return f'{self.tipo_superficie.capitalize()} - {self.nome}'

class Parede(Superficie):
    def __init__(self, nome, area, tipo_superficie):
        super().__init__(nome, area, tipo_superficie)
        
    def calcular_tinta(self):
        litros = (self._area / 10) * 4
        valor = litros * 46.50
        return litros, valor

class Teto(Superficie):
    def __init__(self, nome, area, tipo_superficie):
        super().__init__(nome, area, tipo_superficie)
        
    def calcular_tinta(self):
        litros = (self._area / 8) * 4
        valor = litros * 46.50
        return litros, valor

class Chao(Superficie):
    def __init__(self, nome, area, tipo_superficie):
        super().__init__(nome, area, tipo_superficie)
        
    def calcular_tinta(self):
        litros = (self._area / 8) * 4
        valor = litros * 46.50
        return litros, valor

class Porta(Superficie):
    def __init__(self, nome, area, tipo_superficie):
        super().__init__(nome, area, tipo_superficie)
        
    def calcular_tinta(self):
        litros = (self._area / 4)
        valor = litros * 46.50
        return litros, valor

class Cadastro:
    def __init__(self):
        self.dicionario = {}
    
    def adicionar_superficie(self, superficie):
        chave = str(superficie)
        litros, valor = superficie.calcular_tinta()
        self.dicionario[chave] = {
            'área': superficie.area,
            'litros': litros,
            'valor': valor
        }
    
    def printar(self):
        for chave, valor in self.dicionario.items():
            print(f'{chave} | Área: {valor["área"]} m² | Litros: {valor["litros"]:.2f} | Valor: R${valor["valor"]:.2f}')

def main():
    cadastro = Cadastro()
    
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
            cadastro.adicionar_superficie(obj)
        elif tipo_superficie == 'parede':
            obj = Parede(nome, area, tipo_superficie)
            cadastro.adicionar_superficie(obj)
        elif tipo_superficie == 'teto':
            obj = Teto(nome, area, tipo_superficie)
            cadastro.adicionar_superficie(obj)
        elif tipo_superficie == 'chão' or tipo_superficie == 'chao':
            obj = Chao(nome, area, tipo_superficie)
            cadastro.adicionar_superficie(obj)
        else:
            print("Superfície inválida!")
            continue
        
        opcao = input('Desejas continuar?(s/n): ').lower()
        
        if opcao == 'n':
            break
        elif opcao != 's':
            print('Opção inválida!')

    cadastro.printar()

if __name__ == '__main__':
    main()