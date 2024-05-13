'''Faça um programa que leia um número inteiro qualquer e mostre na tela a sua  tabuada.'''

numero = int(input("Digite um número para saber sua tabuada: "))
print('=======')
print('TABUADA')
print('=======')

for i in range(1,11):
    print(f'{numero} x {i} = {numero * i}')