'''As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe 
contraram para desenvolver o programa que calculará os reajustes.

    Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, 
    baseado no salário atual:
    -salários até R$ 280,00 (incluindo) : aumento de 20%
    -salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
    -salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
    -salários de R$ 1500,00 em diante : aumento de 5% 
    Após o aumento ser realizado, informe na tela:
    -o salário antes do reajuste;
    -o percentual de aumento aplicado;
    -o valor do aumento;
    -o novo salário, após o aumento. '''

salarioBase = float(input('Salário original:'))
if salarioBase <= 280:
    ajuste = 0.2
    porcentagemAjuste = '20%'
    valorAjuste = salarioBase * ajuste
    novoSalario = salarioBase + valorAjuste
elif salarioBase > 280 and salarioBase <= 700:
    ajuste = 0.15
    porcentagemAjuste = '15%'
    valorAjuste = salarioBase * ajuste
    novoSalario = salarioBase + valorAjuste
elif salarioBase > 700 and salarioBase <= 1500:
    ajuste = 0.1
    porcentagemAjuste = '10%'
    valorAjuste = salarioBase * ajuste
    novoSalario = salarioBase + valorAjuste
elif salarioBase > 1500:
    ajuste = 0.05
    porcentagemAjuste = '5%'
    valorAjuste = salarioBase * ajuste
    novoSalario = salarioBase + valorAjuste

print(f'Salário antes do reajuste: \tR${salarioBase:.2f}')
print(f'Percentual de aumento: \t\t{porcentagemAjuste}')
print(f'Valor do aumento: \t\tR${valorAjuste:.2f}')
print(f'Novo salário, apoś o aumento: \tR${novoSalario:.2f}')