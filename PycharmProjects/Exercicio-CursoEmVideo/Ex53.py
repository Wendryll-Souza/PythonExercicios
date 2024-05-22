'''Crie um programa que leia uma frase qualquer e diga se ela é um palindromo, desconsiderando os espaços.'''

print('-'*25)
print('VERIFICADOR DE PALINDROMO')
print('-'*25)

frase = input('Digite uma frase para verificar se é um palindromo: ').upper().strip().split()
frase = ''.join(frase)
fraseReversa = frase[::-1]

if frase == fraseReversa:
    print(f'Frase no sentido normal: {frase}.')
    print(f'Frase no sentido contrário: {fraseReversa}.')
    print(f'A frase {frase} é um palindromo.')
else:
    print(f'Frase no sentido normal: {frase}.')
    print(f'Frase no sentido contrário: {fraseReversa}.')
    print(f'A frase {frase} não é um palindromo.')
