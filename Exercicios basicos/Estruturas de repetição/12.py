'''Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. 
O usuário deve informar de qual numero ele deseja ver a tabuada. A saída deve ser conforme o exemplo
abaixo:

    Tabuada de 5:
    5 X 1 = 5
    5 X 2 = 10
    ...
    5 X 10 = 50'''
    
cont=1
num=int(input('Insira um valor entre 1 e 10:'))
if num < 1 and num > 10:
    print('Valor inválido!')
else:
    while cont <=10:
        print(f'{num} * {cont} \t= {num*cont}')
        cont+=1