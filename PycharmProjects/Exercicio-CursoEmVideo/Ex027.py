'''Faça um programa que leia o nome de uma pessoa , mostre em seguida o primeiro e o
último nome separadamente.'''

nome_completo = str(input('Digite seu nome completo: ')).upper().strip().split()

print(f'Primeiro nome: {nome_completo[0]}.')
print(f'Último nome: {nome_completo[-1]}')