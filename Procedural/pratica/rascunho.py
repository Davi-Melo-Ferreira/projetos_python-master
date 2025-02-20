import os
import string
import time

os.system('cls')

letras = string.ascii_letters
numeros = string.digits
caracteres = string.punctuation
espacos = string.whitespace

terminal = 'Terminando'
for i in range(1, 4):
    terminal += '.'
    print(terminal)
    time.sleep(0.5)
    os.system('cls')