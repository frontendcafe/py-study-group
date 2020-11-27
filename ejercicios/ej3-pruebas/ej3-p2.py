def justficador (linea):
    if len(linea) > 30:
        while len(linea) > 30:
            linea += ' '
        linea += '\n'
    elif len(line) == 30:
        linea += '\n'
    else:
        linea[30] += '\n'
        justificador(linea)
    print(linea)

justficador("Esta es una cadena de texto de ejemplo de unos 60 caracteres")

# justficador("Cadenita de tan sólo 32 símbolos")
# justficador('hola')
#justficador('Cadena de tan sólo 30 símbolos')