'''Faça um programa que imprima todos os valores entre 0 e 100 múltiplos de 10.'''


def numNaturais():
    for i in range(0, 100):
        if (i % 10 == 0):
            print(f'{i}')
    pass


numNaturais()