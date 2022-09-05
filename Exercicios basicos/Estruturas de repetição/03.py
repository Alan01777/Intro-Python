'''Faça um programa que leia e valide as seguintes informações:

    Nome: maior que 3 caracteres;
    Idade: entre 0 e 150;
    Salário: maior que zero;
    Sexo: 'f' ou 'm';
    Estado Civil: 's', 'c', 'v', 'd'; '''
    


nome=str(input('Nome:'))
while len(nome) <=3:
    nome=str(input('Nome:'))

idade=int(input('Idade:'))
while idade<=0 or idade>=150:
    idade=int(input('Idade:'))

salario=float(input('Salário:'))
while salario<0:
    salario=float(input('Salário:'))

sexo=str(input('Sexo:'))
while sexo!= 'f' and sexo!='m':
    sexo=str(input('Sexo:'))

estadoCivil=str(input('Estado civil:'))
while estadoCivil!='s' and estadoCivil!='c' and estadoCivil!='v' and estadoCivil!='d':
    estadoCivil=str(input('Estado civil:'))