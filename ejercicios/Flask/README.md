# Contenido
Mostraremos las consignas para cada semana en este README. Cualquier consulta, haganla en el canal del grupo en [FrontendCafé](https://discord.gg/frontendcafe).

## ./semana2
En la segunda semana, ya sabiendo una base de HTML y CSS, ya podemos arrancar con la parte divertida (*wiii*). Lo dividimos en 2 partes:

1) **API GitHub**
Debemos realizar peticiones a la API de GitHub y obtener información de usuarios de la plataforma. Este ejercicio pide:
- Realizar una petición a la API, sabiendo el usuario de GitHub. Por ejemplo: `https://api.github.com/users/JaviCeRodriguez`.
- Obtener los datos de interés como el nombre, usuario, ubicación, biografía, cantidad de repositorios, usuario de twitter, etc.
- Imprimir estos datos de interés en consola con el siguiente formato:
```cmd
Usuario: JaviCeRodriguez
Nombre: Javier Rodriguez
Ubicación: San Fernando, Buenos Aires, Argentina
Biografía: Hago Testing Manual, Desarrollo Frontend y buenos mates.
Twitter: javicerodriguez
.
.
.
```
Probar con varios usuarios existentes y con un par que no existan, para ver que datos recibimos.
Este ejercicio guardalo, lo vamos a usar en Flask.

2) **Primera app en Flask**
Siguiendo el material de estudio recomendado, ya pueden realizar una app en Flask. En este segundo ejercicio se piede:
- Desarrollar en un script `main.py` las funciones necesarias para poder visualizar el contenido buscado, colocando dos posibles rutas:
    - `/` será la página principal, con solo el buscador, título, header y footer.
    - `/error` solo si recibimos un 404. Acá pueden mostrar el cuadro de búsqueda o un botón para volver atrás.
    - `/user/JaviCeRodriguez` si obtenemos datos de la API
- Usar un lenguaje de plantillas para reutilizar el código HTML.

El ejercicio de la semana pasada lo vamos a usar acá para aplicar un poco de diseño a la app. Si no pudieron terminarlo, avisen por el canal del servidor!

**Material**
- [Curso Flask de Código Facilito (hasta el video 13)](https://codigofacilito.com/cursos/flask)
- [Template Designer Documentation - Jinja](https://jinja.palletsprojects.com/en/2.10.x/templates/)
- [Python requests](https://realpython.com/python-requests/)
- [Enlace de ejemplo de API de GitHub: https://api.github.com/users/JaviCeRodriguez](https://api.github.com/users/JaviCeRodriguez) (solo deberían cambiar el usuario 'JaviCeRodriguez')
- [Extensión de Google Chrome para parsear los JSON de las API: JSON Formatter](https://chrome.google.com/webstore/detail/json-formatter/bcjindcccaagfpapjjmafapmmgkkhgoa)


## ./semana1
Para esta primer semana, haremos un repaso de lo que es **HTML y CSS**. Si queremos ver Flask, debemos tener un mínimo de conocimiento de HTML y saber usar CSS para poder llamar la atención que nuestros proyectos sean más lindos.

El ejercicio es simple, estará orientado a lo que realizaremos en la segunda semana. Básciamente haremos peticiones a la API de GitHub para poder obtener información, pero necesitaremos un entorno agradable para verlo... y acá es donde entra HTML y CSS :D

**Ejercicio**: Crear una página con HTML y CSS, imitando la estética de GitHub para mostrar perfil de usuario (foto, datos, repos, etc). Pueden usar los colores del modo dark o los clásicos.

**Material**:
- https://dev.to/javicerodriguez/ciendiasconcourseit-dia-1-100-890
- https://www.w3schools.com/
- https://www.youtube.com/watch?v=D-h8L5hgW-w
- Cualquier otro video de YT o artículo

> Hice un [video](https://www.youtube.com/watch?v=r6QmrHsW5X0) haciendo un diseño en *Figma* y hecho con HTML y CSS, tal vez les pueda servir o no (*pongan el video en x2 jaj*)

Pueden tomar como ejemplo la [siguiente página](https://javier-rodriguez.vercel.app/proyectos/GitHubAPI/index.html) para que vean como podría ser un posible diseño. Pueden copiarla o hacer otro, usar Tailwind, Bootstrap, lo que les sea más cómodo! Pero si o si, tenemos que tener una estructura y un estilo.
