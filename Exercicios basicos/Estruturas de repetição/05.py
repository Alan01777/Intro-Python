'''Altere o programa anterior permitindo ao usuário informar as populações e as taxas de 
crescimento iniciais. Valide a entrada e permita repetir a operação. '''

anos = 0
continuar = True

while continuar == True:
    paisA = int(input('Informe a população do Pais A:'))
    taxaA = float(input('Informe a taxa de crescimento do Pais A(%):'))
    paisB = int(input('Informe a população do Pais B:'))
    taxaB = float(input('Informe a taxa de crescimento do Pais B(%):'))
    while paisA < paisB:
        paisA = paisA + ((taxaA / 100) * paisA)
        paisB = paisB + ((taxaB / 100) * paisB)
        anos += 1

    else:
        print(f'\nLevou {anos} anos!'
              f'\nPais A: {int(paisA)} habitantes'
              f'\nPais B: {int(paisB)} habitantes')
    escolha = input('Deseja Continuar?(s/n)')
    if escolha == 'n':
        continuar = False
    else:
        continuar = True
