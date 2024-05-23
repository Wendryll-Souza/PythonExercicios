'''Refaça o desafio 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da
progrssão usando a estrutura while.'''

cont = 10
primeiro_termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
termo = primeiro_termo

print('PA: ',end='')
while cont >= 1:
    if cont > 1:
        print(f'{termo}, ',end='')
        termo += razao
    else:
        print(f'{termo}...')
        termo += razao
    cont -= 1