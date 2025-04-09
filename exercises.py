
list = []
# list2 = []
print(""" \n\tBienvenido al test de añadir elementos a una lista """)

number = input("por favor ingrese varios numeros entre (0 y 10) => ")
number_type = number.split(",")
list.append(number)

number = input(""" ¿desea agregar mas elementos a la lista ?
             
              1. (si)
              2. (no)
              
              "!Por favor Ingrese el valor que desea! "
              """)

while number.lower() == "si" or number == "1":
    number = input("por favor ingrese nuevamente un numero entre (0 y 10) => ")
    list.append(number)
    adicional = input(""" ¿desea agregar mas numeros a la lista?               
              1. (si)
              2. (no)
              
              "!Por favor ingrese el valor que desea!
              """)
    while adicional == "no" or adicional == "2":
        break
        
    conclusion = input("por favor pulse una tecla para continuar la aplicacion => ")
    break
    
print(f"los numeros ingresados por el usuario son {list}")
input("pulse una tecla para salir => ")

    
    
    
   
    




        
        
    