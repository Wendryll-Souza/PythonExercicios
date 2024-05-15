'''Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem.
- O primeiro valor é maior.
- O segundo valor é maior.
- Não existiu valor maior, os dois são iguais.'''

print('-'*19)
print('Comparador númerico')
print('-'*19)

n1 = float(input('Digite o primeiro valor a ser comparado: '))
n2 = float(input('Digite o segundo valor a ser comparado: '))
print('-'*19)
if n1 > n2:
    print('o primeiro valor é maior.')
elif n2 > n1:
    print('O segundo valor é maior.')
else:
    print('Ambos os valores são iguais.')