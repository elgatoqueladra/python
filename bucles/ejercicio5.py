# Ejercicio 5
# Escribir un programa que pregunte al usuario una cantidad a invertir,
# el interés anual y el número de años, y muestre por pantalla el capital
# obtenido en la inversión cada año que dura la inversión.

capital = float(input("Introduce la cantidad a invertir: "))
interes = float(input("Introduce el interés anual (en %): "))
anios = int(input("Introduce el número de años: "))

for i in range(1, anios + 1):
    capital = capital * (1 + interes / 100)
    print(f"Año {i}: capital acumulado = {capital:.2f} €")
