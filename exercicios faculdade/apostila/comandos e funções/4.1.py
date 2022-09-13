'''Peça do usuário um valor em graus para um ângulo. Converta-o para radianos e,
usando funções da biblioteca math, imprima o seno, cosseno e tangente deste ângulo.'''

from math import sin, cos, tan, radians

graus = float(input('Insira um valor em graus:'))

print(30 * '=')
print(f'Radianos: {radians(graus)}')
print(f'Seno: {sin(graus)}')
print(f'Consseno: {cos(graus)}')
print(f'Tangente: {tan(graus)}')
print(30 * '=')
