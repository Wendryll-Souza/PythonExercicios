'''
Faça um programa que leia a largura e a altura de uma parede em metros, calcule  a sua área e a quantidade
de tinta necessária para pinta-lá, sabendo que cada litro de tinta, pinta uma área de 2m².
'''

largura = float(input("Digite a largura da parede em metros: "))
altura = float(input("Digite a altura da parede em metros: "))

area = largura * altura

tinta = area / 2

print(f'Uma parede de largura {largura}m e altura {altura}m possui uma área de {area}m², sendo assim precisaremos de {tinta} litros de tinta para pintala.')