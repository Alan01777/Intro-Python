suspeito = 0
print('Responda todas as questões com '
      'sim'
      ' ou '
      'não'
      '')
nome = input('Nome da pessoa:')
telefonou = input(f'{nome} telefonou para a vítima?')
if telefonou == 'sim':
    suspeito += 1
estevaLocal = input(f'{nome} estava no local do crime?')
if estevaLocal == 'sim':
    suspeito += 1
moradia = input(f'{nome} morava perto da vítima?')
if moradia == 'sim':
    suspeito += 1
devia = input(f'{nome} devia para a vítima?')
if devia == 'sim':
    suspeito += 1
jaTrabalhou = input(f'{nome} já trabalhou com a vítima?')
if jaTrabalhou == 'sim':
    suspeito += 1

if suspeito == 2:
    print(f'{nome} é suspeito')
elif suspeito == 3 or suspeito == 4:
    print(f'{nome} é cúmplice')
elif suspeito == 5:
    print(f'{nome} é culpado')