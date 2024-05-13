"""Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno,
cosseno e tangente desse ângulo."""

import math

angulo = int(input("Digite um angulo: "))

print(f'Para um ângulo de {angulo} temos:')
print(f'Seno: {math.sin(math.radians(angulo)):.2f}.')
print(f'Cosseno: {math.cos(math.radians(angulo)):.2f}.')
print(f'Tangente: {math.tan(math.radians(angulo)):.2f}.')