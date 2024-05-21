'''Crie um programa que faça o computador jogar jokenpô com você.'''

from random import choice
from time import sleep


computador = ['PEDRA','PAPEL','TESOURA']
jogada_computador = choice(computador)

print('='*19)
print('VAMOS JOGAR JOKENPÔ')
print('='*19)

print('Vamos jogar pedra papel ou tesoura escolha entre:')
print('''1 - PEDRA
2 - PAPEL
3 - TESOURA''')

jogada_usuario = int(input('Digite a opção desejada [Ex 1]: '))
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PÔ')
sleep(0.5)

if jogada_usuario == 1:
    jogada_usuario = 'PEDRA'
elif jogada_usuario == 2:
    jogada_usuario = 'PAPEL'
else:
    jogada_usuario = 'TESOURA'

if jogada_usuario == jogada_computador:
    print(f'O computador jogou {jogada_computador} e você jogou {jogada_usuario}, sendo assim deu empate.')
elif jogada_usuario == 'PEDRA' and jogada_computador == 'TESOURA':
    print(f'O computador jogou {jogada_computador} e você jogou {jogada_usuario}, sendo assim você venceu.')
elif jogada_usuario == 'PAPEL' and jogada_computador == 'PEDRA':
    print(f'O computador jogou {jogada_computador} e você jogou {jogada_usuario}, sendo assim você venceu.')
elif jogada_usuario == 'TESOURA' and jogada_computador == 'PAPEL':
    print(f'O computador jogou {jogada_computador} e você jogou {jogada_usuario}, sendo assim você venceu.')
else:
    print(f'O computador jogou {jogada_computador} e você jogou {jogada_usuario}, sendo assim o computador ganhou.')