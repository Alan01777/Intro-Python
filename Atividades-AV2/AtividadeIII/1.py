'''Faça um programa que leia 5 números e informe a soma e a média dos números.'''


def cont():
    sum = 0
    for i in range(1, 6):
        num = int(input("Insira um número: "))
        sum += num
    media = sum / i
    print(f'Soma: {sum}\n'
          f'Media: {media}')
    pass


cont()