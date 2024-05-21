"""Desenvolva uma lógica que leia o passo e a altura de uma pessoa, calcule seu IMC e mostre seu status,
de acordo com a tabela abaixo:
- abaixo de 18.5: abaixo do peso.
- entre 18.5 e 25: peso ideal.
- 25 até 30: sobrepeso.
- 30 até 40: obesidade.
- acima de 40: obesidade mórbida."""

print('-'*14)
print('CALCULO DE IMC')
print('-'*14)

altura = float(input('Digite sua altura [Ex 1.90]: '))
peso = float(input('Digite seu peso [Ex 65.5]: '))

print('-'*14)

imc = peso / (altura ** 2)

print(f'Seu IMC é {imc:.2f} e seu STATUS é ',end='')

if imc < 18.5:
    print('abaixo do peso.')
elif imc >= 18.5 and imc < 25:
    print('peso ideal.')
elif imc >= 25 and imc < 30:
    print('sobrepeso ')
elif imc >= 30 and imc < 40:
    print('obesidade')
else:
    print('obesidade mórbida')