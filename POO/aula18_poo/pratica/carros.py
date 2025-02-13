class Carro:
    def __init__(self, marca, cor, ano, velocidade):
        self.marca = marca
        self.cor = cor
        self.ano = ano
        self.velocidade = velocidade
    
    def acelerar(self):
        self.velocidade += 10
        print(f'Velocidade aumentou para {self.velocidade}')
    
    def desacelerar(self):
        if self.velocidade < 11:
            input('Velocidade não pode ser menor que 0.')
            pass
        else:
            self.velocidade -= 10
            print(f'Velocidade diminuiu para {self.velocidade}')
            
    def informar(self):
        print(f'marca: {self.marca},\ncor: {self.cor},')
        print(f'ano: {self.ano},\nvelocidade: {self.velocidade}')

 
carro1 = Carro('camaro', 'amarelo', '2019', 60)

carro1.acelerar()
carro1.desacelerar()
carro1.informar()