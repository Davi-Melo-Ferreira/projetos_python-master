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
import os

class Superficie:
    """
    Classe base para representar uma superfície (parede, teto, porta) de um cômodo.
    Possui métodos para manipulação de atributos e cálculo da quantidade de tinta necessária.
    """
    def __init__(self, comodo, area, tipo_superficie):
        self._comodo = comodo
        self._area = area
        self._tipo_superficie = tipo_superficie

    @property #linha 25 - 52 property para proteger atributos
    def comodo(self): # método acessor
        """Retorna o nome do cômodo"""
        return self._comodo

    @comodo.setter # método modificador
    def comodo(self, comodo):
        """Define o nome do cômodo"""
        self._comodo = comodo

    @property
    def area(self):
        return self._area

    @area.setter
    def area(self, area):
        self._area = area

    @property
    def tipo_superficie(self):
        """Retorna o tipo da superfície (parede, teto, porta)"""
        return self._tipo_superficie

    @tipo_superficie.setter
    def tipo_superficie(self, tipo_superficie):
        """Define o tipo de superfície."""
        self._tipo_superficie = tipo_superficie

    def calcular_tinta(self): #linha 54 - 62: métodos
        """Método abstrato para calcular a quantidade de tinta necessária.
        Deve ser sobrescrito nas subclasses"""
        pass

    def descricao(self):
        """Retorna uma string formatada com a descrição da superfície"""
        return f'\nCômodo {self._comodo} - '\
            f'Tipo: {self._tipo_superficie} - Área: {self._area}m²'

class Parede(Superficie): # linha 64 - 87: classes derivadas
    """Classe que representa uma parede de um cômodo"""
    def __init__(self, comodo, area):
        super().__init__(comodo, area, 'Parede') # chama o método construtor da classe base Superficie

    def calcular_tinta(self): #método sobrescrito
        return self._area / 10

class Teto(Superficie):
    """Classe que representa um teto de um cômodo"""
    def __init__(self, comodo, area):
        super().__init__(comodo, area, 'Teto')

    def calcular_tinta(self):
        return self._area / 8

class Porta(Superficie):
    """Classe que representa uma porta de um cômodo"""
    def __init__(self, comodo, area):
        super().__init__(comodo, area, 'Porta')

    def calcular_tinta(self):
        """Calcula a quantidade de tinta necessária para pintar uma porta (1 litro cobre 4m²)"""
        return self._area / 4

class CadastroSuperficie: # linha 88 - 176: classe CadastroSuperfície
    """
    Classe responsável por coletar as entradas do usuário, armazenar as superfícies e realizar cálculos
    """
    def __init__(self):
        self.lista_instancias = []

    def entrar_com_dados(self):
        os.system('cls')
        """
        Coleta dados do usuário sobre um cômodo e cria a superfície correspondente (parede, teto ou porta).
        """
        comodo = input('Nome do cômodo: ').lower().capitalize() #linha 101 - 111: entrada de dados
        tipo_superficie = input('Tipo de superfície '
                                '(porta, parede, teto): ').capitalize()
        while True:
            area = input('Área da superfície em m²: ')
            if area.isnumeric():
                area = float(area)
                break
            else:
                input('Valor inválido!')
            
        # criando a instância correspondente ao tipo escolhido
        if tipo_superficie == 'Parede': # linha 114 - 122: criando instâncias
            obj = Parede(comodo, area)
        elif tipo_superficie == 'Porta':
            obj = Porta(comodo, area)
        elif tipo_superficie == 'Teto':
            obj = Teto(comodo, area)
        else:
            print("Tipo de superfície inválido!")

        self.lista_instancias.append(obj) # adiciona a instância criada a uma lista
        print(f'{obj.descricao()} adicionado!')
        
        
    def exibir_superficies(self):
        """Exibe as superfícies cadastradas e a quantidade de tinta necessária para cada uma."""
        for obj in self.lista_instancias:
            print(f'{obj.descricao()} - '
                  f'Tinta necessária: {obj.calcular_tinta():.2f} litro(s)')

    def filtrar_por_tipo(self):
        """
        Permite filtrar as superfícies por tipo (parede, teto, porta).
        """
        tipo_filtro = input('Digite o tipo para filtrar'
                            '(parede, teto, porta): ').strip().capitalize()
        if tipo_filtro not in ['Parede', 'Teto', 'Porta']:
            print("Tipo inválido!")
        else:
            encontrado = False
            for obj in self.lista_instancias:
                if obj.tipo_superficie == tipo_filtro:
                    print(f'{obj.descricao()} - Tinta necessária:'
                          f' {obj.calcular_tinta():.2f} litro(s)')
                    encontrado = True # se o loop for feito é porque foi encontrado o tipo de filtro
            if not encontrado:
                input('Não encontrado! Pressione qualquer tecla...')


    def calcular_total_tinta(self):
        """Calcula e exibe a quantidade total de tinta necessária para todas as superfícies cadastradas."""
        total_tinta = 0
        for obj in self.lista_instancias:
            total_tinta += obj.calcular_tinta()
        print(f'\nTotal de tinta gasta: {total_tinta:.2f} litro(s)')

    def executar(self):
        """
        Executa o fluxo principal do programa, coletando dados, exibindo informações e realizando cálculos.
        """
        self.entrar_com_dados() # aplicando método
        while input('\nDeseja continuar? (s/any): ').strip().lower() == 's': # linha 161 - 165: loop while para entrada de dados
            self.entrar_com_dados() # aplicando método

        os.system('cls')
        self.exibir_superficies() #método de superfície
        self.calcular_total_tinta()
        
        while input('\nDeseja filtrar por tipo de superfície?' #loop while para filtrar por tipo
                    '(s/any): ').strip().lower() == 's':
            self.filtrar_por_tipo()
        input('Pressione qualquer tecla para sair...')
        os.system('cls')