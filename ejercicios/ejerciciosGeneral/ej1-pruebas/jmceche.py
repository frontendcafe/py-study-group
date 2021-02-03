def palindromo(str):
    new_str = "".join(str.split(" ")).lower()
    if new_str == new_str[::-1]: # cadena[inicio:fin:paso]
        return True
    return False
    
print(palindromo('Anita lava la tina'))
print(palindromo('Sometamos o matemos'))
print(palindromo('Super palindromo'))