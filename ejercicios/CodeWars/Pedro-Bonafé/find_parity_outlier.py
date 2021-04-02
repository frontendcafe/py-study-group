#El ejercicio pedía definir una funcion que tomara un array de enteros con una característica peculiar, poseía todos los valores pares excepto uno impar, o viceverza
#la funcion debía tomar dicho array y devolver el elemento "distinto" (en el caso del array con mayoría pares devolver el unico elemento impar y viceverza)

def find_outlier(integers):
    pares = []
    impares = []
    for i in integers:
        if i % 2 == 0:
            pares.append(i)
            
        else:
            impares.append(i)
            
    if len(pares) == 1:
        return pares[0]
    else:
        return impares[0]
    
    
    return 
