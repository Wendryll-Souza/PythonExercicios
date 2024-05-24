'''Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada o, programa deverá perguntar se o usuario quer ou não continuar.
No final, mostre:
- quantas pessoas tem mais de 18 anos.
- quantos homens foram cadastrados.
- quantas mulheres com menos de vinte anos.'''

qtd_pessoas_maior_dezoito = 0
qtd_homens = 0
qtd_mulher_menos_vinte = 0
while True:
    idade = int(input('Digite sua idade: '))#recebendo a idade

    while (idade < 0) or (idade > 120):#validação de dados para idade
        idade = int(input('Erro! idade incerida incorreta, digite uma idade válida: '))

    sexo = str(input('Digite o sexo da pessoa [M/F]: ')).upper().strip()#recebendo o sexo

    while (sexo != 'M') and (sexo != 'F'):#validação de dados para sexo
        sexo = str(input('Digite uma opção válida [M/F]: ')).upper().strip()

    continuar = str(input('Deseja continuar cadastrando [S/N]? ')).upper().strip() #recebendo se o usuario quer ou não continuar

    while (continuar != 'S') and (continuar != 'N'):#validação de dados para continuar
        continuar = str(input('Erro! digite uma opção válida: ')).upper().strip()

    if idade > 18: #quantidade de pessoas maiores de 18
        qtd_pessoas_maior_dezoito += 1

    if sexo == 'M':#quantidade de homens cadastrados
        qtd_homens += 1
    elif sexo == 'F' and idade < 20:
        qtd_mulher_menos_vinte += 1

    if continuar == 'N':
        print('====FIM DO PROGRAMA====')
        print('Foram cadastradas:\n'
              f'Quantidade de homens: {qtd_homens}.\n'
              f'Quantidade de mulheres com menos de vinte anos: {qtd_mulher_menos_vinte}.\n'
              f'Quantidade de pessoas com mais de 18 anos: {qtd_pessoas_maior_dezoito}.')
        break