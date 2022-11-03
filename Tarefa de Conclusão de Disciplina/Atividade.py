import sys
import os
import time

clear = lambda: os.system('clear') #função usada para limpar a tela

#Funções axuiliares para chamada das listas/questões
#=================Lista 01=================
def listaI():
    #chamada da questão 1
    def questao01():
        clear()
        print(30 * '=', 'ListaI-Questão:01', 30 * '=')

        #Ainda não foi adicionada

        print('Voltando ao menu...')
        time.sleep(5)
        core()    
        pass
        
    #chamada da questão 2
    def questao02():
        clear()
        print(30 * '=', 'ListaI-Questão:02', 30 * '=')

        #Ainda não foi adicionada

        print('Voltando ao menu...')
        time.sleep(5)
        core()
        pass

    #Menu lista 1
    clear()
    print(30 * '=', 'ListaI', 30 * '=')
    print(f'Selecione suas opções:\n'
          f'1 -Questão 01:\n'
          f'2 -Questão 02:\n'
          f'3 -Voltar ao menu:')
    escolha = int(input("Selecione sua questão: "))

    if (escolha == 1):
        questao01()
    elif (escolha == 2):
        questao02()
    elif (escolha == 3):
        core()
    pass



#=================Lista 02=================
def listaII():
    #Questões utilizadas: 01 e 02
    clear()
    #chamada da questão 1
    def questao01():
        clear()
        print(30 * '=', 'ListaII-Questão:01', 30 * '=')
        print(f'Faça um programa que receba um número inteiro e verifique se este número é\n'
        'maior que 20, em caso afirmativo o programa deverá imprimir a mensagem: "Maior\n'
        'que 20\n')
        #=================
        num = int(input("Insira um número: "))
        if (num > 20):
            print("Maior que 20")
        else:
            print("Menor que 20")
        #=================
        print('Voltando ao menu...')
        time.sleep(5)
        core()
        pass
    
    #chamada da questão 2
    def questao02():
        clear()
        print(30 * '=', 'ListaII-Questão:02', 30 * '=')
        print(f'Faça um programa que receba um número inteiro e verifique se este número é\n'
        'maior que 20, em caso afirmativo o programa deverá multiplicar o valor por 2 e\n'
        'após o cálculo imprimir a mensagem: "Resultado: <valor do resultado>", em que\n'
        '<valor do resultado> deve ser substituído pelo resultado do cálculo\n')
        #=================
        num = int(input("Insira um número maior que 20: "))
        if (num > 20):
            num *= 2
            print(f'Resultado: {num}')
        #=================
        print('Voltando ao menu...')
        time.sleep(5)
        core()
        pass

    #Menu lista 2
    print(30 * '=', 'ListaII', 30 * '=')
    print(f'Selecione suas opções:\n'
          f'1 -Questão 01:\n'
          f'2 -Questão 02:\n'
          f'3 -Voltar ao menu:')
    escolha = int(input("Selecione sua questão: "))

    if (escolha == 1):
        questao01()
    elif (escolha == 2):
        questao02()
    elif (escolha == 3):
        core()
    pass

#=================Lista 03=================
def listaIII():
    #Questões utilizadas: 01 e 02
    #chamada da questão 1
    def questao01():
            clear()
            print(30 * '=', 'ListaIII-Questão:01', 30 * '=')
            print(f'Faça um programa que leia 5 números e informe a soma e a média dos números.\n')
            sum = 0
            #=================
            for i in range(1, 6):
                num = int(input("Insira um número: "))
                sum += num
            media = sum / i
            print(f'Soma: {sum}\n'
                f'Media: {media}')
            #=================
            print('Voltando ao menu...')
            time.sleep(5)
            core()
            pass
        
    #chamada da questão 2
    def questao02():
        clear()
        print(30 * '=', 'ListaIII-Questão:02', 30 * '=')
        ############################################
        print(f'Faça um programa que leia 10 valores e ao final imprima a média aritmética dos\n'
        'valores lidos\n')
        sum = 0
        for i in range(1, 11):
            num = int(input("Insira um valor: "))
            sum += num
        media = sum / i
        print(f'Media: {media}')
        ############################################
        print('Voltando ao menu...')
        time.sleep(5)
        core()
    pass

    #Menu lista 3
    print(30 * '=', 'ListaI', 30 * '=')
    print(f'Selecione suas opções:\n'
          f'1 -Questão 01:\n'
          f'2 -Questão 02:\n'
          f'3 -Voltar ao menu:')
    escolha = int(input("Selecione sua questão: "))

    if (escolha == 1):
        questao01()
    elif (escolha == 2):
        questao02()
    elif (escolha == 3):
        core()
    pass


#Função principal
#=================Menu=================
def core():
    clear()
    print(30 * '=', 'Menu', 30 * '=')
    print(f'Selecione uma lista abaixo:\n'
          f'1 -lista 1: Fundamentos do python\n'
          f'2 -lista 2: Estruturas condicionais\n'
          f'3 -lista 3: Estruturas de repetição\n'
          f'4 - sair')
    escolha = int(input('Escolha: '))

    if (escolha == 1):
        listaI()
    elif (escolha == 2):
        listaII()
    elif (escolha == 3):
        listaIII()
    elif (escolha == 4):
        sair = str(input('Deseja sair? (s/n)'))
        if (sair == 's'):
            sys.exit()
        else:
            core()
    else:
        print("Opção inválida! Tente novamente")
        time.sleep(1.5)
        clear()
        core()
    pass


core()