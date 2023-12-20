"""Faça um programa que leia algo e mostre todas as informações posiveis."""

valor = input("Digite algo: ")

print(f"Foi digitado o valor: {valor}")
print(f"O tipo do valor é {type(valor)}")
print(f"O valor digitado é um espaço: {valor.isspace()}")
print(f"O valor digitado é um número: {valor.isnumeric()}")
print(f"O valor digitado é um caracter: {valor.isalpha()}")
print(f"O valor digitado é alfanumerico: {valor.isalnum()}")
print(f"O valor digitado é maiusculo: {valor.isupper()}")
print(f"O valor digitado é minusculo: {valor.islower()}")