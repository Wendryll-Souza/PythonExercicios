"""Faça um programa que leia o ano de um jovem e informe, de acordo com sua idade.
- se ele ainda vai se alistar ao serviço militar.
- se é a hora de se alistar.
- se já passou do tempo do alistamento.

seu programa também devera mostrar o tempo que falta ou que passou do prazo."""

from datetime import date

print('-'*19)
print("ALISTAMENTO MILITAR")
print('-'*19)

ano_atual = date.today().year #setando a data atual por meio da biblioteca datetime
ano_nascimento = int(input('Digite o seu ano de nascimento: ')) #captando o ano de nascimento por uma entrada do teclado
idade = ano_atual - ano_nascimento #armazenando a idade do usúario

if idade < 18:
    tempFalta = 18 - idade # tempo que falta para votar.
    print(f'Com {idade} anos de idade, você ira se alistar no serviço militar em {tempFalta} anos.')
elif idade >= 18:
    if idade == 18:
        print(f'Com {idade} você pode se alistar no serviço militar.')
    else:
        tempPassou = idade - 18
        print(f'Com {idade} já se passou {tempPassou} anos do seu alistamento militar.')