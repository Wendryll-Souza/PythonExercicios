'''Crie um programa que simule o funcionamento de um caixa eletronico. No inicio, pergunte ao usuario qual será
o valor a ser sacado, (núermo inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
- considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1'''

cinquenta = 0
vinte = 0
dez = 0
um = 0

while True:
    valor_sacar = int(input('Digite um valor para sacar, cédular disponiveis 50, 20, 10 e 1: R$'))

    while valor_sacar > 0:
        if valor_sacar >= 50:
            cinquenta = valor_sacar // 50
            valor_sacar = valor_sacar % 50
        elif valor_sacar >= 20:
            vinte = valor_sacar // 20
            valor_sacar = valor_sacar % 20
        elif valor_sacar >= 10:
            dez = valor_sacar // 10
            valor_sacar = valor_sacar % 10
        else:
            um = valor_sacar // 1
            valor_sacar = valor_sacar % 1

    print('Contando...')
    print('Cédulas para retirada: ')
    print(f'Cédulas de R$50: {cinquenta}.')
    print(f'Cédulas de R$20: {vinte}.')
    print(f'Cédulas de R$10: {dez}.')
    print(f'Cédulas de R$1: {um}.')

    sair = str(input('Encerrar operação[S/N]? ')).upper().strip()

    while (sair != 'S') and (sair != 'N'):
        sair = input('Opção invalida, digite uma opção correta[S/N]: ').upper().strip()

    if sair == 'S':
        print('Operação encerrada, volte sempre.')
        break
