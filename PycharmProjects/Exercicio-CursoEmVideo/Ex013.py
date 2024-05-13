"""Faça um algoritmo que leia o salário de um funcionario e mostre seu novo salário, com 15% de desconto. """

salario = float(input('Digite o salario do funcionario: R$'))

salario_novo = salario + (salario*0.15)

print(f"Um funcionario que possui salário de R${salario} após 15% de aumento passou a ser R${salario_novo}")