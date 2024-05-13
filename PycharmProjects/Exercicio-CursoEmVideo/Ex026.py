"""Faça um programa que leia uma frase pelo teclado e mostre:
- Quantas vezes aparece a letra A.
- Em que posição ela aparece a primeira vez.
- em que posição ela aparece a última vez."""

frase = str(input('Digite uma frase: ')).strip().split()
fraseSemEspaco = ''.join(frase)

print(f'A frase possui {fraseSemEspaco.count('a')} letra(s) A.')
print(f"A letra A aparece pela primeira vez na posição {fraseSemEspaco.find('a') + 1}")
print(f"A letra A aparece pela última vez na posição {fraseSemEspaco.rfind('a') + 1}")