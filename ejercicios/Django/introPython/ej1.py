def suma(x, y):
    '''
    Realiza la suma de dos números
    '''
    return x + y

def resta(x, y):
    '''
    Realiza la resta de dos números
    '''
    return x - y

def producto(x, y):
    '''
    Realiza el producto de dos números
    '''
    return x * y

def division(x, y):
    '''
    Realiza la divisón de dos números\n
    Devuelve "Inf" si "y" es 0
    '''
    if y == 0:
        return 'Inf'
    else:
        return x / y


a = 20
b = 0

print(suma(a, b))
print(resta(a, b))
print(producto(a, b))
print(division(a, b)) # Ojo acá!