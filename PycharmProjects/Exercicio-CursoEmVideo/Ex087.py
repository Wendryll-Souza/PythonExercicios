'''Aprimore o exercicio anterior, mostrando no final:
- A soma de todos os valores pares digitados.
- A soma dos valores da terceira coluna
- O maior valor da segunda linha'''

matriz = [[],[],[]]
pares = 0
soma_terceira_coluna = 0
maior_segunda_linha = 0
for x in range(0,3):
    for y in range(0,3):
        valor = int(input(f'Digite um valor para a posição [{x},{y}] da matriz: '))

        if valor % 2 == 0:
            pares += valor

        matriz[x].insert(y,valor)
print('='*30)
for x in range(0,3):
    for y in range(0,3):
        print(f'[ {matriz[x][y]} ] ',end='')
    print()
print('='*30)
print(f'A soma de todos os valores pares da matriz é: {pares}.')
print(f'A soma dos valores da terceira coluna é ',end='')
for x in range(0,3):
    soma_terceira_coluna += matriz[x][2]
print(soma_terceira_coluna)
print('O maior valor da segunda linha é ',end='')
for x in range(0,3):
    if x == 0:
        maior_segunda_linha = matriz[1][x]
    elif maior_segunda_linha < matriz[1][x]:
        maior_segunda_linha = matriz[1][x]
print(maior_segunda_linha)