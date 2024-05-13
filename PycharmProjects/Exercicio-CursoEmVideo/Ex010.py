"""
Crie um programa que leia quanto  dinheiro uma pessoa tem  na carteira  e mostre  quantos dólares
ela pode comprar.

considerando US$ 1,00 = R$ 3,27
"""

print('='*20)
print('Conversor de moedas')
print('='*20)

reais = float(input('Digite o valor em reais a ser convertido: R$'))

dolar = reais / 3.27

print(f"O valor R${reais:.2f} Convertido corresponde a US${dolar:.2f}.")