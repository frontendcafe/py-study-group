# Autor: Javier Rodriguez (Javo.py) | GitHub: JaviCeRodriguez
# Para FrontendCafé 

#! Desarrollar una función que, al recibir una cadena de text la formatea para que siempre contenga un máximo de 30
#! caracteres y la finaliza con un salto de línea.

#! En caso de tener menos de 30 caracteres, le completa con espacios en blanco por la derecha hasta completar los 30 
#! y luego la finaliza con salto de línea.

#! En caso de tener 30 caracteres exactos, le añade un salto de línea.
#! En caso de tener más de 30 caracteres, la fracciona en distintas cadenas de máximo 30 y les realiza mismas operatorias.

def justifica(text):
    '''
    Description: Justifica texto a 30 caracteres por linea
    Pre: Recibe texto
    Pos: Devuelve texto justificado
    '''
    newText = ''
    while len(text) >= 30:
        newText += texto[0:30] + '\n'
        text = text[30:]
    newText += texto[0:] + '\n'
    
    return newText

print('Escribite algo: ', end='')
texto = input()
print(justifica(texto))