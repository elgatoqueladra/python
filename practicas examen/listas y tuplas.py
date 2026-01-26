#Ejercicio 1
#Escribir un programa que almacene las asignaturas de un curso (por ejemplo
#Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por
#pantalla.

lista = ["Matematicas","Fisica","Quimica"]
print ( lista) 

#Ejercicio 2
#Escribir un programa que almacene las asignaturas de un curso (por ejemplo
#Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por
#pantalla el mensaje Yo estudio <asignatura>, donde <asignatura> es cada
#una de las asignaturas de la lista.

listas = ["Matematicas","Fisica","Quimica"]
for i in listas :
    print ("yo estudio", i) 

#Ejercicio 3
#Escribir un programa que almacene las asignaturas de un curso (por ejemplo
#Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la
#nota que ha sacado en cada asignatura, y después las muestre por pantalla con el
#mensaje En <asignatura> has sacado <nota> donde <asignatura> es
#cada una des las asignaturas de la lista y <nota> cada una de las correspondientes
#notas introducidas por el usuario.

listas = ["Matematicas", "Física", "Química", "Historia", "Lengua"]
for i in listas :
    n=int(input("dime que nota has sacado en " + i))
    print(f"Tu nota en {i} es {n}")

#Ejercicio 4
#Escribir un programa que pregunte al usuario los números ganadores de la lotería
#primitiva, los almacene en una lista y los muestre por pantalla ordenados de menor
#a mayor.

lista = [2 , 4 , 7 ]
while True:
    primitiva = int(input("dime tu numero ganador de loteria entre el 1 al 10"))
    for i in lista:
        if primitiva in lista:
            print ("eres ganador de la loteria")
        else :
             print ("no has ganado nada")
    
        break
#Ejercicio 4
#Escribir un programa que pregunte al usuario los números ganadores de la lotería
#primitiva, los almacene en una lista y los muestre por pantalla ordenados de menor
#a mayor.

    lista = []
    for i in range (0,6):
        lista.append (int(input("dime los numero ganador de loteria entre el 1 al 10")))
    lista.sort()
    print (f"los numeros ganadores de la primitiva son : ", lista)

#Ejercicio 5
#Escribir un programa que almacene en una lista los números del 1 al 10 y los
#muestre por pantalla en orden inverso separados por comas.
    listas=[1,2,3,4,5,6,7,8,9,10]
    listas.reverse()
    print (listas, end=" ,")

#Ejercicio 6
#Escribir un programa que almacene las asignaturas de un curso (por ejemplo
#Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la
#nota que ha sacado en cada asignatura y elimine de la lista las asignaturas
#aprobadas. Al final el programa debe mostrar por pantalla las asignaturas que el
#usuario tiene que repetir

    asignaturas = ["Matematicas", "Fisica", "Quimica"]
    repetir = []

    for a in asignaturas:
        nota = int(input(f"¿Qué has sacado en {a}? "))
        if nota <= 5:
            repetir.append(a)

    print("Tienes que repetir:", repetir)

 #Ejercicio 6
#Escribir un programa que almacene las asignaturas de un curso (por ejemplo
#Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la
#nota que ha sacado en cada asignatura y elimine de la lista las asignaturas
#aprobadas. Al final el programa debe mostrar por pantalla las asignaturas que el
#usuario tiene que repetir

    asignaturas = ["Matematicas", "Fisica", "Quimica"]
    for i in asignaturas[:]:
        nota = int(input(f"¿Qué has sacado en {i}? "))
        if nota >= 5:
            asignaturas.remove(i)
    print("Tienes que repetir:", asignaturas)

#Ejercicio 7
#Escribir un programa que almacene el abecedario en una lista, elimine de la lista las
#letras que ocupen posiciones múltiplos de 3, y muestre por pantalla la lista
#resultante.

    ABC = list("abcdefghijklmnopqrstuvwxyz")
    resultado = []

    for i in range(len(ABC)):   
        if i % 3 != 0:          
            resultado.append(ABC[i])
    print(resultado)

#Ejercicio 8
#Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un
#palíndromo.
    while True:
        palabra = (input("dime una palabra palindrome :")) 
        if palabra == palabra[::-1]:
            print (f"tu palabra {palabra} es palindrome")
            break
        else:
            print ("no lo es")
#9
    palabra = input("Dime una palabra: ")

    a = e = i = o = u = 0

    for letra in palabra:
        if letra == "a":
            a += 1
        elif letra == "e":
            e += 1
        elif letra == "i":
            i += 1
        elif letra == "o":
            o += 1
        elif letra == "u":
            u += 1

    print("a:", a)
    print("e:", e)
    print("i:", i)
    print("o:", o)
    print("u:", u)