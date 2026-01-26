#Ejercicio 1
#Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10
#veces.
palabra = input("Dime una palabra")
for i in range (1, 10):
    print (palabra)

#Ejercicio 2
#Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos
#los años que ha cumplido (desde 1 hasta su edad).
anios = int(input("dime cuantos años tienes"))
for i in range (1 , anios +1):
    print (i)

#Ejercicio 3
#Escribir un programa que pida al usuario un número entero positivo y muestre por
#pantalla todos los números impares desde 1 hasta ese número separados por
#comas.
positivo =int(input("dime un numero positivo"))
for i in range(1, positivo, +1):
    if i % 2 != 0:
        print (i, end=" , ")

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