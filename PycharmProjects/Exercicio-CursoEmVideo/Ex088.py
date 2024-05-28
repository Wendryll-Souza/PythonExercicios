'''Faça um programa que ajude um jogador da Mega Sena a criar palpites. O programa vai perguntar quantos jogos serão gerados
e vai sortear 6 números entre 1 e 60, para cada jogo, cadastrando tudo em uma lista composta.'''

from random import randint

qtd_jogos = int(input('Digite quantos jogos você quer fazer? '))
jogo = []

for i in range(0,qtd_jogos):
    for j in range(0,6):
        jogo.append(randint(1,60))
    print(f'Jogo {i+1}: {jogo}')
    jogo.clear()