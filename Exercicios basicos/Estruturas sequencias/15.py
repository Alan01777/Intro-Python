#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
#Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11%
#para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:

#   salário bruto.
#   quanto pagou ao INSS.
#   quanto pagou ao sindicato.
#   o salário líquido.

#   calcule os descontos e o salário líquido, conforme a tabela abaixo:
#   + Salário Bruto : R$
#   - IR (11%) : R$
#   - INSS (8%) : R$
#   - Sindicato ( 5%) : R$
#   = Salário Liquido : R$

ganhoHora = float(input('Ganho por hora:'))
horasMes = float(input('Horas trabalhadas por mês:'))
salarioBruto = ganhoHora * horasMes
print('Salario Bruto: R$', salarioBruto)
print('Valor pago ao INSS: R$', salarioBruto * 0.08)
print('Valor pago para IR: R$', salarioBruto * 0.11)
print('Valor pago ao Sindicato: R$', salarioBruto * 0.05)
print('Salario líquido: R$', salarioBruto - (salarioBruto * 0.24))
