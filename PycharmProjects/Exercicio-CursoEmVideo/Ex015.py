"""Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado e a
quantidade de dias pelos quais ele foi alugado. calcule o preço a pagar, sabendo que o carro
custa R$60 por dia e R$0,15 por km rodado."""

print("="*20)
print("ALUGUEL DE CARRO")
print("="*20)

km = float(input('Digite a quantidade de KM percorridas com o vieculo: '))
dias = int(input('Digite a quantidade de dias que o veiculo foi alugado: '))

valor_pagar = (dias * 60) + (0.15 * km)

print(f"Para um veiculo alugado por {dias} dias, e tendo percorrido um total de {km}Km, o valor a ser pago é R$ {valor_pagar:.2f} ")