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



