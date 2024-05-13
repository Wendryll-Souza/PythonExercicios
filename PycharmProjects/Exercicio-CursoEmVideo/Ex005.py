"""
Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e antecessor.
"""

numero = int(input('Digite um número para ver seu sucessor e antecessor: '))

antecessor = numero - 1
sucessor = numero + 1

print(f'O número {numero} possui o antecessor {antecessor} e o sucessor {sucessor}.')