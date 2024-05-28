'''Crie um programa onde o usuario possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já
exista na lista, ele não será adicionado . No final, serão exibidos todos os valores únicos digitados, em ordem crescente.'''

numeros = list()

while True:
    numero = int(input('Digite um valor para adicionar a lista: '))

    if numero in numeros:
        while numero in numeros:
            print("O valor digitado já está na lista, por favor digite outro.")
            numero = int(input('Digite um valor para adicionar a lista: '))
        numeros.append(numero)
    else:
        numeros.append(numero)
        print('Valor adicionado a lista com sucesso.')

    sair = str(input('Deseja sair[S/N]: ')).upper().strip()

    while (sair != 'S') and (sair != 'N'):
        print('Erro! Digite um valor valido.')
        sair = str(input('Deseja sair[S/N]: ')).upper().strip()

    if sair == 'S':
        break
print(f'A lista foi formada com os valores {numeros}')
print(f'A lista agora exibida em ordem crescente {sorted(numeros)}')
