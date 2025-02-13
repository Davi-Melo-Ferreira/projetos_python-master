
import os 


os.system('cls')

dias = int(input('Quando o livro foi devolvido após a data de validade?: '))

if dias > 7:
    multa = (dias * 2)
elif dias >= 4:
    multa = (dias * 1)
else:
    multa = (dias * 0.50)

print(f'Você deve R${multa:.2f} reais de multa')