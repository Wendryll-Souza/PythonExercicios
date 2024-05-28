'''Crie um programa que leia nome e duas notas de varios alunos e guarde tudo em uma lista composta. No final,
mostre um boletim contendo a média de cada um e permita que o usuario possa mostrar as notas de cada aluno individualmente'''

aluno = list()
classe = list()
media = 0
while True:
    nome = str(input('Nome do aluno: ')).upper().strip()

    while len(nome) < 2:
        nome = str(input('Erro! Digite um nome válido: ')).upper().strip()

    n1 = float(input('1º Nota: '))
    while (n1 > 10) or (n1 < 0):
        n1 = float(input("Erro! Digite uma nota valida: "))

    n2 = float(input('2º Nota: '))
    while (n1 > 10) or (n1 < 0):
        n2 = float(input('Erro! Digite uma nota valida: '))

    media = (n1 + n2) / 2

    aluno.append(nome)
    aluno.append(n1)
    aluno.append(n2)
    aluno.append(media)
    classe.append(aluno[:])
    aluno.clear()

    sair = input('Deseja encerrar[S/N]? ').upper().strip()
    while (sair != 'S') and (sair != 'N'):
        sair = input('Erro, inseira um valor valido!Deseja encerrar[S/N]? ').upper().strip()

    if sair == 'S':
        break

print('='*30)
print('No.    Nome                        Média')
for i in range(0,len(classe)):
    print(f'{i+1}      {classe[i][0]:<20} {classe[i][-1]:>10}')
while True:
    op = int(input('Deseja consultar a nota de qual aluno digite seu No [0 para sair]: '))

    while (op < 0) or (op > len(classe)):
        op = int(input('Erro! digite o No correto de um aluno[0 para sair]: '))

    if op == 0:
        print('Encerrando...')
        break
    else:
        for i in range(0,len(classe)):
            if (op-1) == i:
                print(f'Notas de {classe[i][0]} são [{classe[i][1]} , {classe[i][2]}]')