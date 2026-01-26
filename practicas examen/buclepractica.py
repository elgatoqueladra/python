#Ejercicio 5
#Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual
#y el número de años, y muestre por pantalla el capital obtenido en la inversión cada
#año que dura la inversión.

invertir = int(input("dime lo que quieres invertir"))
anio = int(input("dime el numeros de años"))
interes = int(input("dime el interes anual"))

for año in range(1, anio + 1):
    invertir = invertir * (1 + interes / 100)
    print(f"Año {año}: {invertir:.2f} €")