'''Faça um programa que leia "n" valores. O programa deve inicialmente solicitar ao
usuário que informe a quantidade desejada de valores a ser informada, depois ler
os "n" valores e ao final imprimir a média aritmética dos valores lidos'''


def cont():
    sum = 0
    quant = int(input("Quantidade desejada: "))

    for i in range(1, quant + 1):
        num = int(input("Informe um valor: "))
        sum += num
    media = sum / quant

    print(f'Media: {media}')

    pass


cont()