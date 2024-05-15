"""Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo
com a média atingida.

- Média abaixo de 5.0: reprovado
- Média entre 5.0 e 6.9: recuperação
- Média 7.0 ou superior: aprovado"""

print('='*16)
print('CALCULO DE MÉDIA')
print('='*16)

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

media = (n1 + n2) / 2

if media < 5:
    print("Situação do Aluno: \033[1:31mREPROVADO\033[m")
elif media >= 5 and media < 7:
    print("Situação do Aluno: \033[1:33mRECUPERAÇÃO\033[m")
else:
    print("Situação do Aluno: \033[1:32mAPROVADO\033[m")