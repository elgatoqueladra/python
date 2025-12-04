
numeros = []
print("Introduce los 6 números ganadores de la lotería primitiva:")

for i in range(5):
    numero = int(input(f"Introduce el número {i+1}: "))
    numeros.append(numero)
numeros.sort()
print("Números ganadores ordenados de menor a mayor:")
print(numeros)
