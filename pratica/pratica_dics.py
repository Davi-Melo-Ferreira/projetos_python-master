import os

os.system('cls')

palavra = input('Digite: ')

for char in palavra:
    pos = ord(char) - ord('a') + 1
    print(pos, end=' ')
    