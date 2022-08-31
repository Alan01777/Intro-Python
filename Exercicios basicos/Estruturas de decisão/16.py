'''Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. 
O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas 
seguintes situações:

    a)Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa 
    não deve fazer pedir os demais valores, sendo encerrado;
    b)Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário 
    e encerre o programa;
    c)Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
    d)Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário; '''
import math

valorA = float(input('Valor de a:'))
valorB = float(input('Valor de b:'))
valorC = float(input('Valor de c:'))

delta = (valorB**2) - 4 * valorA * valorC

if delta == 0:
    print('A equação não é do segundo grau!')
    exit()
if delta < 0:
    print('A equação não possui raizes reais!')
    exit()
if delta == 0:
    x1 = (-valorB + math.sqrt(delta)) / 2 * valorA
    print(f'A operação possui apenas uma raiz real. x1= {x1:.1}')
if delta > 0:
    x1 = ((-valorB + math.sqrt(delta)) / (2 * valorA))
    x2 = ((-valorB - math.sqrt(delta)) / (2 * valorA))
    
    print(delta)
    print(f'\nx1={x1:.3f}'
          f'\nx2={x2:.3f}')
