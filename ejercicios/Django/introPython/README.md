# Introducción a Python 🐍

Link original: [Django / Introducción a Python](https://www.notion.so/javonotion/Introducci-n-a-Python-6bc469a4d92241929606ee82264d4235)

## Ejercicios 🏃‍♀️ 
**1)** Vamos a crear una calculadora. Para eso vamos a tener que definir funciones que resuelvan las operaciones básicas (suma, resta, multiplicación y división).  Hacelo todo en un mismo archivo!

Ejemplo de uso:

```py
a = 20
b = 0

print(suma(a, b))
print(resta(a, b))
print(multiplicacion(a, b))
print(division(a, b)) # Ojo acá!
```

---

**2)** Queremos mejorar el ejercicio anterior. Creá una clase `Calculadora` y meté adentro las funciones creadas para que se conviertan en métodos. Hacelo todo en un mismo archivo!

Ejemplo de uso:

```py
a = 20
b = 0

calc = Calculadora()

print(calc.suma(a, b))
print(calc.resta(a, b))
print(calc.multiplicacion(a, b))
print(calc.division(a, b)) # Ojo acá!
```

---

**3)** Queremos mejorar aún más el ejercicio anterior. Vamos a modularizar la clase `Calculadora` y vamos a importarla (esto requiere que crees un nuevo archivo .py con la clase dentro). Te debería quedar algo así el ejercicio

```md
./main.py
./modules/calculadora.py
```

Comprobá que funcione igual que en el ejercicio anterior.

Te animás a crear otra clase, llamada `CalculadoraPro`? Debe heredar los métodos de `Calculadora` y debería tener más funciones matemáticas (logaritmos, porcentaje, raíz, potencia, etc). La cantidad de funciones a implementar la dejamos a libre albedrío.

---

**4)** Dejando en paz a la calculadora, vamos a manipular datos. Tenemos la siguiente función que va a leer un archivo de texto (está en esta carpeta, llamado `the-zen-of-python.txt`)

```py
def read_text(path):
	lines = []
	with open(path) as f:
	    lines = f.readlines()
	return lines

file_dir = 'the-zen-of-python.txt'
lineas = read_text(file_dir)
```

Necesitamos leer lo que procesa esa función. Utilizá un ciclo for para poder leer la lista lineas e imprimirla por pantalla. Debería ser algo así como resultado:

![Resultado 1](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/ef73be2b-ded9-49b3-953e-44ccb4b6bf9d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20210527%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20210527T131754Z&X-Amz-Expires=86400&X-Amz-Signature=77862ffdf3b67e62fa9aea0ef34fd52308ed20939de7c0de85f14269fcd6aa6a&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22)

**Plus**: Te animás a laburar un poco más? Fijate que si lees la lista tal cual como la recibís de la función `read_text`, vas a ver algo así:

![Resultado 2](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/a01bb546-7fa2-4e83-8980-deae0eddc4fe/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20210527%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20210527T131809Z&X-Amz-Expires=86400&X-Amz-Signature=fb0aa85c139b55de40ea7fa5f4ef18c5c67ee9258b7b7b4683504ab50c58712e&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22)

Los `\n` que se ven ahí crean un salto de línea innecesario (es el espacio que hay entre líneas del resultado anterior). Buscá un método para poder eliminar esos `\n`. 
Ojo con el último elemento de la lista!