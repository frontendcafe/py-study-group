class OperacionMatematica:

    def promedio(self, lista):
        if len(lista) > 0:
            return sum(lista) / len(lista)
        else:
            return lista

    def minimo(self, lista):
        if len(lista) > 0:
            min = lista[0]

            for num in lista[1:]:
                if num < min:
                    min = num

            return min
        else:
            return lista

    def maximo(self, lista):
        if len(lista) > 0:
            max = lista[0]

            for num in lista[1:]:
                if num > max:
                    max = num

            return max
        else:
            return lista

    def repetido(self, lista):
        dups = set([x for x in lista if lista.count(x) > 1])

        if len(dups) > 0:
            return dups
        else:
            return 'No hay elementos duplicados'

    def fibonacci(self, nums):
        a_1 = 0
        a_2 = 1
        fibo = a_1 + a_2

        for i in range(nums-2):
            fibo = a_1 + a_2
            a_1 = a_2
            a_2 = fibo

        return fibo

def main():
    operacion = OperacionMatematica()

    a = [2, 5, 27, 13, -7, 1, 1]
    b = [-1, 1]
    c = []
    d = [10]

    print('PROMEDIOS')
    print('a:', operacion.promedio(a))
    # 6
    print('b:', operacion.promedio(b))
    # 0
    print('c:', operacion.promedio(c))
    # []
    print('d:', operacion.promedio(d))
    # 10

    print()

    print('MÍNIMOS')
    print('a:', operacion.minimo(a))
    # -7
    print('b:', operacion.minimo(b))
    # -1
    print('c:', operacion.minimo(c))
    # []
    print('d:', operacion.minimo(d))
    # 10

    print()

    print('MÁXIMOS')
    print('a:', operacion.maximo(a))
    # 27
    print('b:', operacion.maximo(b))
    # 1
    print('c:', operacion.maximo(c))
    # []
    print('d:', operacion.maximo(d))
    # 10

    print()

    print('REPETIDOS')
    print('a:', operacion.repetido(a))
    # 1
    print('b:', operacion.repetido(b))
    # No posee elementos duplicados
    print('c:', operacion.repetido(c))
    # No posee elementos duplicados
    print('d:', operacion.repetido(d))
    # No posee elementos duplicados

    print()

    print('FIBONACCI')
    print(operacion.fibonacci(8))
    # 13

main()