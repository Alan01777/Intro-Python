#Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule 
# seu peso ideal, utilizando as seguintes fórmulas:
# Para homens: (72.7*h) - 58
# Para mulheres: (62.1*h) - 44.7

genero=input('Qual o seu gênero?')

match genero:
    case "Homem":
        hHomem=float(input('Altura para homem:'))
        print('Seu peso ideal:', (72.7*hHomem) - 58,'KG')
    case "Mulher":
        hMulher=float(input('Altura para mulher:'))
        print('Seu peso ideal:', (62.1*hMulher) - 44.7, 'KG')