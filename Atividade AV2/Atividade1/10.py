'''Faça um programa que leia dois valores inteiros e efetue a adição. Caso o valor
somado seja maior que 20, este deverá ser apresentado somando-se a ele mais 8, caso o
valor somado seja menor ou igual a 20, este deverá ser apresentado subtraindo-se 5.'''


def calc():
    num1 = int(input("Insira um valor: "))
    num2 = int(input("Insira um valor: "))
    soma = num1+num2
    
    if (soma>20):
        soma+=8
    else:
        soma-=5
    print(f"Soma: {soma}")

    pass

calc()