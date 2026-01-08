#programa añadir un menu
lista=[1 ,2 ,3 ,4 ,5 ,6 ,7 ,8 ,9]
while True:
    print ("1.Añadir numero a la lista")
    print ("2.Añadir numero de la lista en una posicion")
    print ("3.Longitud de la lista")
    print ("4.Eliminar el ultimo numero")
    print ("5.Eliminar numero")
    print ("6.Contar numeros")
    print ("7.Posiciones de un numero")
    print ("8.Mostrar numeros")
    print ("9.Salir")

    Menu = int(input("Eliga una opcion: "))

    if Menu == 9:
        print ("Saliendo del programa")
        break
    elif Menu ==1:
        print("opcion1")
        v=int(input("Que numero quieres añadir :"))
        lista.append(v)
    elif Menu == 8:
        for i in lista:
            print(i, end=" ")
            print("")
    elif Menu == 3:
        longitud = len(lista)
        print(longitud)
    elif Menu == 2:
        n = int(input("introduce el numero a añadir: "))
        p = int(input("introduce la posicion: "))
        pos = p -1
        lista.insert(n,p)
        print(f"el numero {n} ha sido añadido")
    elif Menu == 4:
        lista.pop()
    elif Menu == 5:
        n = int(input("dime un numero para eliminar"))
        lista.remove(n)
    elif Menu == 7:
        posicion = int(input("dime un numero"))
        contador = 0
        for numero in lista:
            contador = contador +1
            if numero == posicion:
                print(contador)
