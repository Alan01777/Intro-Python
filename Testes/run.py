# autonomia == 12km/l


def calc_viagem():
    tempoViagem = float(input("Tempo de viagem (minutos): "))
    tempoViagem = tempoViagem/60
    velocidadeMedia = float(input("Velocidade média (KM/H): "))
    
    distanciaPercorrida = tempoViagem*velocidadeMedia
    litrosConsumidos = distanciaPercorrida/12
    
    print(f'Distância percorrida: {distanciaPercorrida}KM')
    print(f'Litros consumidos: {litrosConsumidos}L')
pass
calc_viagem()