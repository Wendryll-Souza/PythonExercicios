'''Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que foram pares, se o valor
digitado for impar desconsidere-o.'''

soma = 0

for i in range(1,7):
    num = int(input(f'Digite um o {i}º valor: '))
    if num % 2 == 0:
        soma += num
print(f'A soma de todos os valores pares digitados foi: {soma}.')