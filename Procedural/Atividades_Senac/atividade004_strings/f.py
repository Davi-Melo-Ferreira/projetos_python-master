#Faça um programa que receba o nome completo de uma pessoa e, posteriormente, imprima esse nome separadamente.
import os


os.system('cls')

nome = input('Diga seu nome completo: ')

separado = nome.split()

#print(separado)
print(f' {separado[0]}\n {separado[1]}\n \
{separado[2]}\n {separado[3]}\n')