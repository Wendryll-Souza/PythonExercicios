'''Faça um programa que jogue par ou impar com computador. Jogo só sera interrompidoquando quando o jogador perder , mostre quantas vitorias consecutivas
que ele consquistou no final do jogo. '''

from random import randint

vitorias = 0
resultado = ''

print('='*12)
print('PAR OU ÍMPAR')
print('='*12)

while True:
    computador = randint(0, 10) # gerando um número entre 0 e 10

    usuario = int(input('Digite um valor entre 0 e 10: ')) # recebendo um valor númerico pelo teclado

    while (usuario < 0) or (usuario > 10): # validação de dados
        usuario = int(input('Digite um valor válido: '))

    palpite = str(input('Par ou Ímpar [P/I]: ')).upper().strip() #palpite do usuario se o resultado vai ser par ou impar

    while (palpite != 'P') and (palpite != 'I'):#validação de dados
        palpite = str(input('Digite um valor válido, Par ou Ímpar [P/I]')).upper().strip()

    soma = usuario + computador #somando os valores númericos digitados junto ao do computador.

    if (soma % 2 == 0):
        resultado = 'P'
    else:
        resultado = 'I'

    if palpite == resultado:
        vitorias += 1
    else:
        print(f'Você errou! Foram {vitorias} vitorias consecutivas.')
        break