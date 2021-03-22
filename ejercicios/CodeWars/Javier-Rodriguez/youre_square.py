# You're a square!
# https://www.codewars.com/kata/54c27a33fb7da0db0100040e
# Javier Rodriguez

# Version 1
def is_square(n):
    res = 0 # Sumatoria
    k = 1 # Referencia inicial de sumatoria
    
    if (n < 0): # En el caso de que sea negativo
        return False
    
    while (res < n): # Sumatoria
        res += 2*k - 1
        k += 1
        
    if n == res: # Si resultado de sumatoria es igual al valor de entrada...
        return True
    return False