'''Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
- Quantas vezes apareceu o valor 9.
- Em que posição foi digitado o primeiro valor 3.
- Quais foram os números pares.'''
print('='*20)
n1 = int(input('Digite o 1º valor: '))
n2 = int(input('Digite o 2º valor: '))
n3 = int(input('Digite o 3º valor: '))
n4 = int(input('Digite o 4º valor: '))

numeros = (n1,n2,n3,n4)

print(f'Foram digitados os valores: {numeros}.')
if 3 in numeros:
    print(f'O número 3 foi digitado primeiro na posição: {numeros.index(3)+1}.')
else:
    print(f'O número 3 não foi digitado nenhuma vez.')

print(f'Números pares digitados: ',end='')
for i in range(0,len(numeros)):
    if numeros[i] % 2 == 0:
        print(f'{numeros[i]} ',end='')