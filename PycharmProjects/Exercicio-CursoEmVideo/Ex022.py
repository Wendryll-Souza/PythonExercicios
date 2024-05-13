'''
crie um programa que leia o nome completo de uma pessoa e mostre.
- O nome com todas as letras Maiusculas.
- O nome com todas as letras minusculas.
- Quantas letras, sem considerar espaços.
- Quantas letras tem o primeiro nome.
'''

print('='*20)
print('ANALISE DE NOME')
print('='*20)

nome_completo = str(input('Digite seu nome completo: ')).upper().strip()
nome_separado = nome_completo.split()
tot_letras = ''.join(nome_separado)
print('-'*20)
print(f"Nome em maiúsculo: {nome_completo}")
print(f'Nome em minúsculo: {nome_completo.lower()}')
print(f'Quantidade de letras sem considerar os espaços: {len(tot_letras)}')
print(f'Quantidade de letras do primeiro nome: {len(nome_separado[0])}')