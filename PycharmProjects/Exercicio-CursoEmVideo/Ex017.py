import math

"""Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retângulo,
calcule e mostre o comprimento da hipotenusa. """

cateto_adjacente = float(input('Digite o valor do cateto adjacente: '))
cateto_oposto = float(input('Digite o valor do cateto oposto: '))

hipotenusa = math.hypot(cateto_adjacente,cateto_oposto)

print(f'Para um cateto oposto de {cateto_oposto} e um cateto adjacente de {cateto_adjacente}, temos uma hipotenusa de {hipotenusa:.2f}.')
