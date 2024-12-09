import os


os.system('cls')

# varredura eficiente 
alph = 'abcdefghijklmnopqrstuvwxyz áàâãéêèíìîóòôõúùûç'

letras = input('Digite algo:').lower()
letras_corrigidas = ''

for char in letras:
        if char in alph:
            letras_corrigidas += char
print(letras_corrigidas.strip())