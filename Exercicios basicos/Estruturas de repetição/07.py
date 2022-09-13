'''Faça um programa que leia 5 números e informe o maior número. '''


a=1
maior=0
while a <=5:
    num1=float(input('Insira um número:'))
    if num1 >maior:
        maior=num1
    a+=1
        
print(f'O maior é: {maior:.1f}')
