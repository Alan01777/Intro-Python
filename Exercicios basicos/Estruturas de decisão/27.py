#Morango
pesoMorango = float(input('Peso total dos morangos(KG):'))
if pesoMorango > 5:
    preçoMorango = 2.20
elif pesoMorango <= 5:
    preçoMorango = 2.50

valorMorango = pesoMorango * preçoMorango
if valorMorango > 25 or pesoMorango > 8:
    descontoMorango = 0.1
    valorMorango = (pesoMorango * preçoMorango) - (descontoMorango *
                                                   valorMorango)

#Maça
pesoMaça = float(input('Peso total das maçãs(KG):'))
if pesoMaça > 5:
    preçoMaça = 1.50
elif pesoMaça <= 5:
    preçoMaça = 1.80

valorMaça = pesoMaça * preçoMaça
if valorMaça > 25 or pesoMaça > 8:
    descontoMorango = 0.1
    valorMaça = (pesoMaça * preçoMaça) - (descontoMorango * valorMaça)

#saida
print(f'\nValor dos morangos: \tR${valorMorango:.2f}'
      f'\nValor das maçãs: \tR${valorMaça:.2f}')