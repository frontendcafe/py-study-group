# Autor: Javier Rodriguez (Javo.py) | GitHub: JaviCeRodriguez
# Para FrontendCafé 

#///---- Función palindromo ----///
def palindromo(sentencia):
    ''' #docstring
    Descripcion: Obtengo una cadena 'sentencia' y verifico si es palindromo.
    Precondicion: Dar como argumento una cadena con al menos 1 elemento.
    Poscondicion: Devuelve True si es palindromo. De lo contrario, False.
    '''
    cadenaPrincipal = sentencia.replace(' ', '').lower() # Elimino espacio con replace y
                                                        # pongo todo en minusculas con lower
    cadenaReversa = ''.join(reversed(cadenaPrincipal)) # Invierto cadena con reversed y
                                                        # lo convierto en cadena con join (Ustedes: "what?")
    print(cadenaPrincipal)
    print(reversed(cadenaPrincipal)) # Ver texto comentado abajo si descomentan este print
    print(cadenaReversa)
    if (cadenaPrincipal == cadenaReversa): # Si son iguales, es palindromo (True)
        return True
    return False

print('Ingrese frase para palindromear: ', end='') # Pido que escriba una frase
frase = input() # Obtengo la frase y la guardo
print(palindromo(frase)) # Voy a la función


# Seguramente vas a ver algo raro cuando ejecutes la linea 15. Esto se debe a que estamos en 
# presencia de un iterador, que contiene nuestra frase invertida!

# Iteradores: Los iteradores son objetos que utilizan el protocolo iterador. Esto significa que
# podemos utilizar la función 'next()' para obtener la siguiente letra de la secuencia. Aplicamos
# la función 'next()' hasta que Python nos lanza un error 'StopIteration', indicando que llegamos al 
# final de la secuencia del objeto.

# secuencias = [dic1, dic2, dic3]
# dic = {'nombre': 'Javier'}