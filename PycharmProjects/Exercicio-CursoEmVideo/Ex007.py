"""Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média."""

print('='*17)
print('Calculo de média')
print('='*17)

nota1 = float(input('Digite a primeira nota do aluno: '))
nota2 = float(input('Digite a segunda nota do aluno: '))

media = (nota1 + nota2) / 2

print(f"O aluno com notas de {nota1} e {nota2} possui média de {media}.")