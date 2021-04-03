#La tarea es ordenar una cadena determinada. 
#Cada palabra de la cadena contendrá un solo número. 
#Este número es la posición que debería tener la palabra en el resultado.

#Nota: Los números pueden ser del 1 al 9. Por lo tanto, 1 será la primera palabra (no 0).

#Si la cadena de entrada está vacía, devuelve una cadena vacía. Las palabras en la cadena de entrada solo contendrán números consecutivos válidos.


def order(sentence):
    lista = sentence.split()
    lista2 = []
    for palabra in lista:
        for letra in palabra:
            if letra == '1':
                lista2.append(palabra)
    for palabra in lista:
        for letra in palabra:
            if letra == '2':
                lista2.append(palabra)   
    for palabra in lista:
        for letra in palabra:
            if letra == '3':
                lista2.append(palabra)
    for palabra in lista:
        for letra in palabra:
            if letra == '4':
                lista2.append(palabra)
    for palabra in lista:
        for letra in palabra:
            if letra == '5':
                lista2.append(palabra)
    for palabra in lista:
        for letra in palabra:
            if letra == '6':
                lista2.append(palabra)
    for palabra in lista:
        for letra in palabra:
            if letra == '7':
                lista2.append(palabra)
    for palabra in lista:
        for letra in palabra:
            if letra == '8':
                lista2.append(palabra)
    for palabra in lista:
        for letra in palabra:
            if letra == '9':
                lista2.append(palabra)
    nuevo = ' '.join(lista2)
    return nuevo
