# Persistent Bugger
# https://www.codewars.com/kata/55bf01e5a717a0d57e0000ec
# Javier Rodriguez

# Version 2
def persistence(n):
    resu = 0
    if n < 10:
        return 0
    else:
        while n >= 10:
            aux = 1
            for d in str(n):
                aux *= int(d)
            n = aux
            resu += 1
        return resu

# Version 1
def persistence(n):
    per = 0
    val = str(n)
    while len(val) > 1:
        k = 1
        for num in val:
            k *= int(num)
        val = str(k)
        per += 1
    return per