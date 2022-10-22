'''Escreva um programa que leia um peso na Terra e o número de um planeta e
imprima o valor correspondente do peso neste planeta. A relação de planetas é
dada a seguir juntamente com o valor das gravidades relativas à Terra. Para
calcular o peso no planeta use a fórmula:
Em que:
PP = Peso no planeta
PT = Peso na Terra
G = Gravidade relativa'''


def pesoPlaneta():
    codPlaneta = int(input("Insira o cód. do planeta: "))
    pesoTerra = float(input("Insira o peso na terra: "))

    if (codPlaneta == 1):
        planeta = "Mecúrio"
        gravidadeRelativa = 0.37
    elif (codPlaneta == 2):
        planeta = "Vênus"
        gravidadeRelativa = 0.88
    elif (codPlaneta == 3):
        planeta = "Marte"
        gravidadeRelativa = 0.38
    elif (codPlaneta == 4):
        planeta = "Júpiter"
        gravidadeRelativa = 2.64
    elif (codPlaneta == 5):
        planeta = "Saturno"
        gravidadeRelativa = 1.15
    elif (codPlaneta == 6):
        planeta = "Urano"
        gravidadeRelativa = 1.17

    pp = (pesoTerra / 10) * gravidadeRelativa

    print(f'Peso no platena {planeta}: {pp}')
    pass


pesoPlaneta()