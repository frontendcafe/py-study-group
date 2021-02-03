import unidecode

def palindromo(sentencia, inicio, longitud):
    # Función que recibe como argumento 3 valores, el primero es una cadena de caracteres la cual la función verifica si es palíndromo retornando un valor booleano.
    # Los valores inicio y longitud son de tipo entero, para comparar las posiciones iniciales con las finales.
    
    # Zona de inicialización de variable
    exito = False

    if inicio == longitud or inicio < longitud:
        if sentencia[inicio] == sentencia[longitud]:
            exito = True
    else:
        exito = palindromo(sentencia, inicio+1, longitud-1)
        if sentencia[inicio] == sentencia[longitud]:
            exito = True
        else:
            exito = False

    return exito

def verificar_condicion(condicion):
    # Función que dada una cadena de caracteres recibida como argumento, verifica que sea SI sin importar las ocurrencias, retornando un valor booleano.

    # Zona de inicialización de variables
    i = 0
    familia = ["SI","Si","si","sI","SÍ","Sí","sí","sÍ"]
    encontrado = False  # Busca la ocurrencia de SI dentro de la lista familia
    continuar = True    # Valor a retornar
    longitud_familia = len(familia)-1

    while encontrado == False and i <= longitud_familia:
        if familia[i] == condicion:
            encontrado = True   # Encontró la palabra que buscaba
        else:
            i = i + 1   # Si no encontró la palabra, sigo buscando

    if not encontrado:
        continuar = False   # Si no encontro la palabra SI en la lista, retorna False
    
    return continuar

# Zona de inicialización de variable
cont = True

while(cont):

    # Zona de inicialización de variables dentro del bucle
    encontrado = False 
    inicio = 0
    print("Ingrese la palabra que desea verificar si es palíndromo o no")
    palabra_original = input()

    palabra = (palabra_original.replace(" ","")).lower()  #Le quito los espacios y transformo los caracteres a minúsculos
    
    resultado = unidecode.unidecode(palabra) # Utilizo la librería unidecode para sacar los acentos de las vocales

    longitud = len(resultado)-1 
    
    print("palabra_original:", palabra_original)
    print("palabra:", palabra)
    print("resultado:", resultado)
    # Invocación de la función palindromo que verifica si la palabra ingresada es o no palindromo
    exito = palindromo(resultado, inicio, longitud)

    if exito:
        print("La palabra",palabra_original,"es palíndromo")
    else:
        print("La palabra",palabra_original,"no es palíndromo")
    
    print("¿Desea continuar?. Ingrese SI, en caso contrario ingrese cualquier letra.")
    condicion = input()

    cont = verificar_condicion(condicion)