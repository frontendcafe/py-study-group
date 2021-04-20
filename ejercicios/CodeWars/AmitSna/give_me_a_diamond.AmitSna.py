def diamond(n):
    if n < 1 or n%2==0:
        return None
    diamond = ""
    for amount in range(1, n + 1, 2):
        diamond += " " * ((n - amount) // 2) + "*" * amount + "\n"
    for amount in range(n - 2, 0, -2):
        diamond += " " * ((n - amount) // 2) + "*" * amount + "\n"
    return diamond
