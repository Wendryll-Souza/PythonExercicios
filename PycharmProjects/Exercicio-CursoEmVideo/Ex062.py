'''Melhore o desafio 061, perguntando para o usuário se ele quer mostrar mais alguns termos. o programa encerra quando ele disser
que quer mostrar 0 termos.'''

while True:
    qtd_termos = int(input("Digite a quantidade de termos que deseja exibir: "))

    if qtd_termos == 0:
        print('Encerrando...')
        break
    else:
        primeiro_termo = int(input('Digite o primeiro termo da Pa: '))
        razao = int(input('Digite a razão da Pa: '))
        termo = primeiro_termo

        while qtd_termos >= 1:
            if qtd_termos > 1:
                print(f'{termo}, ',end='')
                termo += razao
            else:
                print(f'{termo}...')
                termo += razao
            qtd_termos -= 1