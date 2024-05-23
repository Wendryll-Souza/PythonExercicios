'''Crie um programa que leia dois valores e mostre um menu na tela:
[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa

seu programa deverá realizar a operação solicitada em cada caso.'''

from time import sleep

n1 = n2 = 0

while True:
    print('='*6)
    print(' MENU')
    print('='*6)
    print(' [1] SOMAR \n [2] MULTIPLICAR \n [3] MAIOR \n [4] NOVOS NÚMEROS \n [5] SAIR DO PROGRAMA')
    print('-'*25)

    opcao = int(input('Digite sua opção desejada [Ex 1]: '))
    while (opcao < 1) or (opcao > 5):
        opcao = int(input('Digite uma opção válida [Ex 1]: '))

    if opcao == 1:
        soma = n1 + n2
        print(f'A soma dos valores {n1} e {n2} é {soma}.')
        sleep(1)
    elif opcao == 2:
        multiplicacao = n1 * n2
        print(f'A multiplicação dos valores {n1} e {n2} é {multiplicacao}.')
        sleep(1)
    elif opcao == 3:
        if n1 > n2:
            print(f"O maior valor entre {n1} e {n2} é {n1}.")
            sleep(1)
        else:
            print(f'O maior valor entre {n1} e {n2} é {n2}.')
            sleep(1)
    elif opcao == 4:
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o segundo valor: '))
        sleep(1)
    else:
        print('Encerrando . . .')
        sleep(1)
        break
