
"""pide al usuario un numero entero y muestralo en consola"""

number_int = int(input("\n\tingresa un numero entre 0 y 100 => "))

print("\n\t", number_int)


""" Pide al usuario su nombre y edad, luego muestra un mensaje como:
 "Hola [nombre], tienes [edad] años." """
 
name = input("\n\tpor favor, ingresa tu nombre => ").upper()
age = int(input("\n\tpor favor, ingresa tu edad => "))
 
print("\n\t!HOLA {} tienes {} años estas viejo compa ".format(name, age))

print("\nPrograma terminado")




""" Ejercicios con operadores aritméticos """

""" 3. Suma de dos números
        a. Pide al usuario dos números y muestra la suma de ambos.
    """
    
number_one = int(input("\n\tIngresa un numero para sumar => "))
number_two = int(input("\n\tIngresa otro numero para sumar => "))

total = number_one + number_two

print("\n\tEl resultado de la suma es => {} " .format(total))

print("\nPrograma terminado")


"""   4. Resta de dos números
        a. Pide al usuario dos números y muestra la resta del primero menos el segundo.
 """
 
print("\n\tBIENVENIDO A LA CALCULADORA DE RESTAS INSERTAR NUMEROS PARA PODER RESTAR 2 NUMEROS ")
number_1x = int(input("\n\tPor favor ingresa un numero para restar  =>  "))
number_2x = int(input("\n\tor favor ingresa otro numero para restar =>  "))

total = number_1x - number_2x

print("\n\tel resultado de la resta es => {} ".format(total))

print("\nPrograma terminado")


""" . Multiplicación de dos números
        a. Pide al usuario dos números y muestra el resultado de multiplicarlos. 
        """ 
        
print("\n\t!Bienvenido a la calculadora para multiplicar 2 numeros ")
    
number_1xx = int(input("\n\t !Por favor ingresa un numero para multiplicar => "))
number_2xx = int(input("\n\t !Por favor , ingresa otro numero para multiplicar => "))

total = number_1xx * number_2xx

print("\n\t!El resultado de multiplicar es => {}".format(total))

print("\nPrograma terminado")


"""    6. División de dos números
        a. Pide al usuario dos números y muestra el resultado de dividir el primero por el segundo.
        b. Asegúrate de que el segundo número no sea cero.
 """


number1 = int(input("Ingresa un numero para dividir => "))
number2 = int(input("Ingresa otro numero para dividir => "))

total = number1 // number2

print("El resultado de la division es => {}".format(total))

print("\n\tPrograma terminado")



""" 
    7. Promedio de tres números
        a. Pide al usuario tres números y muestra su promedio. 
        """

number1 =int(input("ingresa un numero => "))
number2 =int(input("ingresa un numero => " ))
number3 = int(input("ingresa un numero => "))

totals = number1 + number2 + number3

p = total // 3 

print("El resultado de la operacion es => {}".format(p))



