'''Faça um programa que leia um número e diga se ele é ou não um número primo.'''

numero = int(input('Digite um número para saber se é primo: '))
divisor = 0

if numero > 0:
    for i in range(1,(numero + 1)):
        if numero % i == 0:
            divisor += 1
    if divisor == 2:
        print(f'Número {numero} é um número primo.')
    else:
        print(f'Número {numero} não é um número primo.')
else:
    print('Não existem número primos negativos ou nulos.')