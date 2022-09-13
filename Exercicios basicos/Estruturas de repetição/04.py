'''Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de 
crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%.
Faça um programa que calcule e escreva o número de anos necessários para que a população do país
A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento. '''

anos = 0

paisA = 80000
taxaA = 0.03
paisB = 200000
taxaB = 0.015

while paisA < paisB:
    paisA = paisA + (taxaA * paisA)
    paisB = paisB + (taxaB * paisB)
    anos += 1

else:
    print(f'\nLevou {anos} anos!'
          f'\nPais A: {int(paisA)} habitantes'
          f'\nPais B: {int(paisB)} habitantes')