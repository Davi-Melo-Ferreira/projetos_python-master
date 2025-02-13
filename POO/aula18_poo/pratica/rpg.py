# class Avatar:
#     def __init__(self, vida, stamina, defesa, ataque, esquiva):
#         self.vida = vida
#         self.stamina = stamina
#         self.defesa = defesa
#         self.ataque = ataque
#         self.esquiva = esquiva

pts = 20

hp = int(input('HP: '))
stamina = int(input('STAMINA: '))
defesa = int(input('DEFESA: '))
ataque = int(input('ATAQUE: '))
esquiva = int(input('ESQUIVA: '))

lista = [hp, stamina, defesa, ataque, esquiva]

for i in lista:
    pts -= i
print(f'Você possui {pts} para distribuir')

    