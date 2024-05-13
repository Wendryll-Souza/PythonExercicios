"""Desenvolva um programa que pergunte a distancia de uma viagem em Km. Calcule o preço
da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas."""

print('-'*28)
print('\033[1:34mCalculo de custo para viagem\033[m')
print('-'*28)

km = int(input('Digite a distancia em Km a ser percorrida: '))

if km >= 0 and km <= 200:
    custo_passagem = km * 0.5
    print(f'O valor da passagem para uma viagem de {km}km é R${custo_passagem:.2f}.')
elif km > 200:
    custo_passagem = km * 0.45
    print(f'O valor da passagem para uma viagem de {km}Km é R${custo_passagem:.2f}.')
else:
    print('Não é possivel calcular viagens com km negativo.')