'''Crie um programa onde o usuario possa digitar cinco valores numéricos e cadastre-os em uma posição correta de inserção.
(sem usar sort()). No final mostre a lista ordenada na tela.'''

numeros = list()
troca = 0
for i in range(0,5):
    numero = int(input(f'Digite o {i + 1}º valor: '))
    numeros.append(numero)

print(f'Lista conforme digitado: {numeros}.')

for p in range(0,len(numeros)):
    for q in range(0,len(numeros)):
        if numeros[p] < numeros[q]:
            troca = numeros[q]
            numeros[q] = numeros[p]
            numeros[p] = troca

print(f'Lista ordenada em forma crescente: {numeros}')
