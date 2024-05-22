'''Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram
a maioridade e quantas já são maiores.'''

from datetime import date

ano_atual = date.today().year
maior_idade = menor_idade = 0


for i in range(1,8):
    ano_nascimento = int(input(f'Digite o ano de nascimento da {i}° pessoa: '))
    idade = ano_atual - ano_nascimento

    if idade >= 18:
        maior_idade += 1
    else:
        menor_idade += 1

print('='*40)
print(f'Total de pessoas que completou a maior idade: {maior_idade}.')
print(f'Total de pessoas que ainda não completaram a maior idade: {menor_idade}')