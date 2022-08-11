#Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
#   o produto do dobro do primeiro com metade do segundo.
#   a soma do triplo do primeiro com o terceiro.
#   o terceiro elevado ao cubo.

inteiro = int(input('Numero inteiro:'))
inteiro2 = int(input('Numero inteiro:'))
real = int(input('Numero real:'))

print('Produto:',((inteiro * 2) * (inteiro2 / 2)))
print('Soma:', ((inteiro * 3) + real))
print('Cubo:', real**3)
