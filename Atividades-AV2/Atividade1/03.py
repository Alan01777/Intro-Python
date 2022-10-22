'''Faça um programa que receba um número inteiro e verifique se este número é
maior que 20, em caso afirmativo o programa deverá multiplicar o valor por 2 e em
caso negativo deve multiplicar por 4. Após realizar o cálculo o programa deve
imprimir a mensagem: "Resultado: <valor do resultado>", em que <valor do
resultado> deve ser substituído pelo resultado do cálculo'''

def mult():
    num = int(input("Insira um número: "))

    if (num > 20):
        num *= 2
    else:
        num *= 4

    print(f'Resultado: {num}')
    pass
mult()