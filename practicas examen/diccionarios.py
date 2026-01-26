#Ejercicio 1
#Escribir un programa que guarde en una variable el diccionario {'Euro':'€',
#'Dollar':'$', 'Yen':'¥'}, pregunte al usuario por una divisa y muestre su
#símbolo o un mensaje de aviso si la divisa no está en el diccionario.

divisa = {'Euro':'€','Dollar':'$', 'Yen':'¥'}
p=input("dime una divisa")
if p in divisa:
    print (divisa[p])
else:
    print ("Este no esta")

#Ejercicio 2
#Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono
#y lo guarde en un diccionario. Después debe mostrar por pantalla el mensaje
#<nombre> tiene <edad> años, vive en <dirección> y su número de
#teléfono es <teléfono>.

persona = {}

persona.update({
    "nombre": input("Dime tu nombre: "),
    "edad": input("Dime tu edad: "),
    "direccion": input("Dime tu dirección: "),
    "telefono": input("Dime tu teléfono: ")
})

print(f'{persona["nombre"]} tiene {persona["edad"]} años, vive en {persona["direccion"]} y su número de teléfono es {persona["telefono"]}.')

#Ejercicio 3
#Escribir un programa que guarde en un diccionario los precios de las frutas de la
#tabla, pregunte al usuario por una fruta, un número de kilos y muestre por pantalla el
#precio de ese número de kilos de fruta. Si la fruta no está en el diccionario debe
#mostrar un mensaje informando de ello.

frutas = {"platano": 1.20, "naranja": 1.35, "manzana": 2.50}

fruta = input("Dime una fruta: ")
kilos = float(input("Dime los kilos: "))

if fruta in frutas:
    precio_total = kilos * frutas[fruta]
    print(f"{kilos} kg de {fruta} cuestan {precio_total:.2f} €")
else:
    print("Esa fruta no está en el diccionario.")

#Ejercicio 4
#Escribir un programa que pregunte una fecha en formato dd/mm/aaaa y muestre
#por pantalla la misma fecha en formato dd de <mes> de aaaa donde <mes> es
#el nombre del mes.

dic={"01":"enero", "02":"febrero","03":"marzo","04":"abril"}
fecha=input("dime una fecha con formato dd/mm/aaaa")
dia, mes, anio = fecha.split("/")
print(f"{dia} de {dic[mes]} de {anio}")

#Ejercicio 5
#Escribir un programa que almacene el diccionario con los créditos de las asignaturas
#de un curso {'Matemáticas': 6, 'Física': 4, 'Química': 5} y después
#muestre por pantalla los créditos de cada asignatura en el formato <asignatura>
#tiene <créditos> créditos, donde <asignatura> es cada una de las
#asignaturas del curso, y <créditos> son sus créditos. Al final debe mostrar
#también el número total de créditos del curso.

asignaturas = {
    "matematicas": 6,
    "fisica": 4,
    "quimica": 5
}
suma = 0
for asignaturas, creditos in asignaturas.items():
    print(f"{asignaturas} tiene {creditos} creditos")
    suma = suma + creditos
print (f"la suma total de tus creditos es : {suma}")

#Ejercicio 5
#Escribir un programa que almacene el diccionario con los créditos de las asignaturas
#de un curso {'Matemáticas': 6, 'Física': 4, 'Química': 5} y después
#muestre por pantalla los créditos de cada asignatura en el formato <asignatura>
#tiene <créditos> créditos, donde <asignatura> es cada una de las
#asignaturas del curso, y <créditos> son sus créditos. Al final debe mostrar
#también el número total de créditos del curso.

asignaturas = {
    "matematicas": 6,
    "fisica": 4,
    "quimica": 5
}
suma = 0
for asignaturas, creditos in asignaturas.items():
    print(f"{asignaturas} tiene {creditos} creditos")
    suma = suma + creditos
print (f"la suma total de tus creditos es : {suma}")

#Ejercicio 6
#Escribir un programa que cree un diccionario vacío y lo vaya llenado con
#información sobre una persona (por ejemplo nombre, edad, sexo, teléfono, correo
#electrónico, etc.) que se le pida al usuario. Cada vez que se añada un nuevo dato
#debe imprimirse el contenido del diccionario.

dic = {}
nombre=input("dime tu nombre :")
dic.update({"nombre":nombre})
print (dic)
apellido=input("dime tu apellido :")
dic.update({"apellido":apellido})
print (dic)
edad=input("dime tu edad :")
dic.update({"edad":edad})
print (dic)

