'''Melhore o jogo do desafio 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar
adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.'''

from random import randint

computador = randint(0,10) # definindo o número pensado pelo computador
tentativas = 0 #variavel que vai contar a quantidade de tentativas até acertar

print('='*19)
print('JOGO DA ADIVINHAÇÃO')
print('='*19)
print('Será que você consegue acertar o número sorteado pelo computador? vamos lá.')
print('De o seu palpite entre 0 e 10. ')
print('-'*20)

while True:
    jogada_usuario = int(input('Digite seu palpite: '))
    while (jogada_usuario < 0) or (jogada_usuario > 10):
        jogada_usuario = int(input('Digite um palpite válido: '))

    tentativas += 1

    if jogada_usuario != computador:
        if jogada_usuario < computador:
            print('Poxa você errou, tente um número um pouco mais alto.')
        else:
            print('Poxa você errou, tente um número um pouco mais baixo.')
    else:
        print(f'Parabéns, você acertou! o número pensado foi {computador} e você precisou de {tentativas} tentativas para acertar.')
