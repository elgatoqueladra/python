nombre = input("introduce tu nombre")
edad = input("introduce tu edad")
direcciones = input("introduce tu direccion")
telefono = input("introduce tu telefono")
dic = {"nombre":nombre,"edad":edad,"direcciones":direcciones,"telefono":telefono,} 
print (f"{dic['nombre']} tiene {dic['edad']} años vive en {dic['direcciones']} su numero de telefono es {dic['telefono']}")