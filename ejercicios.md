# Ejercicios para la gente de FEC
En este Markdown, iremos poniendo todos los ejercicios que deberán hacer. Si hay dudas, consulten en el canal!

<p align="center">
  <a href="https://discord.gg/frontendcafe" target="_blank">
	<img alt="FrontendCafe" src=".\imgs\channel-discord.jpg">
  </a>
</p>

Se agregarán cierta cantidad de ejercicios, veremos la cantidad con el tiempo. Tomaremos como piloto los primeros ejercicios y evaluaremos como seguimos.

## Ejercicios
En el siguiente listado, se agregaran ejercicios en orden cronológico. Los enunciados están los más recientes primero. Fecha de entrega no hay, pero si vamos a estar 1 o 2 días por semana para discutir los ejercicios propuestos y daremos la oportunidad de que los demás participen y muestren sus códigos.
- [**Ejercicio 1**: Palindromo (9/11/2020)](https://github.com/JaviCeRodriguez/py-study-group/blob/main/ejercicios.md#ejercicio-1-palindromo-pywombat)
- [**Ejercicio 2**: Secuencia genética (10/11/2020)](https://github.com/JaviCeRodriguez/py-study-group/blob/main/ejercicios.md#ejercicio-2-secuencia-gen%C3%A9tica-inventado)

---
### Ejercicio 2: Secuencia genética (Inventado)
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
	<img alt="FrontendCafe" src=".\imgs\codigo-genetico.jpg">
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

---
### Ejercicio 1: Palindromo ([Pywombat](https://pywombat.com/)):
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
