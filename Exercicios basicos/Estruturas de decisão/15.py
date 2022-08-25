'''Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores 
podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, 
isósceles ou escaleno.

    Dicas:
    Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
    Triângulo Equilátero: três lados iguais;
    Triângulo Isósceles: quaisquer dois lados iguais;
    Triângulo Escaleno: três lados diferentes;'''
    
a=float(input('Lado A:'))
b=float(input('Lado B:'))
c=float(input('Lado C:'))

if (a + b < c) or (a + c < b) or (b + c < a):
        print('Nao é um triangulo')
elif a==b==c:
    print('É um triângulo equilátero')
elif a==b or a==c:
    print('É um triângulo isóceles')
else:
    print('É um triângulo escaleno')