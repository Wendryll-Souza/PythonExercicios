'''Faça um programa que leia três números e mostre qual é o maior e qual é o menor.'''

print('='*24)
print('Calculo de maior e menor')
print('='*24)

n1 = float(input('Digite o primeiro valor a ser comparado: '))
n2 = float(input('Digite o segundo valor a ser comparado: '))
n3 = float(input('Digite o terceiro valor a ser comparado: '))

if n1 > n2 > n3:
    print(f'Entre {n1}, {n2} e {n3} o maior valor é {n1} e o menor {n3}.')
elif n3 > n2 > n1:
    print(f'Entre {n1}, {n2} e {n3} o maior valor é {n3} e o menor {n1}.')
elif n2 > n1 > n3:
    print(f'Entre {n1}, {n2} e {n3} o maior valor é {n2} e o menor {n3}.')
else:
    print(f'Entre {n1}, {n2} e {n3} o maior valor é {n3} e o menor {n2}.')