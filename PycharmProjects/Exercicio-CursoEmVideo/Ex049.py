'''Refaça o desafio 009, mostre a tabuada de um número que o usuario escolher, só que desssa vez em um laço de repetição for'''

numero = int(input('Digite o número que você desejá verificar a tabuada: '))

for i in range(0,11):
    print(f'{numero:^2} X {i:^2} = {(numero * i):^2}')
