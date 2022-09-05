'''Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do 
usuário, mostrando uma mensagem de erro e voltando a pedir as informações. '''

condicao = False

while condicao == False:
    usuario = input('Usuário:')
    senha = input('Senha:')
    if usuario != senha:
        condicao = True
    else:
        print('Seu usuário deve ser diferente da sua senha! Tente novamente!\n')