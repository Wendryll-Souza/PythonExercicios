'''Faça um programa que leia  um número de 0 a 999 e mostre na tela cada um dos digitos separados.
Ex: 1834

unidades: 4
dezenas: 3
centenas: 8
milhar: 1
'''

u = 0
d = 0
c = 0
m = 0

num = str(input('Digite um valor entre 0 e 9999: ')).strip()

u = num[3]
d = num[2]
c = num[1]
m = num[0]

print(f'''Unidades: {u}
Dezenas: {d}
centenas: {c}
Milhares: {m}''')