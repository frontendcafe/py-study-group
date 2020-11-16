# Autor: Javier Rodriguez (Javo.py) | GitHub: JaviCeRodriguez
# Para FrontendCafé 

#! Formato de diccionario
#! {'SecuenciaN': 'secuencia', 'Num secuencias': 'cantidad', 'Num codones': 'cantidad'}

from pprint import pprint

#///---- Función deteccion ----///
def deteccion(secuencias):
    listSecuencias = [] # Guardo diccionarios de secuencias
    auxSecuencia = ''
    listCantCodones = []
    cantCodones = 0

    for nucleotido in secuencias:
        if (nucleotido.islower()) or (not nucleotido.isalpha()):
            return [], []

    while len(secuencias) >= 3:
        if secuencias[0:3] == 'AUG':
            auxSecuencia = secuencias[0:3]
            cantCodones = 1

        elif secuencias[0:3] in ['UAA', 'UAG', 'UGA']:
            if len(auxSecuencia) <= 3:
                auxSecuencia == ''
                cantCodones = 0

            else:
                auxSecuencia += secuencias[0:3]
                listSecuencias.append(auxSecuencia)
                auxSecuencia = ''
                cantCodones += 1
                listCantCodones.append(cantCodones)

        elif auxSecuencia[0:3].islower():
            cantCodones = 0
            auxSecuencia = ''

        elif auxSecuencia[0:3] == 'AUG':
            auxSecuencia += secuencias[0:3]
            cantCodones += 1

        secuencias = secuencias[3:]

    return listSecuencias, listCantCodones

#///---- Función dictSave ----///
def dictSave(listSec):
    dictsSec = []

    for n, _ in enumerate(listSec):
        numSecuencia = 'Secuencia ' + str(n+1) 
        dictsSec.append({numSecuencia: listSec[n], 'Codones': len(listSec[n])//3})

    pprint(dictsSec, width=1)

#///---- Main ----///
validSecuencias = []
secuencias = ['AUGGGGUaUxAXUA-AGGUaG',
              'UAGAUGGAAUUUAUGGAAUUUUAAUAGAUGGAAUUUUAA',
              'AAAUUUUUUUUU',
              'UAGAUGGAAUUUGAAUUUGAAUUUGAAUUUGAAUUUGAAUUUUAAUAGAUGGAAUUUUAA',
              'AUGGGGUACUACUAUAGGUAG',
              'UAGAUGGAAUUUUAA',
              'UAGAUGGAAUUUUAA']

for i, data in enumerate(secuencias):
    tupleData = deteccion(data)
    if (not tupleData[0]) and (not tupleData[1]):
        print(f'No hay gen en secuencia {i+1}')
    else:
        print(f'Hay {tupleData[1][0]} codones en secuencia {i+1}')
        validSecuencias.append(tupleData[0][0])

print('\n\n')
dictSave(validSecuencias)
# print(validSecuencias)