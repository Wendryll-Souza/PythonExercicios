"""Escreva um programa que faça o computador 'pensar' em um número inteiro entre
0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.

O programa deverá escrever na tela se o usuário venceu ou perdeu."""

from random import randint

print('='*20)
print('\033[1:34mJogo da adivinhação\033[m')
print('='*20)
print('Sorteando um número')

num_computador = randint(0,5)

num_jogador = int(input('tente adivinhar o número pensado pelo computador entre 0 e 5: '))

if num_jogador == num_computador and num_jogador <= 5 and num_jogador >= 0:
    print("\033[1:32mJogador Venceu\033[m")
elif num_jogador != num_computador and num_jogador <= 5 and num_jogador >= 0:
    print("\033[1:31mJogador Perdeu\033[m")
else:
    print("\033[1:33mO número advinhado precisa ser entre 0 e 5\033[m")