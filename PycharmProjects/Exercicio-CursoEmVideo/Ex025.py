'''Crie um programa que leia o nome de uma pessoa e diga se ela tem Silva no nome'''

nome = str(input('Digite o nome completo: ')).upper().strip()
print(f'Nome: {nome}')
if 'SILVA' in nome:
    print('O nome digitado possuí Silva.')
else:
    print('O nome digitado não possuí Silva.')