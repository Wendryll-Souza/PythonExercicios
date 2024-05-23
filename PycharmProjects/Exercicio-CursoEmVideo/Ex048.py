'''Faça um programa que calcule a soma entre todas os números que são múltiplos de três e que se encontram no
intervalo de 1 até 500'''

soma = 0

for i in range(1,501,2):
    if i % 3 == 0:
        soma += i
print(f'A soma entre todos os valores entre 1 e 500 é {soma}.')