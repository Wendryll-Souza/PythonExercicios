'''Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final mostre os 10 primeiros termos da
progressão.'''

print('-'*21)
print('PROGRESSÃO ARITMÉTICA ')
print('-'*21)

primeiro_termo = int(input('Digite o primeiro termo da P.A: '))
razao = int(input('Digite a razão da P.A: '))
termo = primeiro_termo

print('PA: ')
for i in range(0,10):
    print(f'{termo} ',end='')
    termo += razao
