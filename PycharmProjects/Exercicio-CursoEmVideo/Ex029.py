'''Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80 KM/H, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$7,00 por cada km acima do limite.'''

print('-'*26)
print('\033[1:34mCalculo de multa veicular\033[m')
print('-'*26)

velocidade = int(input('Digite o valor da velocidade em KM: '))

if velocidade > 80:
    multa = (velocidade - 80) * 7
    print(f'\033[1:31mVeiculo acima do limite permitido de 80 Km/h, condutor multado em R${multa:.2f}\033[m')
else:
    print('\033[1:32mVeiculo dentro do limite permitido, condutor não sera multado.\033[m')