import modules

if __name__ == "__main__": # No es necesaria esta linea, en este caso
    a = 20
    b = 0
    calc = modules.Calculadora(a, b)

    print(calc.suma())
    print(calc.resta())
    print(calc.producto())
    print(calc.division()) # Ojo acá!