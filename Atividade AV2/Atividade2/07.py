'''Faça um programa que realize a soma de todos os valores inteiros de 1 a n, sendo
que n deve ser informado pelo usuário.'''


def soma():
    n = int(input("Insira um valor para n: "))
    sum = 0
    for i in range(1, n + 1):
        sum += i
    print(sum)
    pass


soma()