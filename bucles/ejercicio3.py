#Ejercicio 3
#Escribir un programa que pida al usuario un número entero positivo y muestre por
#pantalla todos los números impares desde 1 hasta ese número separados por
#comas.

p=int(input("introduce un numero positivo"))
for i in range (1,p+1,2):
    print(i, end=",")
