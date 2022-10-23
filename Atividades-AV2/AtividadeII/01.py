'''Faça um programa que receba um número inteiro e verifique se este número é
maior que 20, em caso afirmativo o programa deverá imprimir a mensagem: "Maior
que 20"'''

def compara():
    num = int(input("Insira um número: "))

    if (num > 20):
        print("Maior que 20")
    else:
        print("Menor que 20")
    pass
compara()