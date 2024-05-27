'''Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar,
para cada palavra, quais são suas vogais.'''

palavras = ('APRENDER','PROGRAMAR','LINGUAGEM','PYTHON','CURSO','GRATIS','ESTUDAR','PRATICAR')

for i in range(0,len(palavras)):
    print(f"Na palavra {palavras[i]} temos ", end='')

    for p in palavras[i]:
        if p == "A":
            print('A ',end='')
        elif p == 'E':
            print('E ',end='')
        elif p == 'I':
            print('I ',end='')
        elif p == 'O':
            print('O ',end='')
        elif p == 'U':
            print('U ',end='')
    print()