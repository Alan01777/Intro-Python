'''Faça um programa que leia um número inteiro entre 1 e 12 e escreva o mês
correspondente. Caso o usuário digite um número fora desse intervalo, deverá
aparecer uma mensagem informando que não existe mês com este número.'''


def informaMes():

    mes = int(input("Infore o número do mês: "))

    if (mes == 1):
        nomeMes = "Janeiro"
    elif (mes == 2):
        nomeMes = "Fevereiro"
    elif (mes == 3):
        nomeMes = "Março"
    elif (mes == 4):
        nomeMes = "Abril"
    elif (mes == 5):
        nomeMes = "Maio"
    elif (mes == 6):
        nomeMes = "Junho"
    elif (mes == 7):
        nomeMes = "Julho"
    elif (mes == 8):
        nomeMes = "Agosto"
    elif (mes == 9):
        nomeMes = "Setembro"
    elif (mes == 10):
        nomeMes = "Outubro"
    elif (mes == 11):
        nomeMes = "Novembro"
    elif (mes == 12):
        nomeMes = "Dezembro"
    else:
        print("Valor inválido! Não existe um mês com esse número!")
        informaMes()

    print(f'{nomeMes}')
    pass


informaMes()