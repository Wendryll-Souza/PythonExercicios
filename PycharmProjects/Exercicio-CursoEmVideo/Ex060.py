'''Faça um programa que leia um número qualquer e mostre seu fatorial.
Ex 5! = 5x4x3x2x1 = 120'''

print('='*19)
print('CALCULO DE FATORIAL')
print('='*19)

num = int(input('Digite um número para verificar seu fatorial: '))
resultado = num
for i in range(num,0,-1):
    if i > 1:
        print(f'{i} x ',end='')
    else:
        print(f'{i} = ',end='')
    i -= 1
    if i != 0:
        resultado = resultado * i
print(f'{resultado}')
