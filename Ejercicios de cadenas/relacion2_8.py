precio=str(input("Indique precio de un producto : "))
new=precio.split(".")
euros=new[0]
cents=new[1]
print("El producto  vale",euros,"en €")
print("El producto vale",cents,"em cnts") 
#copiado en clase