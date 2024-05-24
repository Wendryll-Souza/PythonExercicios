'''Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada usuario. O programa será interrompido
quando o número solicitado for negativo.'''

while True:

    numero = int(input('Digite um número para exibir sua tabuada ou um valor negativo para sair: '))

    if numero > 0:
        for i in range(1,11):
            print(f'{numero:^2} x {i:^2} = {(numero*i):^2}')
    else:
        print('Encerrando...')