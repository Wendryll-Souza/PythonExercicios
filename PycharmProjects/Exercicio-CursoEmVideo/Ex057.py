'''Faça um programa que leia o sexo de uma pessoa, mas somente aceite os valores "M" ou "F". Caso esteja errado,
peça a digitação novamente até ter um valor correto.'''

print('='*19)
print('Cadastrador de Sexo')
print('='*19)

sexo = input('Digite o seu sexo [F/M]: ').upper().strip()

while (sexo != 'M') and (sexo != 'F'):
    sexo = input('Invalido! digite uma opção valida [F/M]: ').upper().strip()

