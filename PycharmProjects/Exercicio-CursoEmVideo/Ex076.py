'''Crie um  programa que tenha uma tupla única com nomes de produção e seus respectivos preços, na sequencia.
No final, mostre uma lista de preços, organizando os dados em forma de tabela.'''

produtos = ('Lápis',1.75,'Borracha',2,'Caderno',15.9,'Estojo',25,'Transferidor',4.2,'Compasso',9.99,'Mochila',120.32,
            'Canetas',22.30,'Livro',34.90)
msg = 'LISTA DE PREÇOS'
print('-'*40)
print(f'{msg:^30}')
print('-'*40)
for i in range(0,len(produtos)):
    if i % 2 == 0:
        print(f'{produtos[i]:.<20} ',end='')
    else:
        print(f'R$ {produtos[i]:.2f}')
print('-'*40)