"""
1. Suma condicional de números impares del 1 al 100 que no sean múltiplos de 3
Recorre del 1 al 100 y suma solo los impares que no sean múltiplos de 3."""
# imparesTres = 0
# pares = 0

# for num in range(1,101):
#     if(num % 2 != 0) and (num % 3 != 0):
#         #print(num)
#         imparesTres += num
#     else:
#         pares += num
    
# print(f" la suma de numeros impares => {imparesTres} y la suma de los  numeros pares son => {pares}  " )



"""Ingresa una palabra y reemplaza cada vocal por un carácter:"""

word = input("palabra => ")
words1 = ""

for character in word:
    if character in ["a", "e", "i", "o", "u"]:
        character = "@" 
        words1 += character 
    else:
        words1 += character
        
print(words1)
        
   
        
        

# """Ingresa una cadena y encuentra la letra que más se repite (sin usar librerías)."""

# cadena = input("ingresa lo que sea => ")

# letra = 0

# for letra in cadena:
#     if cadena.count("a"):
#         letra += 1
#         print(letra)
        


        