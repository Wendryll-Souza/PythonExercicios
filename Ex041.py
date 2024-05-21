'''A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria
de acordo com a idade.
- até 9 anos: mirim
- até 14 anos: infantil
- até 19 anos: junior
- até 20 anos: sênior
- acima: master'''

from datetime import date

print('='*32)
print('CONFEDERAÇÃO NACIONAL DE NATAÇÃO')
print('='*32)

ano_atual = date.today().year #pegando o ano atual por meio da biblioteca datetime
ano_nascimento = int(input('Ano de nascimento: ')) #pegando o ano de nascimento por meio da entrada de dados

idade = ano_atual - ano_nascimento

print(f"Com {idade} anos de idade sua ",end='')

if idade <= 9:
    print('Categoria é Mirim')
elif idade <=14:
    print('Categoria é Infantil')
elif idade <= 19:
    print('Categoria é Junior')
elif idade <= 20:
    print('Categoria é Sênior')
else:
    print('Categoria é Master')