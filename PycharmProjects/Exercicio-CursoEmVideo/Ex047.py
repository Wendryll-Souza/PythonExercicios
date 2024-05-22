'''Crie um programa que mostre na tela todos os números pares que estão no intervalo de 1 e 50.'''

print('Número entre 1 e 50:')

for i in range(1,51):
    print(f'{i:^2}',' ',end='')
    if i % 10 == 0:
        print()