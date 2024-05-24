'''Crie que leia vários números, inteiros pelo teclado. O programador só vai parar quando o usuario digitar o valor 999,
que é a condição de parada. No final mostre quantos números foram digitados e qual foi a soma entre eles desconsiderando o flag.'''

soma = cont = 0

while True:

    numero = int(input('Digite um número: '))

    if numero == 999:
        print('Encerrando...')
        break
    else:
        soma += numero
        cont += 1
print(f'Foram digitados {cont} números e sua soma foi {soma}.')