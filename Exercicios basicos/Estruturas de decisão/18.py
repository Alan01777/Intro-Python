#Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.

dia = int(input('Dia:'))
mes = int(input('Mês:'))
ano = int(input('Ano:'))

valida = False

if (mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 \
        or mes == 12):
    if dia > 0 and dia <= 31:
        valida = True
        print('1')

elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
    if dia > 0 and dia <= 30:
        valida = True
        print('2')

elif mes == 2:
    if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
        if dia > 0 and dia <= 29:
            valida = True
            print('3')
    else:
        if dia > 0 and dia <= 28:
            valida = True
            print('4')

if valida == True:
    print(f'{dia}/{mes}/{ano} É uma data válida')
else:
    print(f'{dia}/{mes}/{ano} Não é uma data válida')
