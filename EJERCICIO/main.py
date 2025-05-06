
from utils import *

data = {}

print("----------Welcome to university----------")

name = input("nombre y apellido -> ").capitalize()
data["Nombre -> "] = name
no_subjects = int(input("Numero de materias ->"))
data["Num Materias-> "] = no_subjects

materias = """
             1. (Ingles)
             2. (Matematicas)
             3. (Desarrollo)
             4. (Historia)
"""

print(materias)

mis_materias()
delay()    

print(f""""-----------Datos de usuario-----------
      Resumen :
      nombre -> {name}
      numero de materias -> {no_subjects} 
      materias -> 
      """)


        



