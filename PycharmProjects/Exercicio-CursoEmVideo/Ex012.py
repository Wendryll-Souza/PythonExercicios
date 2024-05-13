"""Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com
5% de desconto."""

print('='*20)
print('Calculo de desconto')
print('='*20)

valor_produto = float(input('Digite o valor do produto: R$'))

valor_novo = valor_produto - (valor_produto*0.05)

print(f"O produto de R${valor_produto:.2f} com desconto de 5% passará a ter R${valor_novo:.2f}.")