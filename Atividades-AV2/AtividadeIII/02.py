'''Faça um programa que leia 10 valores e ao final imprima a média aritmética dos
valores lidos.'''


def cont():
    sum = 0
    for i in range(1, 11):
        num = int(input("Insira um valor: "))
        sum += num
    media = sum / i
    print(f'Media: {media}')
    pass


cont()