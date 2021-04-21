def two_sum(numbers, target):
    # start coding!
    encontrado = False
    i = 0
    j = 1
    longitud = len(numbers)
    tuple = [-1, -1]

    while(not encontrado and i < longitud):
        while(not encontrado and j < longitud):
            acum = numbers[i] + numbers[j]
            if(acum == target):
                encontrado = True
                tuple = [i, j]
            j = j + 1
        i = i + 1
        j = 0
    return tuple
