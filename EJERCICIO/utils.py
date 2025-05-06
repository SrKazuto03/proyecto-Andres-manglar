
import time, os

def mis_materias():
    opcion = input(" Seleccion de materias -> ")
    tipo = list(map(float, opcion.split(",")))

    if opcion == "1":
        return "Ingles"
    elif opcion == "2":
        return "Matematicas"
    elif opcion == "3":
        return "Desarrollo"
    elif opcion == "4":
        return "Historia"
    
def promedio()
    

def delay():
    for i in range(5, 0, -1):
        print(f"Cargando {i}.......")
        time.sleep(1)
        
def limpiarconsola():
    for i in range(5, 0, -1):
        print(f"limpieza en {i}")
        time.sleep(1)
        os.system("clear")
        
        