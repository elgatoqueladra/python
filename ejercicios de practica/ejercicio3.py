saldo = float (1000)
salir = ""
while salir != "4":
    print ("1 saldo")
    print ("2 ingreso")
    print ("3 reintegro")
    print ("4 salir")
    salir = input ("¿Que opcion quieres usar?")
    if salir == "1":
        print ("el dinero total es de", total)
    elif salir == "2":
        ingresar = float(input("cuanto quieres meter "))
        total = saldo + ingresar
        saldo = total
        print ("el dinero total es de", total)
    elif salir == "3":
        sacar = float(input("cuanto quieres sacar "))
        total = saldo - sacar
        saldo = total
        print ("el dinero total es de", total)