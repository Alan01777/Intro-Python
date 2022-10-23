''' Uma transportadora utiliza caminhões que suportam até 10 toneladas de peso, as
caixas transportadas tem tamanho fixo e o caminhão comporta no máximo 200
volumes, assim, esta transportadora precisa controlar a quantidade e o peso dos
volumes para acomodar nos caminhões. Faça um programa que leia n caixas e
seu peso, ao final, o programa deve imprimir a quantidade de volumes, o peso total
dos volumes e o peso médio dos volumes'''

import sys
def caixas():
    nCaixas = int(input("Quantas caixas deseja ler? "))
    somaPeso = 0
    for i in range(1, nCaixas + 1):
        if (nCaixas <= 200) and (somaPeso <= 10000):
            peso = float(input(f'#{i} peso:'))
            somaPeso += peso
        elif (nCaixas>200):
            print("Quantidade de caixas ultrapassou o limite!")
            sys.exit()
        elif (somaPeso>10000):
            print("Peso total ultrapassou o limite!")
            sys.exit()
    print(f'Quantidade de caixas lidas: {nCaixas}\n'
          f'Peso total lido: {somaPeso}KG')

    pass


caixas()