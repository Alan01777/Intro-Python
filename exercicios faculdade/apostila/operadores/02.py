'''Faça um Python Script que receba um valor t referente a uma quantidade total em
segundos. Calcule a quantas horas:minutos:segundos a quantidade total de segudos
corresponde.'''


segundos=int(input('Insira um valor em segundos:'))

horas = segundos // 3600
resto = segundos % 3600
minutos = resto // 60
segundos = resto % 60

print(f'{horas}:{minutos}:{segundos}')