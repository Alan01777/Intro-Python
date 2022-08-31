'''Faça um Programa que peça um número e informe se o número é inteiro ou decimal. 
Dica: utilize uma função de arredondamento.'''

import math

num=float(input('Insira um valor:'))

if num == round(num):
    print(f'{num} é inteiro')
else:
    print(f'{num} é decimal')