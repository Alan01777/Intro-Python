'''
Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar,
sabendo que a decisão é sempre pelo mais barato.'''

produtoA=float(input('Insira o valor do produto A:'))
produtoB=float(input('Insira o valor do produto B:'))
produtoC=float(input('Insira o valor do produto C:'))

if produtoA<produtoB and produtoA<produtoC:
    print(f'O produto mais barato é o A')
elif produtoB<produtoA and produtoB<produtoC:
   print(f'O produto mais barato é o B')
else:
    print(f'O produto mais barato é o C')