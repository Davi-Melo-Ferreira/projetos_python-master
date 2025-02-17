import math
import os

class Triangulo:
    def __init__(self, cateto_op, cateto_adj):
        self.cateto_op = cateto_op
        self.cateto_adj = cateto_adj

class TrianguloRetangulo(Triangulo):
    def calcular_hipotenusa(self):
        resultado = math.sqrt(pow(self.cateto_op, 2) + pow(self.cateto_adj, 2))
        return resultado

while True:
    os.system('cls')
    cateto_op = float(input('Entre com o cateto oposto: '))
    cateto_adj = float(input('Entre com o cateto adjacente: '))
    
    if cateto_op == 0 or cateto_op == 0:
        print('Fim do programa!')
        break
    else:
        triangulo_retangulo = TrianguloRetangulo(cateto_op, cateto_adj)
        hipotenusa = triangulo_retangulo.calcular_hipotenusa()
        
        os.system('cls')
        
        print(f'O triângulo retângulo de lado 1 = {cateto_op} e')
        print(f'de lado 2 = {cateto_adj} é igual a {hipotenusa:.2f} aproximadamente!')
        input('Pressione Enter para retornar...')
