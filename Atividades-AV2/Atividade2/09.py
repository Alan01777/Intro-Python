'''Faça um programa que permita entrar com números e imprimir o quadrado de cada
número digitado até entrar um número múltiplo de 6 que deverá ter seu quadrado
impresso também'''

import sys


def quadrado():
    for i in range(0, 11):
        num = float(input("Insira um valor: "))
        if (num % 6 != 0):
            quadrad = num**2
            print(f"Quadrado: {quadrad}")
        elif (num % 6 == 0):
            quadrad = num**2
            print(f"Quadrado: {quadrad}")
            sys.exit()

    pass


quadrado()