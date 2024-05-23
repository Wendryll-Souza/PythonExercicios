'''crie um programa que leia vários numeros inteiros pelo teclado, o programa só deve parar quando o usuário
digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre
eles (desconciderando o flag).'''

qtd_numeros = soma = 0

while True:
    num = int(input('Digite um número ou 999 para encerrar: '))

    if num == 999:
        print("Encerrando ...")
        break
    else:
        soma += num
        qtd_numeros += 1

print(f'Foram digitados {qtd_numeros} números e a soma de todos os valores é digitados {soma}.')