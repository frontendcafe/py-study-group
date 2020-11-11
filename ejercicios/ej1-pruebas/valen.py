# función que permite conocer si un string es un palíndromo o no
def palindromo(sentencia):
    try:
        joined_string = sentencia.replace(" ", "")
        lower_case_string = joined_string.lower()
        reverse_string = lower_case_string[::-1]
        if lower_case_string == reverse_string:
            return True
        else:
            return False
    except AttributeError:
        print("Ingrese una palabra u oracion")

print(palindromo('Neuquen'))