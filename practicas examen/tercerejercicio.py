#Escribe un programa que imprima los números del 1 al 50, pero: 
#● Si el número es múltiplo de 3, imprime "Fizz". 
#● Si es múltiplo de 5, imprime "Buzz". 
#● Si es múltiplo de ambos, imprime "FizzBuzz". 

for i in range(1,51):
    if (i % 5 == 0 and i % 3 == 0):
        print("FizzBuzz")
    elif(i % 5 == 0):
        print("buzz")
    elif(i % 3 == 0):
        print( "Fizz")
    else:
        print(i)
        