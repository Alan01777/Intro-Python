'''Faça um programa que imprima todos os valores pares entre 1 e 20'''


def contPar():
    for i in range(1, 21):
        if (i % 2 == 0):
            print(i)
    pass


contPar()