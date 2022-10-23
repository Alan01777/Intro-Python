'''Faça um programa que leia 10 números positivos e imprima o quadrado de cada
número. Para cada entrada de dados deverá haver um trecho de validação para
que um número negativo não seja aceito pelo programa'''

def quadrado():
    for i in range(1, 11):
        num = float(input("Insira um valor: "))
        if (num>=0):
                quadrad = num**2
                print(f"Quadrado: {quadrad}")
        else:
                print("Não são permitidos valores negativos!")    
                quadrado()
        
    
    pass
quadrado()