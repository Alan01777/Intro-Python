#Faça um Programa que leia três números e mostre-os em ordem decrescente.

a = int(input('Insira um valor:'))
b = int(input('Insira um valor:'))
c = int(input('Insira um valor:'))
valor = 0
if a < c:
    a, c = c, a

if a < b:
    a, b = b, a

if b < c:
    b, c = c, b

print(f'Ordem decrescente {a} {b} {c}')
print(f'{valor}')