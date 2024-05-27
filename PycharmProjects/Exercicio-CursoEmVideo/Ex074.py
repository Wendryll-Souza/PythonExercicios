'''Crie um programa que vai gerar cinco números aleatorios e colocar em uma tupla.
Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla'''

from random import randint

numeros = (randint(0,100),randint(0,100),randint(0,100),randint(0,100),randint(0,100))
menor = maior = 0
print(f'Foram gerados os valores: {numeros}')

for i in range(0,5):
    if i == 0:
        menor = maior = numeros[i]
    elif numeros[i] < menor:
        menor = numeros[i]
    elif numeros[i] > maior:
        maior = numeros[i]

print(f'O maior valor é {maior}.')
print(f'O menor valor é {menor}.')