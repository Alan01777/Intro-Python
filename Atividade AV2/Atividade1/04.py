'''Um escritório de contabilidade, está realizando o reajuste do salário dos
funcionários de todos os seus clientes. Para isso, estão utilizando como referência
o reajuste acordado com os sindicatos de cada classe trabalhadora, conforme
apresentado na tabela a seguir. Para ajudar o escritório nesta tarefa, faça um
programa que receba o salário atual, o cargo conforme especificado na tabela a
seguir e realize o cálculo do reajuste do salário. Ao término do cálculo o programa
deve imprimir o valor do reajuste e o novo salário do funcionário'''


def reajusteSalario():
    salario = float(input("Informe o salário: "))
    cargo = int(input("Informe o código do cargo: "))

    if (cargo == 1):
        reajuste = 0.07
    elif (cargo == 2):
        reajuste = 0.09
    elif (cargo == 3):
        reajuste = 0.05
    elif (cargo == 4):
        reajuste == 0.12
    else:
        print("Código inválido!")
        reajusteSalario()

    valorReajuste = (salario * reajuste)
    salarioAjuste = (salario * reajuste) + salario

    print(f'Valor do rejuste: {valorReajuste:.2f}\n'
          f'Salario com reajuste: {salarioAjuste}')

    pass


reajusteSalario()