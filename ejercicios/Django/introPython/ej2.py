class Calculadora:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def suma(self):
        '''
        Realiza la suma de dos números
        '''
        return self.x + self.y

    def resta(self):
        '''
        Realiza la resta de dos números
        '''
        return self.x - self.y

    def producto(self):
        '''
        Realiza el producto de dos números
        '''
        return self.x * self.y

    def division(self):
        '''
        Realiza la divisón de dos números\n
        Devuelve "Inf" si "y" es 0
        '''
        if self.y == 0:
            return 'Inf'
        else:
            return self.x / self.y


a = 20
b = 0
calc = Calculadora(a, b)

print(calc.suma())
print(calc.resta())
print(calc.producto())
print(calc.division()) # Ojo acá!