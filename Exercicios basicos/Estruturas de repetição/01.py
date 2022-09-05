'''Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido 
e continue pedindo até que o usuário informe um valor válido. '''

condicao=False
while condicao==False:
    num=int(input('Insira um valor de 0 a dez:'))
    if num>=0 and num<=10:
        condicao=True
    else:
        print('Valor Inválido')
        condição=False