'''
Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
'''

numero = int(input("Digite um valor: "))

dobro = numero * 2
triplo = numero * 3
raiz = numero ** (1/2)

print(f'''O valor {numero} possui:
Dobro de {dobro}.
triplo de {triplo}.
raiz quadrada de {raiz:.2f}.''')
