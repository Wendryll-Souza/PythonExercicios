'''Faça um programa que leia um ano qualquer e mostre se o ano é bissexto.'''

ano = int(input('Digite o ano atual: '))
if ano & 4 == 0 and ano % 100 != 0 and ano % 400 == 0:
    print(f'O ano {ano} é Bissexto.')
else:
    print(f'O ano {ano} não é Bissexto')