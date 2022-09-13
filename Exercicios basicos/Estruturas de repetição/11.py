'''Altere o programa anterior para mostrar no final a soma dos números. '''

min=int(input('Valor mínimo:'))
max=int(input('valor máximo:'))
soma=0
while (min<(max-1)):
    min+=1
    soma+=min
    print(min)

print(soma)