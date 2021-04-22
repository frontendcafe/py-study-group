# return masked string
def maskify(cc):
    cadena = list(cc)
    longitud = len(cc)-4
    
    for x in range(0, longitud):
        cadena[x] = "#"
    cadena = ''.join(cadena)
    return cadena