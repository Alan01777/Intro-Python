#Faça um Programa que leia três números e mostre o maior e o menor deles.
maior = 0
menor = 0
a = int(input('Insira um valor:'))
if a > maior:
    maior = a
menor = a

b = int(input('Insira um valor:'))
if b > maior:
    maior = b
if b < menor:
    menor = b
    
c = int(input('Insira um valor:'))
if c > maior:
    maior = c
if c < menor:
    menor = c

print(f'Maior: {maior}')
print(f'Menor: {menor}')