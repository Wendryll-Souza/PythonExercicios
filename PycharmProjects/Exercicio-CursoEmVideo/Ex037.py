"""Escreva um programa que leia um número inteiro   qualquer e peça para o usuário escolher qual será a base de
conversão:

1 - para binario
2 - para octal
3 - para hexadecimal"""

print('='*30)
print(' Conversor de bases númericas')
print('='*30)

print('''
    [ MENU ]
1 - Binario.
2 - Octal.
3 - Hexadecimal.
''')
print('='*30)

op = int(input('Digite a opção desejada [Ex: 1]: '))
num = int(input('Digite o valor a ser convertido: '))

if op == 1:
    print(f'O valor de base decimal {num} convertido para a base binaria é {bin(num)[2:]}.')
elif op == 2:
    print(f'O valor de base decimal {num} convertido para a base octal é {oct(num)[2:]}.')
elif op == 3:
    print(f'O valor de base decimal {num} convertido para a base hexadecimal é {hex(num)[2:]}')
else:
    print('Opção invalida!')