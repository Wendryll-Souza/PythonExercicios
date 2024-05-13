'''Desenvolva um programa que leia o comprimento de três retas e diga ao usuario se elas podem ou não formar um
triângulo.'''

print('='*25)
print('Verificador de Triangulo:')
print('='*25)

print('''Para se formar um triangulo,
a soma de dois lados deve ser menor que o terceira.''')
print('-'*25)

r1 = int(input('Digite o valor do primeiro seguimento de reta: '))
r2 = int(input('Digite o valor do segundo seguimento de reta: '))
r3 = int(input('Digite o valor do terceiro seguimento de reta: '))

if r3 < (r1 + r2) and r2 < (r1 + r3) and r1 < (r2 + r3):
    print('Com os valores digitados é possivel formar um triangulo.')
else:
    print('Com os valores digitados não é possivel formar um triangulo.')