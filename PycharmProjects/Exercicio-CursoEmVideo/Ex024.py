"""Crie um programa que leia o nome de uma cidade e diga  se ela começa ou não com o nome santo"""

nome_cidade = str(input('Digite o nome da cidade: ')).upper().strip().split()

if nome_cidade[0] == 'SANTO' or 'SANTOS':
    print('O nome da cidade começa com Santo.')
else:
    print('O nome da Cidade não começa com Santo.')