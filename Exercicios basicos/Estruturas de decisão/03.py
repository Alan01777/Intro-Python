#Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

gener = input('Insira o gênero:')

if gener == 'F':
    print('Feminino')
elif gener == 'M':
    print('Masculino')
else:
    print('Gênero inválido!')