'''Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça
um programa que ajude ele, lendo o nome deles e escreva o nome do escolhido'''

from time import sleep
from random import choice

nomes = list()

for i in range(0,4):
    nome = str(input('Digite o nome do aluno: ')).upper().strip()
    nomes.append(nome)

print('Sorteando',end='')
sleep(1)
print('.',end='')
sleep(1)
print('.',end='')
sleep(1)
print('.')

print(f"O aluno sorteado foi {choice(nomes)}")