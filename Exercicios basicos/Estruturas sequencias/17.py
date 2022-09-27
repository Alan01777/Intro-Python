#Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros
#quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para
#cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam
#R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
#-Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
#-comprar apenas latas de 18 litros;
#-comprar apenas galões de 3,6 litros;
#-misturar latas e galões, de forma que o desperdício de tinta seja menor.
#Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

metrosCliente = float(input("Área em m²:"))

litros = (metrosCliente / 6)*1.1
quantidadeLatas = int(litros / 18)

if (metrosCliente % 18 != 0):
    quantidadeLatas += 1
quantidadeGaloes = int((litros / 3.6))
if (metrosCliente % 3.6 != 0):
    quantidadeGaloes += 1

quantidadeGaloesMisto = int(litros/3.6)
quantidadeLatasMisto =((litros - quantidadeGaloesMisto * 3.6) / 18)
valorGalaoMisto = quantidadeGaloesMisto * 25
valorLataMisto = quantidadeLatasMisto * 80

print("Latas necessárias:", quantidadeLatas, "\tPreço: R$", quantidadeLatas * 80)
print("Galões necessários:", quantidadeGaloes, "\tPreço: R$", quantidadeGaloes * 25)

print('considerando o menor desperdíciode tinta, temos:')
print(f'quantidade galões: {quantidadeGaloesMisto:.0f}')
print(f'quantidade latas: {quantidadeLatasMisto:.0f}')
print(f'quantidade total mistas: {quantidadeGaloesMisto + quantidadeLatasMisto:.0f}')
print(f'valor total considerando GALOES e LATAS é: R$ {valorGalaoMisto + valorLataMisto:.2f}')