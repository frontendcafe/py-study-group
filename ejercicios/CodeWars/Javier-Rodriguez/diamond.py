def diamond(n):
    if (n % 2 == 0 or n < 1):
        return None
    
    if (n == 1):
        return "*\n"
    
    dArr = [' ' * ((n - i) // 2) + ('*' * i) + '\n' for i in range(n+1) if (i % 2 != 0)]
    salida = ''

    for d in (dArr + dArr[-2::-1]):
        salida += d

    return salida

print (diamond(5))