palabra = 'Anitalavalatina'
espalindromo = 1
contador = 1
for letra in palabra:
    if letra.lower() != palabra[contador*-1].lower():
        espalindromo = 0
    contador+=1

if espalindromo == 0:
    print ("no es")
else:
    print ("si es")
