'''Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. 
Ex.: 5!=5.4.3.2.1=120 '''

num = int(input('Insira um valor:'))
anterior = num - 1
i = 1
for i in range(num):
    while anterior != 0:
        num = num * anterior
        anterior = anterior - 1
print(num)
