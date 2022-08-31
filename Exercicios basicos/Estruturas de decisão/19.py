'''Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, 
dezenas e unidades do mesmo.

    Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
    326 = 3 centenas, 2 dezenas e 6 unidades
    12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 
    10, 21, 11, 1, 7 e 16'''

num = int(input('Inira um valor entre 0 e 1000:'))

if num <= 1000:
    unidades = num // 1 % 10
    dezenas = num // 10 % 10
    centenas = num // 100 % 10

    print(f'{centenas} centenas, {dezenas} dezenas e {unidades} unidades')
else:
    print('Valor inválido!')