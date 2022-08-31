'''O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:

                          Até 5 Kg           Acima de 5 Kg
    File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
    Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
    Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg

    Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, 
    porém não há limites para a quantidade de carne por cliente. Se compra for feita no cartão Tabajara o
    cliente receberá ainda um desconto de 5% sobre o total da compra. Escreva um programa que peça o tipo
    e a quantidade de carne comprada pelo usuário e gere um cupom fiscal, contendo as informações da 
    compra: tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar. 
'''
desconto = 0
tipoCarne = input('Tipo de carne (Filé duplo; Alcatra; Picanha):')
peso = float(input('Peso da compra:'))

if tipoCarne == 'Filé duplo' or 'filé duplo' or 'file duplo' or 'File duplo':
    preço = 4.90
    if peso > 5:
        preço = 5.80
elif tipoCarne == 'Alcatra' or 'alcatra':
    preço = 5.90
    if peso > 5:
        preço = 6.80
elif tipoCarne == 'Picanha' or 'picanha':
    preço = 6.90
    if peso > 5:
        preço = 7.80

valorBruto = peso * preço

tipoPagamento = input('Deseja utilizar cartão Tabajara?(sim/nao)')
if tipoPagamento == 'sim':
    desconto == 0.05

valorDesconto = valorBruto * desconto
valorLiquido = valorBruto - valorDesconto

print('========================================================='
      f'\nTipo de carne:\t\t\t{tipoCarne}'
      f'\nPeso total:\t\t\tKG {peso}'
      f'\nPreço total:\t\t\tR$ {valorBruto}'
      f'\nCompra com cartão:\t\t{tipoPagamento}'
      f'\nvalor do desconto:\t\tR$ {valorDesconto}'
      f'\nValor a pagar:\t\t\tR$ {valorLiquido}'
      '\n=========================================================')