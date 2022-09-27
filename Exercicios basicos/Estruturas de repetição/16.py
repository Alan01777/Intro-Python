''''''


anterior = 0
proximo = 0

n = int(input("Termos: "))

for i in range(n):
    print(proximo)
    proximo = proximo + anterior
    anterior = proximo - anterior

    if proximo == 0:
        proximo = proximo + 1
