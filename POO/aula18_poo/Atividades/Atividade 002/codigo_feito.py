import os


class Superficie:
    def __init__(self, comodo, area, tipo_superficie):
        self._comodo = comodo
        self._area = area
        self._tipo_superficie = tipo_superficie
        
    @property
    def comodo(self):
        return self._comodo
    
    @comodo.setter
    def comodo(self, comodo):
        self._comodo = comodo
        
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
    
    def calcular_tinta(self): # método abstrato
        pass

    def descricao(self): # método retorna uma string com informações da superfície
        return f'Cômodo {self._comodo} - Tipo: {self.tipo_superficie} - Área: {self.area}m²'
    
    
class Parede(Superficie):
    def __init__(self, comodo, area, tipo_superficie):
        super().__init__(comodo, area, 'Parede')# define que tipo sempre será Parede
        
    def calcular_tinta(self): # método para calcular tinta
        self._litros = self._area / 10
        return self._litros

class Teto(Superficie):
    def __init__(self, comodo, area, tipo_superficie):
        super().__init__(comodo, area, 'Teto')# define que tipo sempre será Teto
        
    def calcular_tinta(self): # método para calcular tinta
        self._litros = self._area / 8
        return self._litros


class Porta(Superficie):
    def __init__(self, comodo, area, tipo_superficie):
        super().__init__(comodo, area, 'Porta')# define que tipo sempre será Porta
        
    def calcular_tinta(self): # método para calcular tinta
        self._litros = self._area / 4
        return self._litros

class GerenciadorSuperficie:
    def __init__(self):
        self.lista_superficies = []

    def entrar_com_dados(self):
        comodo = input('Nome do comodo: ').lower().capitalize()
        tipo_superficie = input('Tipo de superfície(porta, parede, teto): ').capitalize()
        area = float(input('Area da superfície: '))

        if tipo_superficie == 'Parede':
            obj = Parede(comodo, area, tipo_superficie)

        elif tipo_superficie == 'Porta':
            obj = Porta(comodo, area, tipo_superficie)

        elif tipo_superficie == 'Teto':
            obj = Teto(comodo, area, tipo_superficie)
        
        self.lista_superficies.append(obj)
        print(f'{obj.descricao()} adicionado!')
        
    def calcular_total_tinta(self):
        pass
    
    def exibir_superficies(self):
        for s in self.lista_superficies:
            print(f'{s.descricao()} - Tinta necessária: {s.calcular_tinta():.2f} litros')
    
    def filtrar_por_tipo(self):
        tipo_filtro = input('Digite o tipo para filtrar (parede, teto, porta): ').strip().capitalize()
        filtrados = [s for s in self.lista_superficies if s.tipo_superficie == tipo_filtro]
        
        if filtrados:
            for s in filtrados:
                print(f'{s.descricao()} - Tinta necessária: {s.calcular_tinta():.2f} litros')
        else:
            print('Nenhuma superfície encontrada para esse tipo.')
    
    def executar(self):
        while True:
            self.adicionar_superficie()
            if input('Deseja continuar? (s/n): ').strip().lower() != 's':
                os.system('cls' if os.name == 'nt' else 'clear')
                break
        
        self.exibir_superficies()
        self.calcular_total_tinta()
        
        while input('\nDeseja filtrar por tipo de superfície? (s/n): ').strip().lower() == 's':
            self.filtrar_por_tipo()

if __name__ == '__main__':
    gerenciador = GerenciadorSuperficie()
    gerenciador.executar()