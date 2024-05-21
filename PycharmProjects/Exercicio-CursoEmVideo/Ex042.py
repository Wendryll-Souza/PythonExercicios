'''Refaça o desafio 035 dos triângulos, acrescentando otipo de triângulo que será formado:
- Equilatero: Todos os lados iguais
- Isósceles: Dois lados iguais
- Escaleno: Todos os lados diferentes.'''

print('-='*11)
print('FORMAÇÃO DE TRIÂNGULOS')
print('-='*11)

r1 = float(input('Digite a medida do primeiro lado: '))
r2 = float(input('Digite a medida do segundo lado: '))
r3 = float(input('Digite a medida do terceiro lado: '))

if r3 < (r1 + r2) and r2 < (r1 + r3) and r1 < (r2 + r3):
    print(f'Com as medidas {r1}, {r2} e {r3} é possivel formar um triângulo.')
    if r1 == r2 == r3:
        print('Tipo de triângulo: Equilatero.')
    elif r1 == r2 != r3 or r1 == r3 != r2 or r2 == r3 != r1:
        print('Tipo do triângulo: Isósceles.')
    else:
        print('Tipo de triângulo: Escaleno.')
else:
    print(f'Com as medidas {r1}, {r2} e {r3} não é possível criar um triângulo.')