#Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y
#el nombre. El grupo A está formado por las mujeres con un nombre anterior a la M y
#los hombres con un nombre posterior a la N y el grupo B por el resto. Escribir un
#programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo
#que le corresponde.
sexo = str(input("Eres chico o chica: "))
nombre = str(input("Ingresa tu nombre: "))
if sexo == "chico" and nombre > "N":
    print("Grupo A")
elif sexo == "chica" and nombre < "M":
    print("Grupo A")
else:
    print("Grupo B") 