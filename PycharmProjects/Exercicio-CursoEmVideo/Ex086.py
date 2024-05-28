'''Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
No final mostre a matriz na tela, com a formatação correta.'''

matriz = [[],[],[]]

for x in range(0,3):
    for y in range(0,3):
        valor = int(input(f'Digite um valor para a posição [{x},{y}] da matriz:'))
        matriz[x].insert(y,valor)
print('='*30)

for x in range(0,len(matriz)):
    for y in range(0,3):
        print(f'[ {matriz[x][y]} ] ',end='')
    print()