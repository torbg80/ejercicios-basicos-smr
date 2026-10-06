print("Hola mundo")

#Ejercicio1

def ejercicio1():
    nombre = input("Introduce tu nombre: ")
    print ("Hola", nombre)

#if __name__ == "__main__":
 #   ejercicio1()

#Ejercicio2

def ejercicio2():
    num1=int(input("Introduce el primer numero "))
    num2=int(input("Introduce el segundo numero "))

    suma=num1+num2
    resta=num1-num2
    multiplicacion=num1*num2
    division=num1/num2

    print("Suma", suma)
    print("Resta", resta)
    print("Multiplicacion", multiplicacion)
    print("Division", division)

if __name__ == "__main__":
    ejercicio2()