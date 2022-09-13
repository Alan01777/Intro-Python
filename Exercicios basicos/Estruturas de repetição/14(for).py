'''Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares. '''

par=0
impar=0

for i in range(10):
    num=int(input('Insira um valor:'))
    if num % 2 == 0:
        par+=1
    else:
        impar+=1
print(f'Valores pares:\t\t{par}\n'
      f'Valores impares:\t{impar}')
