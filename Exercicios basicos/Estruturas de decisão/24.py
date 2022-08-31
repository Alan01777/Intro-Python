print('Divisão == /'
      '\nMultiplicação == *'
      '\nAdição == +'
      '\nSubtração == -')

operação = input('Operação a se realizar:')

if operação == '*':
    num1 = float(input('Insira o numero:'))
    num2 = float(input('Insira o numero:'))

    resultado = num1 * num2
elif operação == '/':
    num1 = float(input('Insira o numero:'))
    num2 = float(input('Insira o numero:'))

    resultado = num1 / num2
elif operação == '-':
    num1 = float(input('Insira o numero:'))
    num2 = float(input('Insira o numero:'))

    resultado = num1 - num2
elif operação == '+':
    num1 = float(input('Insira o numero:'))
    num2 = float(input('Insira o numero:'))

    resultado = num1 + num2

else:
    print('Operação inválida!')

print(f'Resultado: {resultado}')
if resultado % 2 == 0:
    print(f'{resultado} é par')
else:
    print(f'{resultado} é impar')
if resultado == round(resultado):
    print(f'{resultado} é inteiro')
else:
    print(f'{resultado} é decimal')
if resultado >= 0:
    print(f'{resultado} é positivo')
else:
    print(f'{resultado} é negativo')
