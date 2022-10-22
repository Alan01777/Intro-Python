'''Faça um programa que receba um número inteiro e verifique se este número é
maior que 20, em caso afirmativo o programa deverá multiplicar o valor por 2 e
após o cálculo imprimir a mensagem: "Resultado: <valor do resultado>", em que
<valor do resultado> deve ser substituído pelo resultado do cálculo'''

def mult():
    num = int(input("Insira um número: "))

    if (num > 20):
        num *= 2
        print(f'Resultado: {num}')
    pass

mult()