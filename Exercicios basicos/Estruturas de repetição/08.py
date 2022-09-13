'''Faça um programa que leia 5 números e informe a soma e a média dos números. '''


a=1
soma=0

while a <=5:
    num=float(input('Insira um número:'))
    soma+=num
    a+=1
media=soma/5
print(f'Soma: \t\t{soma}\n'
      f'Média: \t\t{media}')