asignaturas = {
    "matematicas": "6",
    "fisica": "4",
    "quimica": "5"
}
suma = 0
for asignaturas, creditos in asignaturas.items():
    print(f"{asignaturas} tiene {creditos} creditos")
    suma += int(creditos)
print (f"la suma total de tus creditos es : {suma}")