''''Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar
no final, mostre:

- Qual é o total de gastos na compra
- Quantos produtos custam mais de R$1000.
- Qual é o nome do produto mais barato.'''

tot_compra = qtd_mais_mil = prod_barato = contador = 0
nome_prod_barato = ''

while True:
    nome_produto = str(input("Digite o nome do produto: ")).upper().strip()

    preco = float(input(f'Digite o preço do produto {nome_produto}: R$'))

    continuar = str(input('Deseja continuar[S/N]? ')).upper().strip()

    while (continuar != 'S') and (continuar != 'N'):
        continuar = input('Digite um valor válido[S/N]: ').upper().strip()

    tot_compra += preco #total da compra

    if preco > 1000: #produtos que custam mais de mil
        qtd_mais_mil += 1

    if contador == 0:
        nome_prod_barato = nome_produto
        prod_barato = preco
    elif preco < prod_barato:
        nome_prod_barato = nome_produto
        prod_barato = preco

    contador += 1

    if continuar == 'N':
        print('===FIM DO PROGRAMA===')
        print(f'Total da compra: R$ {tot_compra}')
        print(f"Produtos que custam mais de mil reais: {qtd_mais_mil}")
        print(f'Nome do produto mais barato: {nome_prod_barato}')
        break