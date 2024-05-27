'''Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.

seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-la por extenso.'''

numeros = ('Zero','Um','Dois','Três','Quatro','Cinco','Seis','Sete','Oito','Nove','Dez',
           'Onze','Doze','Treze','Quatorze','Quinze','Dezesseis','Dezessete','Dezoito','Dezenove','Vinte')

num = int(input('Digite um valor entre 0 e 20: '))

while (num < 0) or (num > 20):
    num = int(input('Erro! Digite um valor entre 0 e 20:'))

print(f'Valor por extenso: {numeros[num]}.')