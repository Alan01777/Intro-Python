'''Faça um programa que receba dois números inteiros e gere os números inteiros que 
estão no intervalo compreendido por eles. '''


min=int(input('Valor mínimo:'))
max=int(input('valor máximo:'))

while (min<(max-1)):
    min+=1
    print(min)