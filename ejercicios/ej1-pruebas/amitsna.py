"""
#Versión Función:

def palindromo(sentencia):
  print(sentencia.lower().replace(" ", "") == sentencia.lower().replace(" ", "")[::-1])

sentencia = input("Ingrese la frase a validar: ")

palindromo(sentencia)
"""

palindromo = lambda sentencia: print(sentencia.lower().replace(" ", "") == sentencia.lower().replace(" ", "")[::-1])

sentencia = input("Ingrese la frase a validar: ")

palindromo(sentencia)
