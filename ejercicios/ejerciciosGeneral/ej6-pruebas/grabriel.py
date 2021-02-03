# Importar librería math
import math


class OperacionMatematica():
    # Clase que se compone de funciones que resuelven operaciones matemáticas

    def suma(self, a, b):
        # Función que recibe dos números por parámetro y retorna el resultado de sumarlos
        return a+b

    def resta(self, a, b):
        # Función que recibe dos números por parámetro y retorna el resultado de restarlos
        return a-b

    def multiplicacion(self, a, b):
        # Función que recibe dos números por parámetro y retorna el resultado de multiplicarlos
        return a*b

    def division(self, a, b):
        # Función que recibe dos números por parámetro y retorna el resultado de dividirlos
        return a/b

    def potenciacion(self, a, b):
        # Función que recibe dos números por parámetro y retorna el resultado de elevar un número sobre otro
        return int(math.pow(a, b))

    def radicacion(self, a):
        # Función que recibe un número por parámetro y calcula su raíz
        return math.sqrt(a)


# Creación de un objeto de tipo OperacionMatematica
operacion = OperacionMatematica()

print("Suma 2+3 =", operacion.suma(2, 3))

print("Resta 5-12 =", operacion.resta(5, 12))

print("Multiplica -3*(-6) =", operacion.multiplicacion(-3, -6))

print("Divide 1/2 =", operacion.division(1, 2))

print("Potenciacion 2^8 =", operacion.potenciacion(2, 8))

print("Radicacion de 36 =", operacion.radicacion(36))