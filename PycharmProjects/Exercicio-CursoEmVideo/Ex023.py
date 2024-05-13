'''Faça um programa que leia  um número de 0 a 999 e mostre na tela cada um dos digitos separados.
Ex: 1834

unidades: 4
dezenas: 3
centenas: 8
milhar: 1
'''

num = int(input('Digite um valor entre 0 e 9999: '))

u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print(f'''Unidades: {u}
Dezenas: {d}
centenas: {c}
Milhares: {m}''')