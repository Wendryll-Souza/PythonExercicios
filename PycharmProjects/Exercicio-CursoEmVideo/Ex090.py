'''Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final,
mostre o conteúdo da estrutura na tela.'''

aluno = dict()

nome = str(input('Nome do aluno: ')).upper().strip()
while len(nome) < 3:
    nome = str(input('Digite um nome válido: ')).upper().strip()

media = float(input('Média aluno: '))
while (media < 0) or (media > 10):
    media = float(input('Digite uma média válida: '))

if media > 7:
    situacao = 'APROVADO'
elif media > 5 and media < 7:
    situacao = 'RECUPERAÇÃO'
else:
    situacao = 'REPROVADO'

aluno['nome'] = nome
aluno['media'] = media
aluno['situacao'] = situacao

print(f'Nome é igual a {aluno['nome']}')
print(f'Média é igual a {aluno['media']}')
print(f'Situação é igual a {aluno['situacao']}')