'''Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de
pagamento:
- à vista dinheiro/cheque 10% de desconto.
- à vista cartão: 5% de desconto.
- em até 2x no cartão: preço normal.
- em 3x ou mais no cartão 20% de juros.'''

print('-*-'*6)
print('CAIXA DE PAGAMENTO')
print('-*-'*6)

print("""[Opcões de Pagamento]
1 - à vista dinheiro/cheque 10% de desconto.
2 - à vista cartão: 5% de desconto.
3 - em até 2x no cartão: preço normal.
4 - em 3x ou mais no cartão 20% de juros.
""")
desconto = 0
valor_pagar = 0
valor_produto = float(input('Digite o valor do produto: R$'))
op_pagamento = int(input('Digite a opção de pagamento desejada [Ex 1]: '))

if op_pagamento == 1:
    desconto = valor_produto * 0.1
    valor_pagar = valor_produto - desconto
    print(f'O produto que custava R${valor_produto:.2f} com a opção de pagamento em dinheiro/cheque com 10% de desconto passa a custar R${valor_pagar:.2f}')
elif op_pagamento == 2:
    desconto = valor_produto * 0.05
    valor_pagar = valor_produto - desconto
    print(f'O produto que custava R${valor_produto:.2f} com a opção de pagamento à vista no cartão com 5% de desconto passa a custar R${valor_pagar:.2f}.')
elif op_pagamento == 3:
    valor_pagar = valor_produto / 2
    print(f'O produto que custa R${valor_produto:.2f} com a opção de pagamento em 2x no cartão, tem suas parcelas com valor de R${valor_pagar:.2f}.')
else:
    qtd_parcelas = int(input('Digite em quantas parcelar você gostaria de parcelar de 3 a 12: '))
    acrescimo = valor_produto * 0.2
    valor_pagar = valor_produto + acrescimo
    print(f'O produto que custava R${valor_produto:.2f} com a opção de pagamento em {qtd_parcelas}x no cartão com 20% de juros, passa a custar R${valor_pagar} e tem suas parcelas com valor de R${(valor_pagar/qtd_parcelas):.2f}')