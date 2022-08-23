#Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros
#quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para
#cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam
#R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

metros_cliente = float(input("Área em metros quadrados a ser pintada:"))
litros_necessarios = metros_cliente / 3
latas_necessarias = int(litros_necessarios / 18)
if (litros_necessarios % 18 != 0):
    latas_necessarias += 1
print("Latas necessárias: ", latas_necessarias)
print("Valor: R$", latas_necessarias * 80)