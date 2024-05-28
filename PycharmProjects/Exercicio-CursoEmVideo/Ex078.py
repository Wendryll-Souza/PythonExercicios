'''Faça um programa que leia 5 valores númericos e guardeos em uma lista.
No final, mostre qual foi o maior e o menor valor digitado e as suas respctivas posições na lista.'''

numeros = list()
maior = menor = 0

for i in range(0,5):
    numero = int(input(f'Digite o {i+1}º valor: '))
    numeros.append(numero)

    if i == 0:
        maior = menor = numero
    elif maior < numero:
        maior = numero
    elif menor > numero:
        menor = numero
#exibindo as posições que aparece o maior valor na lista
print(f'Lista de números digitados: {numeros}')
print(f'O maior valor digitado foi {maior} e esta nas posições ',end='')
for i in range(0,len(numeros)):
    if numeros[i] == maior:
        print(f'{i + 1}... ',end='')
print()
#exibindo as posições que aparece o menor valor na lista
print(f'O menor valor digitado foi {menor} e esta nas posições ',end='')
for i in range(0,len(numeros)):
    if numeros[i] == menor:
        print(f'{i + 1}... ',end='')
print()