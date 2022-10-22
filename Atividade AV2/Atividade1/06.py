'''Faça um programa que leia o destino do passageiro, se a viagem inclui retorno (ida
e volta) e informe o preço da passagem conforme a tabela a seguir:'''


def calcPassagem():
    codDestino = int(input("Insira o código de seu destino: "))
    retorno = str(input("Deseja incluir passagem de volta? (s/n)"))

    if (codDestino == 1):
        passagem = 500
        destino = "Região Norte"
        if (retorno == "s"):
            passagem = 900
    if (codDestino == 2):
        passagem = 350
        destino = "Região Nordeste"
        if (retorno == "s"):
            passagem = 650
    if (codDestino == 3):
        passagem = 350
        destino = "Região Centro-oeste"
        if (retorno == "s"):
            passagem = 600
    if (codDestino == 4):
        passagem = 300
        destino = "Região Sul"
        if (retorno == "s"):
            passagem = 550

    print(f'Destino: {destino}\n'
          f'valor: R${passagem:.2f}')

    pass
calcPassagem()