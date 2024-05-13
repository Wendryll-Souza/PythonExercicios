'''O mesmo professor do desafio anterior quer sortear a ordem de apresentação do trabalho dos alunos.
Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.'''

from random import shuffle

nomes = list()
for i in range(0,4):
    nome = str(input('Digite o nome do aluno: ')).upper().strip()
    nomes.append(nome)  
shuffle(nomes)
print(f'Depois do embaralhamento a ordem de apresentação será: {nomes}')