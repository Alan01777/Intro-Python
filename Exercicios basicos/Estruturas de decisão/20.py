'''Faça um Programa para leitura de três notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e presentar:

    A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
    A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
    A mensagem "Aprovado com Distinção", se a média for igual a 10. 
'''

nota1=float(input('Insira anota:'))
nota2=float(input('Insira anota:'))
nota3=float(input('Insira anota:'))
media=(nota1+nota2+nota3)/3

if (nota1>=0 and nota1<=10) and (nota2>=0 and nota2<=10) and (nota3>=0 and nota3<=10): 
    if media>=7 and media<10:
        print(f'Aluno aprovado: {media:.2f}')
    elif media<7:
        print(f'Aluno Reprovado: {media:.2f}')
    elif media==10:
        print(f'Aluno Reprovado com distinção: {media:.2f}')
else:
    print('Valor Inválido!')
        