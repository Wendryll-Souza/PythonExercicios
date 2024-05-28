'''faça um programa que leia nome e peso de varias pessoas, guardando tudo em uma lista. No final, mostre.
- Quantas pessoas foram cadastradas.
- uma listagem com as pessoas mais pesadas
- uma listagem com as pessoas mais leves'''

maior_peso = menor_peso = 0

info = list()
pessoa = list()
while True:
    nome = str(input('Nome: ')).upper().strip()

    while len(nome) < 3:
        nome = str(input('Erro!Digite um número válido: ')).upper().strip()

    peso = float(input('Peso[Ex 60]: '))

    if maior_peso == 0 and menor_peso == 0:
        menor_peso = peso
        maior_peso = peso
    elif maior_peso < peso:
        maior_peso = peso
    elif menor_peso > peso:
        menor_peso = peso

    pessoa.append(nome)
    pessoa.append(peso)
    info.append(pessoa[:])
    pessoa.clear()

    sair = str(input('Deseja sair[S/N]')).upper().strip()

    while (sair != 'S') and (sair != 'N'):
        sair = str(input('Erro! Digite um valor válido[S/N]: ')).upper().strip()

    if sair == 'S':
        print('Encerrando...')
        break

print('-'*20)
print(f'Ao total foram cadastradas: {len(info)} pessoas.')
print(f'O maior peso foi {maior_peso:.1f}Kg, peso de ',end='')
