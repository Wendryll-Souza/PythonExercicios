'''Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
- quantos números foram digitados.
- a lista de valores, ordenados de forma decrescente.
- se o valor 5 foi digitado e está ou não na lista.'''

numeros = list()
troca = 0

while True:
    numero = int(input('Digite um número: '))
    numeros.append(numero)

    sair = input('Deseja sair[S/N]: ').upper().strip()
    while (sair != 'N') and (sair != 'S'):
        sair = input('Erro! Digite um valor valido para sair[S/N]: ').upper().strip()
    if sair == 'S':
        print('Encerrando...')
        break
print('='*20)
print(f'Valores digitados: {numeros}')
print(f'Foram digitados: {len(numeros)} numeros.')
print(f'Lista em forma decrescente: ',end='')
#exibindo os números em forma decrescente sem usar funções.
for p in range(0,len(numeros)):
    for q in range(0,len(numeros)):
        if numeros[p] > numeros[q]:
            troca = numeros[q]
            numeros[q] = numeros[p]
            numeros[p] = troca
print(f'{numeros}.')

if 5 in numeros:
    print('O número cinco foi digitado e está na lista.')
else:
    print('O número cinco não foi digitado, assim não está na lista.')
