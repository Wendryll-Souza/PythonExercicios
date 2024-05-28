'''Crie uma lista onde o usuário possa digitar sete valores númericos e cadastre-os em uma lista única que mantenha
separada os valores pares e ímpares. No final, mostre os valores praes e ímpares em ordem crescente.'''

numeros = list()
impares = list()
pares = list()

for i in range(0,7):
    valor = int(input(f'Digite o {i+1}° valor númerico: '))

    if valor % 2 == 0:
        pares.append(valor)
    else:
        impares.append(valor)
numeros.append(impares[:])
numeros.append(pares[:])
print('='*30)
print(f'Lista completa: {numeros}')
print('='*30)
print(f'Lista de valores ímpares em ordem crescente: {sorted(numeros[0])}')
print('='*30)
print(f'Lista de valores pares em ordem crescente: {sorted(numeros[1])}')