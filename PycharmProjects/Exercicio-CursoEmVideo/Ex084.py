'''faça um programa que leia nome e peso de varias pessoas, guardando tudo em uma lista. No final, mostre.
- Quantas pessoas foram cadastradas.
- uma listagem com as pessoas mais pesadas
- uma listagem com as pessoas mais leves'''

maior_peso = menor_peso = 0

info = list()
pessoa = list()
while True:
    nome = str(input('Nome: ')).upper().strip() # recebendo o nome do usuario

    while len(nome) < 3: # válidação de dados para nome
        nome = str(input('Erro!Digite um número válido: ')).upper().strip()

    peso = float(input('Peso[Ex 60]: ')) # recebendo o peso do usuario

    if maior_peso == 0 and menor_peso == 0: #verificando o maior e menor peso
        menor_peso = peso
        maior_peso = peso
    elif maior_peso < peso:
        maior_peso = peso
    elif menor_peso > peso:
        menor_peso = peso

    pessoa.append(nome) #adicionando nome a lista pessoa
    pessoa.append(peso) #adicionando peso a lista pessoa
    info.append(pessoa[:]) #adicionando uma cópia da lista pessoa a lista info
    pessoa.clear() #limpando a lista pessoa

    sair = str(input('Deseja sair[S/N]')).upper().strip() # perguntando se o usuario deseja sair.

    while (sair != 'S') and (sair != 'N'): #válidação de dados para a variavel sair.
        sair = str(input('Erro! Digite um valor válido[S/N]: ')).upper().strip()

    if sair == 'S': #lógica de saida do loop while
        print('Encerrando...')
        break

print('-'*20)
print(f'Ao total foram cadastradas: {len(info)} pessoas.')
print(f'O maior peso foi {maior_peso:.1f}Kg, peso de ',end='')
for x in range(0,len(info)): #percorrendo a lista info e exibindo o maior valor
    for y in range(0,2):
        if info[x][y] == maior_peso:
            print(f'[{info[x][0]}] ',end='')
print()
print(f'O menor peso foi {menor_peso:.1f}Kg, peso de ',end='')
for x in range(0,len(info)): #percorrendo a lista info e exibindo o menor valor
    for y in range(0,2):
        if info[x][y] == menor_peso:
            print(f'[{info[x][0]}] ',end='')
print()
