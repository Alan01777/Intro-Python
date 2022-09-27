'''Crie um Python Script que receba um número inteiro n, correspondente a um valor
em reais. Calcule a quantidade mínima de notas que um banco deve fornecer para
atingir o valor. Notas disponíveis: 100,00 reais; 50,00 reais; 10,00 reais; 1,00 real.'''


saque = int(input('Valor do saque:'))

if (saque >= 1) and (saque <= 600):
    nota100Real = saque // 100
    saque -= nota100Real * 100
    nota50Real = saque // 50
    saque -= nota50Real * 50
    nota10Real = saque // 10
    saque -= nota10Real * 10
    nota1Real = saque

    if nota100Real > 0:
        print(f'R$100 == {nota100Real}')
    if nota50Real > 0:
        print(f'R$50 == {nota50Real}')
    if nota10Real > 0:
        print(f'R$10 == {nota10Real}')
    if nota1Real > 0:
        print(f'R$1 == {nota1Real}')
else:
    print('Valor do saque inválido!')