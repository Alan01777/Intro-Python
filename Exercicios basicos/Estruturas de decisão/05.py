'''Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a 
média alcançada por aluno e apresentar:

    A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
    A mensagem "Reprovado", se a média for menor do que sete;
    A mensagem "Aprovado com Distinção", se a média for igual a dez. '''

nota=float(input('Nota do aluno:'))
if nota>=7 and nota<10:
    print('Aprovado')
elif nota<7 and nota>=0:
    print('Reprovado')
elif nota==10:
    print('Aprovado com distinção')
else:
    print('Valor inválido!')