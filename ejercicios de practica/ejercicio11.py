altura = int(input("Introduce la altura: "))
numero = altura - 1 

for i in range(altura):
    print(" " * numero + " * ")
    numero -= 1