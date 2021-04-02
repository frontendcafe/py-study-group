#Dados dos enteros ayb, que pueden ser positivos o negativos, 
#el ejercicio pide encontrar la suma de todos los enteros entre ellos, a y b inclusive, y devolverla
#Si los dos números son iguales, devuelver a o b.

#Nota: ¡ayb no están ordenados!


def get_sum(a,b):
    if a==b:
        return a 
    if a<b:
        lista= list(range(a,b+1))
        suma = 0
        for i in lista:
            suma += i 
        return suma
    else:
        lista = list(range(b,a+1))
        suma = 0
        for i in lista:
            suma += i
        return suma
