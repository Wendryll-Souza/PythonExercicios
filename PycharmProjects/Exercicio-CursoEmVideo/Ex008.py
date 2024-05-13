"""Escreva um programa que leia um valor em metros e exiba convertido em centimetros e mílimetros."""

valor = float(input('Digite um valor em metros: '))

cm = valor * 100
mm = valor * 1000

print(f'''O valor {valor}m corresponde a {cm}cm e {mm}mm''')