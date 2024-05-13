'''Escreva um programa que pergunte o salário de um funcionario e calcule o valor do seu aumento.
- Para salário superior a R$ 1.250,00 calcule um aumento de 10%.
- Para os inferiores ou iguais o aumento é de 15%.'''

print('='*27)
print('Calculo de aumento salárial')
print('='*27)

salario_atual = float(input('Digite o valor do salario atual: '))
salario_novo = 0

if salario_atual > 1250:
    salario_novo = salario_atual + (salario_atual * 0.1)
    print(f'O Funcionario que possui salario de R${salario_atual:.2f} depois de um aumento de 10% passou a ganhar R${salario_novo:.2f}.')
else:
    salario_novo = salario_atual + (salario_atual * 0.15)
    print(f'O Funcionario que possui salario de R${salario_atual:.2f} depois de um aumento de 15% passou a ganhar R${salario_novo:.2f}.')
