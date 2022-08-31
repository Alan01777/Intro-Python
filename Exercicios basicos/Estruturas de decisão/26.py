litros = float(input('Litros abastecidos:'))
tipoCombustivel = input('Tipo de combustível(G-gasolina, A-álcool):')
if tipoCombustivel == 'G':
    preçoLitro = 2.50
    valor = litros * preçoLitro
    if litros <= 20:
        desconto = 0.05  #Desconto de 5%
        valor = (litros * preçoLitro) * desconto
elif tipoCombustivel == 'A':
    preçoLitro = 1.90
    valor = litros * preçoLitro
    if litros > 20:
        desconto = 0.04  #Desconto de 5%
        valor = (litros * preçoLitro) * desconto

print(f'Valor a ser pago: R${valor}')