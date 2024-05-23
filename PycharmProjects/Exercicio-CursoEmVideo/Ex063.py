'''Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma sequencia de fibonacci
Ex 0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8'''

n = int(input('Digite a quantidade de termos da sequencia de FIBONACCI deseja exibir: '))

t1 = 0
t2 = 1
t3 = 1

print("FIBONACCI: ",end='')
for i in range(0,n):
    if i == (n - 1):
        print(f'{t1}')
    else:
        print(f'{t1} -> ', end='')

    t1 = t2
    t2 = t3
    t3 = t1 + t2