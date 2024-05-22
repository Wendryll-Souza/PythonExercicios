'''Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:

- A média de idade do grupo.
- Qual é o nome do homem mais velho.
- Quantas mulheres têm menos de 20 anos.'''

#variaveis
media_idade = idade_homem = qtd_mulheres_vinte = 0
nome_homem_velho = ''


for i in range(1,5):
    print('='*20)
    #validação para nome
    nome = input(f'Digite o nome da {i}° pessoa: ').upper().strip()
    while len(nome) < 3:
        nome = input(f'Digite um nome válido: ')

    #validação de dados para idade
    idade = int(input(f'Digite a idade da {i}° pessoa: '))
    while (idade <= 0) or (idade >= 120):
        idade = int(input('Digite uma idade valida: '))

    #validação de dados para sexo
    sexo = str(input(f'Digite o sexo da {i}° pessoa [M/F]: ')).upper().strip()
    while (sexo != 'F') and (sexo != 'M'):
        sexo = str(input(f'Opção invalida! Digite o sexo [M/F]:')).upper().strip()

    #media de idades do grupo
    media_idade += idade

    #nome do homem mais velho
    if sexo == 'M' and idade_homem == 0:
        idade_homem = idade
        nome_homem_velho = nome
    elif sexo == 'M' and idade_homem < idade:
        idade_homem = idade
        nome_homem_velho = nome

    #quantidade de mulheres com menos de vinte anos
    if sexo == 'F' and idade < 20:
        qtd_mulheres_vinte += 1

media_idade = media_idade / 4 #média das idades do grupo
print('='*20)
#exibindo na tela a média das idades
print(f'A média de idades do grupo é {int(media_idade)} anos.')

#exibindo na tela o nome do homem mais velho
if nome_homem_velho == '':
    print(f'Não foi cadastrado nenhum homem.')
else:
    print(f'O nome do homem mais velho cadastrado é {nome_homem_velho} com {idade_homem} anos.')

#exibindo na tela a quantidade de mulheres com menos de vinte anos.
print(f'A quantidade de mulheres com menos de vinte anos é {qtd_mulheres_vinte}.')