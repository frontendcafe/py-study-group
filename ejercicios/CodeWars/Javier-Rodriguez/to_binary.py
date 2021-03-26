def to_binary(n):
    resu = ''
    while n >= 1:
        resu = str(n % 2) + resu
        n //= 2
    return int(resu)

to_binary(10)