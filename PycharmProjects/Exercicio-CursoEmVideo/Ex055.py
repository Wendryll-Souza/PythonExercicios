'''Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior peso e o menor peso lidos'''

menor = maior = 0

for i in range (1,6):
    peso = float(input(f'Digite o peso da {i}° pessoa: '))

    if i == 1:
        menor = maior = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso

print(f'O maior peso digitado foi {maior:.1f}kg e o menor {menor:.1f}kg')