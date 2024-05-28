'''Crie um programa onde o usuario digite uma expressão qualquer que use parenteses. Seu aplicativo deverá analisar
se a expressão passada está com os parênteses abertos e fechados na ordem correta.'''

espressao = input('Digite uma expressão: ')

parenteses_aberto = espressao.count('(')
parenteses_fechado = espressao.count(')')

if parenteses_aberto != parenteses_fechado:
    print(f'Expressão incorreta!')
    print(f'Temos {parenteses_aberto} parenteses abertos.')
    print(f'Temos {parenteses_fechado} parenteses fechados.')
else:
    print(f'Expressão correta!')
    print(f'Temos {parenteses_aberto} parenteses abertos.')
    print(f'Temos {parenteses_fechado} parenteses fechados.')