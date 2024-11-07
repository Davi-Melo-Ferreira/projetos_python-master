#Peça ao usuário para digitar três palavras separadamente e, em seguida, junte-as para formar uma frase completa. Exiba essa frase na tela.
import os


os.system('cls')

print('-'*70)
print('Junção de Três Palavras')
print('-'*70)
palavra1 = input('Cite um Sujeito(Pessoa): ')
palavra2 = input('Diga um Verbo(Ação): ')
palavra3 = input('Diga um Complemento(Objeto): ')

lista = [palavra1, palavra2, palavra3]
juncao = ' '.join(lista)

print(f'{juncao}')
print('-'*70)
print('FIM')









print('-'*70)
print('FIM')