
import os


os.system('cls')

seg = int(input('livros emprestados na segunda?: '))
ter = int(input('livros emprestados na terça?: '))
qua = int(input('livros emprestados na quarta?: '))
qui = int(input('livros emprestados na quinta?: '))
sex = int(input('livros emprestados na sexta?: '))

total_livros = seg + ter + qua + qui + sex
media = total_livros / 5

if seg > ter and seg > qua and seg > qui and seg > sex:
    print('Segunda é o maior ')
elif ter > qua and ter > qui and ter > sex:
    print('Terça é o maior')
elif qua > qui and qua > sex:
    print('Quarta é o maior')
elif qui > sex:
    print('Quinta é o maior')
elif media == seg:
    print('Todos são iguais')
else:
    print('Sexta é o maior')

print(f'O número Total de livros é: {total_livros}')
print(f'A média dos livros emprestados é de: {media}')