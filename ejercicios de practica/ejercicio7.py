base = int(input("dime una base"))
exp = int(input("dime un exponente"))
resultado = 1
for i in range(1, exp + 1):
    resultado = resultado *base
print (resultado)