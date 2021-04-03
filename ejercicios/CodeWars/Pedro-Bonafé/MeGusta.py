#El programa debe ser una funcion que una función como :: [String] -> String, 
#que debe incluir una matriz de entrada, que contiene los nombres de las personas a las que les gusta un elemento.
#Debe devolver el texto de la pantalla como se muestra en los ejemplos:
# likes([]) # must be "no one likes this"
#likes(["Peter"]) # must be "Peter likes this"
#likes(["Jacob", "Alex"]) # must be "Jacob and Alex like this"
#likes(["Max", "John", "Mark"]) # must be "Max, John and Mark like this"
#likes(["Alex", "Jacob", "Mark", "Max"]) # must be "Alex, Jacob and 2 others like this"

#Nota para 4 o mas nombres debe decir los primeros dos nombres 'and 2 others like this'


def likes(names):
    if names == []:
        return 'no one likes this'
    elif len(names) == 1:
        return f'{names[0]} likes this'
    elif len(names)==2:
        return f'{names[0]} and {names[1]} like this'
    elif len(names) == 3:
        return f'{names[0]}, {names[1]} and {names[2]} like this'
    if len(names)>= 4:
        a = len(names) - 2
        return f'{names[0]}, {names[1]} and {a} others like this' 
