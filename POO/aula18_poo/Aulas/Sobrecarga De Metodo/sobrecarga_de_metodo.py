# Sobrecarga de Métodos

class ClassePai:
    # Método construtor
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    # Para sobrecarregar
    # Vai ser usada para soma 2 números
    def metodo_classe(self):
        pass

class ClasseFilha(ClassePai):   # Classe derivada
    # Método construtor
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def metodo_classe(self):
        return self.a + self.b

# Programa Main
teste = ClasseFilha(1, 2)
print(teste.metodo_classe())