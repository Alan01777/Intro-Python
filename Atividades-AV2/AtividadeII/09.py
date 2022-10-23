'''O banco Facimp concederá um crédito especial com juros de 2% aos seus clientes
de acordo com o saldo médio no último ano. Faça um programa que leia o saldo
médio de um cliente e calcule o valor do crédito de acordo com a tabela a seguir. O
programa deve imprimir uma mensagem informando o saldo médio e o valor de
crédito.'''


def valorCredito():
    saldoMedio = float(input("Informe seu saldo médio: "))

    if (saldoMedio >= 0) and (saldoMedio <= 500):
        credito = 0
    elif (saldoMedio > 500) and (saldoMedio <= 1000):
        credito = saldoMedio * 0.3
    elif (saldoMedio > 1000) and (saldoMedio <= 3000):
        credito = saldoMedio * 0.4
    elif (saldoMedio > 3000):
        credito = saldoMedio * 0.5
        
    print(f'Saldo médio: R${saldoMedio:.2f}\n'
          f'Valor de crédito: R${credito:.2f}')
    
    pass

valorCredito()