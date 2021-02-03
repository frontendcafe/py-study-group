class OperacionMatematica:

    def suma(self, num1, num2):
        return num1 + num2

    def resta(self, num1, num2):
        return num1 - num2

    def multiplicacion(self, num1, num2):
        return num1 * num2

    def division(self, num1, num2):
        return num1 / num2

    def potenciacion(self, num1, num2):
        return num1 ** num2

    def radicacion(self, num1, num2):
        return num1 ** (1/num2)

def main():
    operacion = OperacionMatematica()

    print(operacion.suma(1, 2))
    # 3
    print(operacion.resta(10, 8))
    # 2
    print(operacion.multiplicacion(3, 5))
    # 15
    print(operacion.division(20, 4))
    # 5
    print(operacion.potenciacion(2, 4))
    # 16
    print(operacion.radicacion(9, 2))
    # 3

main()