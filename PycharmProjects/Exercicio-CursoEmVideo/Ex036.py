"""Escreva um programa para aprovar o emprestimo bancario para a compra de uma casa. O programa vai
perguntar o valor da casa, o salario do comprador e em quantos anos ele vai pagar.

- calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salario ou entao o emprestimo será negado."""

print('='*32)
print('\033[1:34mAPROVAÇÃO DE EMPRÉSTIMO BANCÁRIO\033[m')
print('='*32)
print('''calculo de aprovação de compra de imovel,
para aprovação a parcela não pode exceder 30% do seu salário.''')
print("="*32)

valor_casa = float(input('Digite o valor do Imovel: R$'))
salario = float(input('Digite o valor do seu salário: R$'))
qtd_anos = int(input('Digite em quantos anos deseja pagar: '))

porcentagem_salario = salario * 0.3 #calculando 30% do salário

parcela = valor_casa / (qtd_anos * 12) # calculando o valor da parcela

if parcela > porcentagem_salario:
    print(f'''\033[1:31m
    valor da parcela: R${parcela:.2f}
    Salário: R${salario:.2f}
    30% do salário: R${porcentagem_salario:.2f}
    Com uma parcela acima do valor de 30 % do seu salário,temos seu pedido de empréstimo negado.     
    \033[m''')
else:
    print(f'''\033[1:32m
        valor da parcela: R${parcela:.2f}
        Salário: R${salario:.2f}
        30% do salário: R${porcentagem_salario:.2f}
        Com uma parcela abaixo ou igual ao valor de 30 % do seu salário,temos seu pedido de empréstimo aprovado.     
        \033[m''')