cantidad = float(input("introduce la cantidad a invertir"))
tasa = float(input("introduce el interes anual"))
años = int(input("introduce el numero de años"))

final = cantidad * (1 + tasa / 100) ** años
print("el capital final es", final)
