'''Segundo uma tabela médica, o peso ideal está relacionado com a altura e o sexo.
Faça um programa que receba a altura e o sexo de uma pessoa, após isso calcule
e imprima o seu peso ideal, utilizando as seguintes fórmulas:
• Para homens: (72,7 * A) – 58
• Para mulheres: (62,1 * A) – 44,7
Em que: A = Altura'''


def pesoIdeal():
    genero = str(input("Insira seu gênero (masculino ou feminino): "))
    altura = float(input("Insira sua altura (m): "))
    if (genero == "masculino") or (genero == "Masculino"):
        imc = (72.7 * altura) - 58
    elif (genero == "feminino") or (genero == "Feminino"):
        imc = (62.1 * altura) - 44.7

    print(f'IMC: {imc:.2f}')
    pass


pesoIdeal()