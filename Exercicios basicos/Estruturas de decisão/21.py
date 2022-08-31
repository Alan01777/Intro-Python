'''Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque
e depois informar quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de: 
1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais. 
O programa não deve se preocupar com a quantidade de notas existentes na máquina.

    Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, 
    uma nota de 5 e uma nota de 1;
    Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, 
    quatro notas de 10, uma nota de 5 e quatro notas de 1. 
'''

saque = int(input('Valor do saque:'))

if saque >= 10 and saque <= 600:
    nota100Real = saque // 100
    saque -= nota100Real * 100
    nota50Real = saque // 50
    saque -= nota50Real * 50
    nota10Real = saque // 10
    saque -= nota10Real * 10
    nota5Real = saque // 5
    saque -= nota5Real * 5
    nota1Real = saque

    if nota100Real > 0:
        print(f'R$100 == {nota100Real}')
    if nota50Real > 0:
        print(f'R$50 == {nota50Real}')
    if nota10Real > 0:
        print(f'R$10 == {nota10Real}')
    if nota5Real > 0:
        print(f'R$5 == {nota5Real}')
    if nota1Real > 0:
        print(f'R$1 == {nota1Real}')
else:
    print('Valor do saque inválido!')