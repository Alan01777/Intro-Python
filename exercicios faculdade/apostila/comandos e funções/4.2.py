'''Repita o processo da questão anterior, porém utilizando a função deg2rad da biblio-
teca numpy para converter o ângulo de graus para radianos.'''


from math import sin, cos, tan, radians
from numpy import deg2rad

graus = float(input('Insira um valor em graus:'))

print(30 * '=')
print(f'Radianos: {deg2rad(graus)}')
print(f'Seno: {sin(graus)}')
print(f'Consseno: {cos(graus)}')
print(f'Tangente: {tan(graus)}')
print(30 * '=')