'''Crie um programa que vai ler várias números e colocar em uma lista.
Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores impares digitados, respectivamente.
Ao final mostre o conteúdo das três listas geradas.'''

numeros = list()
pares = list()
impares = list()

while True:
    numero = int(input('Digite um número: '))

    numeros.append(numero)

    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

    sair = input('Deseja sair[S/N]? ').upper().strip()
    while (sair != 'S') and (sair != 'N'):
        sair = input('Erro! Digite um valor correto[S/N]: ').upper().strip()

    if sair == 'S':
        break

print(f'Valores digitados {numeros}.')
print(f'Valores impares digitados {impares}.')
print(f'Valores pares digitados {pares}.')