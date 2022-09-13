'''Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número 
elevado ao segundo número. Não utilize a função de potência da linguagem. '''

base = int(input('Insira um valor para a base:'))
expoente = int(input('Insira um valor para o expoente:'))

cont = 1
res = 1
while cont <= expoente:
    res = res * base
    cont += 1
    
print(f'Valor final: {res}')