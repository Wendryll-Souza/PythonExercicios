'''Crie um programa que leia vários números inteiros pelo teclado, mostre a média entre todos os valores lidos. O programa
deve ao usuário se ele quer ou não continuar a digitar valores.'''

#variaveis
media = soma = maior = menor = cont = 0

while True:
    numero = int(input('Digite um valor: '))
    soma += numero #somando todos os valores.
    cont += 1 # contador
    if cont == 1:
        maior = menor = numero #definindo o primeiro valor das variavis menor e maior
    else: # validando o maior valor
        if numero > maior:
            maior = numero
        elif numero < menor:
            menor = numero

    sair = str(input('Deseja sair [S/N]? ')).upper().strip()

    while (sair != 'S') and (sair != 'N'):
        sair = str(input('Opção inválida! digite uma opção valida [S/N]: ')).upper().strip()

    if (sair == 'S'):
        break

media = soma / cont
print(f'Foram digitados {cont} valores, sua soma é {soma}, sua média é {media:.2f}, o maior número digitado foi {menor} e o maior foi {maior}.')