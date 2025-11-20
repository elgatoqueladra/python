num = int(input("introduce el numero"))
suma = num
mayor = num
menor = num
for i in range (1,6):
    num=int(input("Di un numero"))
    suma = num + suma
    if mayor < num:
        mayor = num
    elif menor < num:
        menor = num
print ("La suma total es de ", suma)
print ("el numero mas grande es  ", mayor)
print ("el numero mas pequeño es  ", menor)