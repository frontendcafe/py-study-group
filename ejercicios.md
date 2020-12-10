# Ejercicios para la gente de FEC
En este Markdown, iremos poniendo todos los ejercicios que deberán hacer. Si hay dudas, consulten en el canal!

<p align="center">
  <a href="https://discord.gg/frontendcafe" target="_blank">
	<img alt="FrontendCafe" src=".\imgs\channel-discord.jpg">
  </a>
</p>

Se agregarán cierta cantidad de ejercicios, veremos la cantidad con el tiempo. Tomaremos como piloto los primeros ejercicios y evaluaremos como seguimos.

**Te pedimos que, una vez termines los ejercicios semanales, nos mandes tus ejercicios a este [Google Form](https://forms.gle/zy7svSNpUTVE8Rf27). Esto nos sirve para tener una mejor organización.**

## Ejercicios
En el siguiente listado, se agregaran ejercicios en orden cronológico. Los enunciados están los más recientes primero. Fecha de entrega no hay, pero si vamos a estar 1 o 2 días por semana para discutir los ejercicios propuestos y daremos la oportunidad de que los demás participen y muestren sus códigos.
- [**Ejercicio 1**: Palíndromo (9/11/2020)](https://github.com/JaviCeRodriguez/py-study-group/blob/main/ejercicios.md#ejercicio-1-palíndromo-pywombat)
- [**Ejercicio 2**: Secuencia Genética (11/11/2020)](https://github.com/JaviCeRodriguez/py-study-group/blob/main/ejercicios.md#ejercicio-2-secuencia-gen%C3%A9tica-inventado)
- [**Ejercicio 3**: Justificador de Líneas (18/11/2020)](https://github.com/JaviCeRodriguez/py-study-group/blob/main/ejercicios.md#ejercicio-3-justificador-de-líneas-propuesto-amitsna)
- [**Ejercicio 4**: Imprimir Números (26/11/2020)](https://github.com/JaviCeRodriguez/py-study-group/blob/main/ejercicios.md#ejercicio-4-imprimir-números-pywombat)
- [**Ejercicio 5**: Intersección de Conjuntos (26/11/2020)](https://github.com/JaviCeRodriguez/py-study-group/blob/main/ejercicios.md#ejercicio-5-intersección-de-conjuntos-pywombat)
- [**Ejercicio 6**: Operaciones Matemáticas (2/12/2020)](https://github.com/JaviCeRodriguez/py-study-group/blob/main/ejercicios.md#ejercicio-6-operaciones-matemáticas)
- [**Ejercicio 7**: Funciones Matemáticas (2/12/2020)](https://github.com/JaviCeRodriguez/py-study-group/blob/main/ejercicios.md#ejercicio-7-funciones-matemáticas)

---

### Ejercicio 9: Datos y gatitos
Utilizando clases y el módulo `datetime`, crear un diccionario que obtenga datos de salida de gatos de una casa de adopción con el siguiente formato:
```cmd
Gatos: 3
Nombres: Juan, Carlos, Sanchez
Fecha de salida: 28/10/2020
```

Para este ejercicio, se pide:
- Crear un diccionario que obtenga los valores de las claves `Gatos` (int), `Nombres` (list) y `Fecha` (datetime). El largo de la lista Nombres debe ser igual al de Gatos.
- Se debe crear un `plot de barras` (o pueden elegir otro a gusto) para ver la cantidad de gatos que tuvieron adopción en un **día**, en un **mes** y en un **año**. Día, mes y año se especifican en consola.
- Se sugiere crear un archivo `csv` en donde se van a almacenar estos datos y así poder volver a *consultar* los mismo datos utilizados.
- Crear una función `menu` para poder mostrar por consola si se quiere:
  1) Insertar datos nuevos
  2) Consultar datos
  3) Eliminar datos
  4) Crear plot con datos del diccionario (solo si el diccionario no está vacío).

Pueden encarar este ejercicio como les sea más cómodo o como les salga primero! Hay muchas formas de encarar este ejercicio.

> **Sugerencia**:

Para que el código no sea tan largo (y fácil de perderse), pueden armar códigos Python por separado y luego importarlos en uno principal. Un ejemplo puede ser: `csvData.py` (para guardar, eliminar y consultar datos de un archivo csv), `plotData.py` (para generar plot) y `gatitos.py` (como código principal).
Luego deberían importar así:
```py
#gatitos.py

import csvData
import plotData

o

from csvData import nombreClaseCSV
from plotData import plotearClaseGatos
```
Es mejor utilizar la segunda opción, porque solo utilizarían las clases y no todo el código que posiblemente no nos sirva.

---

### Ejercicio 8: Módulos de tiempo (Opcional para practicar)
Utilizando los módulos `datetime` y `time`, se pide:
- Calcular la edad actual de una persona según su fecha de nacimiento (en `dd/MM/yyyy`).
- Crear cuenta regresiva (para fines prácticos, conviene usar tiempos cortos).

Pueden realizar este ejercicio o saltearlo, es solo para familiarizarse con estos módulos antes de empezar el **Ejercicio 9**. El formato de salida en consola se deja a libre albedrío.

---

### Ejercicio 7: Funciones Matemáticas
> Enunciado

Realizar las funciones correspondientes con clases como lo planteado en el ejercicio anterior, para realizar las siguientes operaciones sobre listas de elementos:

- Calcular el promedio.
- Hallar el valor máximo. 
- Hallar el valor mínimo.
- Buscar valores repetidos y mostrarlos por consola.
- Dado un número se debe calcular la sucesión de Fibonacci. En este caso, dicho número representa la cantidad de dígitos que se tienen en cuenta.

> Observaciones

- En caso de que la lista no posea elementos, se debe mostrar una lista vacía.
- Para el caso en que la lista tenga 1 solo elemento, ese elemento se considera el promedio, el valor máximo y el valor mínimo.
- Además si la lista no posee valores repetidos, se debe mostrar un cartel indicando que dicha lista no posee elementos repetidos.
- En caso de que se deba dividir por 0, se debe mostrar la palabra por consola "Error".

> Ejemplos
```cmd
>>> a = [2, 5, 27, 13, -7, 1, 1]
>>> b = [-1, 1]
>>> c = []
>>> d = [10]

Funcion promedio:

>>> operacion = FuncionMatematica() 
>>> operacion.promedio(a)
6

>>> operacion.promedio(b)
"Error" 

>>> operacion.promedio(c)
[]

>>> operacion.promedio(d)
10

Funcion mínimo:

>>> operacion.minimo(a)
-7

>>> operacion.minimo(b)
-1

>>> operacion.minimo(c)
[]

>>> operacion.minimo(d)
10

Funcion máximo:

>>> operacion.maximo(a)
27

>>> operacion.maximo(b)
1

>>> operacion.maximo(c)
[]

>>> operacion.maximo(d)
10

Funcion repetido:

>>> operacion.repetido(a)
1

>>> operacion.repetido(b)
No posee elementos repetidos

>>> operacion.repetido(c)
No posee elementos repetidos

>>> operacion.repetido(d)
No posee elementos repetidos

Funcion Fibonacci:

>>> num = 8
>>> operacion.fibonacci(num)
13
Esto se debe a que cuenta: 
0 + 1 + 1 + 2 + 3 + 5 + 8 + 13
```

Para conocer sobre Fibonacci pueden seguir el siguiente link a [Wikipedia - Sucesión de Fibonacci](https://es.wikipedia.org/wiki/Sucesi%C3%B3n_de_Fibonacci).

---

### Ejercicio 6: Operaciones Matemáticas
> Enunciado

Desarrollar una clase llamada "OperacionMatematica" que contenga una función, por cada una de las operaciones matemáticas habituales descriptas a continuación: 
  - Suma.
  - Resta.
  - Multiplicación.
  - División.
  - Potenciación.
  - Radicación.

> Ejemplos
```cmd
>>> operacion = OperacionMatematica() 
>>> operacion.suma(2,3)
5
>>> operacion.resta(5,12)
-7
>>> operacion.multiplicacion(-3,-6)
18
>>> operacion.division(1,2)
0.5
>>> operacion.potenciacion(2,8)
256
>>> operacion.radicacion(36)
6
```
> Observación: En los ejemplos de arriba, se ha creado un objeto de tipo Operaciones_matematicas, para luego operar con las funciones (o métodos llámense) de nuestra clase, las cuales muestran por consola el resultado, es decir, hacen un "print(resultado)". Pueden hacerlo de ésta forma, o retornar el valor.


> Requerimientos

- Para los ejercicios se deben utilizar clases y, como buena práctica de programación se deben modularizar los problemas. Es decir, tendrán una clase llamada "OperacionMatematica" (es importante que comience en mayúscula el nombre de la clase), y dentro de la misma tendrán una función por cada operación matemática. De esa forma se dividen los problemas en partes pequeñas de código.

- Se debe utilizar documentación (docstrings) tanto para la clase como para cada función.

Para conocer sobre las clases en Python pueden seguir el siguiente link a [W3Schools](https://www.w3schools.com/python/python_classes.asp).

---

### Ejercicio 5: Intersección de Conjuntos (PyWombat)
> Enunciado

Desarrollar una función que recibe dos listas a y b que contienen números enteros,

la lista a cuenta con una cantidad de elementos menor que b (a < b),

luego las compara entre sí y retorna una única lista con todos los números enteros presentes en ambas listas.

Los elementos de la lista retornada deben estar ordenados de menor a mayor y sólo deben estar listados una única vez.

En caso de no tener elementos en común ambas listas, debe retornar una lista vacía.

> Ejemplos
```cmd
>>> interseccion([1, 2, 3, 4, 5, 6, 7, 8], [10, 25, 52, 80, 1, 46, 6, 33, 14, 27, 19])
[1, 6]
>>> interseccion([1, 1, 1], [2, 2, 2])
[]
>>> interseccion([3, 2, 1], [4, 3, 2, 1])
[1, 2, 3]
>>> interseccion([1, 2, 3, 4, 5], [0, 2, 4, 6, 8, 10])
[2, 4]
>>> interseccion([6, 7, 1, 2, 1, 3, 4, 5], [7, 8, 1, 3, 2, 1, 7, 3, 7, 10])
[1, 2, 3, 7]
```


### Ejercicio 4: Imprimir Números (PyWombat)
> Enunciado

Desarrollar una función que reciba por input una lista de números enteros separados por coma,

y retorne cada uno de los números impresos en saltos de líneas separados.

> Ejemplos
```cmd
>>> print_numeros([1, 2, 3, 4, 5])
1
2
3
4
5
>>> print_numeros([1, 1, 1])
1
1
1
>>> print_numeros([3, 2, 1])
3
2
1
>>> print_numeros([10, 20, 30, 14, 14, 16, 20])
10
20
30
14
14
16
20
```


### Ejercicio 3: Justificador de Líneas (propuesto AmitSna)
> Enunciado

Desarrollar una función que, al recibir una cadena de texto la formatea para que siempre contenga un máximo de 30 caracteres y la finaliza con un salto de línea.

En caso de tener menos de 30 caracteres, le completa con espacios en blanco por la derecha hasta completar los 30 y luego la finaliza con salto de línea.

En caso de tener 30 caracteres exactos, le añade un salto de línea.

En caso de tener más de 30 caracteres, la fracciona en distintas cadenas de máximo 30 y les realiza mismas operatorias.

El retorno debe ser una cadena de texto justificada según la consigna.

> Ejemplos
```cmd
>>> justificador("Esta es una cadena de texto de ejemplo de unos 60 caracteres")
"Esta es una cadena de texto de\n ejemplo de unos 60 caracteres\n"
>>> justificador("Cadenita de tan sólo 32 símbolos")
"Cadenita de tan sólo 32 símbol\nos                              \n"
>>> justificador("hola")
"hola                              \n"
>>> justificador("¡stringsstringsstringsstrings!")
"¡stringsstringsstringsstrings!\n"
```

### Ejercicio 2: Secuencia Genética (Inventado)
> Nota aclaratoria

Este ejercicio es uno de tantos que vamos a meter para tocar varias áreas en donde se utiliza Python. Acá lo vamos a encarar para que puedan hacerlo desde cero, pero sepan que existen librerías (por ejemplo: [Biopython](https://biopython.org/)) que hacen esto y mucho más de manera más sencilla.

> Mini teoría

Para no meternos en tanta teoría, lo resumo así (para el interesado, googleenlo): Todos los "seres vivos" contienen material genético en el cual nos identifica como tal: Humanos, Monos, Pythons (*ba dum tss*), etc. Este material genético tiene al conocido **ADN** (Ácido desoxirribunicléico) con sus respectivos nucleótidos, que son la **Adenina, Citosina, Guanina y Timina** (simplificados en A, C, G y T, respectivamente). Estos mismos, ayudan al organismo en la producción de biomoléculas a partir de grupos de **codones** (grupos de 3 nucleótidos).

Una *secuencia* de ejemplo sería:
**AUG** CCA GAC AAC **UAA**

*Observación*: hay una U, que corresponde al **Uracilo** y aparece en el **ARN** (Ácido ribunucléico). Este nucleótido reemplaza a la Timina (para más detalles, le preguntan a Javo).

Hay una tabla para poder identificar cada codón:
<p align="center">
  <a href="https://discord.gg/frontendcafe" target="_blank">
	<img alt="FrontendCafe" src=".\imgs\codigo-genetico.jpg" style="width: 300px">
  </a>
</p>

Una cosa para destacar es que **las secuencias de ARN empiezan con el codón AUG, y terminan con el codón UAA, UAG o UGA**. No importa que tan largo sea, es una de las condiciones de las secuencias para producir "algo" en el organismo.

> Enunciado

Una vez entendida la teoría (si no, consulten), vamos a desarrollar un detector de secuencias de ARN que contiene una cadena de varios A, U, C, G, sin importar el largo que tenga. Si existe una secuencia, debe avisar por consola e indicar cuantas. De lo contrario, avisar que no hay secuencia.

> Requerimientos

- Simplemente, detectar la secuencia como indica el enunciado. Deben asegurarse de poder detectar primero un codón AUG y (si o sí) un codón UAA, UAG o UGA al final.
- Para que sea secuencia genética, debe al menos existir 1 codón, junto con el AUG al inicio y el UAA, UAG o UGA al final.
- Opcional 1: Mostrar por consola las secuencias detectadas
- Opcional 2: Indicar cuantos codones contiene cada secuencia
- Opcional 3: Emplear un diccionario para guardar todas las secuencias
- Opcional 4: Guardar las secuencias en un documento de texto, excel o como prefieran.

Los opcionales están para que veamos que saben y como lo encaran. Estaría bueno que hagan todos o algunos opcionales para que aprendan otras cositas de Python, a parte de la lógica.

> Ejemplos
```cmd
Inserte secuencia: AUGGGGUACUACUAUAGGUAG
Secuencias detectadas: 1

Inserte secuencia: AUGGGGUaUxAXUA-AGGUaG
Secuencias detectadas: 0

Inserte secuencia: AUGGGGUAUUAUUAUAGGUAGAUGGGGUAUUAUUAUAGGUAGAUGGGGUAUUAUUAUAGGUAG
Secuencias detectadas: 3
```
*NOTA*: No es obligatorio ingresar las secuencias, pueden generarlas de forma automática con random! (aunque las posibilidades de obtener una secuencia son bajas dependiendo del largo de la cadena).

---
### Ejercicio 1: Palíndromo ([PyWombat](https://pywombat.com/)):
> Enunciado

Definir una función la cual permita conocer si un string es un *palíndromo* o no.

Un palíndromo es una palabra, o frase, que se lee igual de izquierda a derecha que de derecha a izquierda
> Requerimientos

- La función debe tener por nombre palíndromo.
- La función debe poseer como parámetro la variable sentencia.
- La función debe retornar verdadero(True) si el parámetro es una palíndromo, en caso contrario retornará falso(False).
> Ejemplos

```cmd
>>> palindromo('Anita lava la tina')
True
>>> palindromo('Sometamos o matemos')
True
>>> palindromo('Super palindromo')
False
```
