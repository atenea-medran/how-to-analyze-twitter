# Important Links
* **[Converting twarc2 json to csv](Twarc2%20twitter%20scraper/Convert%20twarc2%20json%20to%20csv.ipynb)**
* **[Hashtag analysis with Python retrieved with Twarc2](Twarc2%20twitter%20scraper/Hashtag%20Analysis%20With%20Python/0.%20Hashtag%20analysis%20with%20Python.ipynb)**
* **[Retweets graph](Twarc2%20twitter%20scraper/Retweets%20graph/Grafo%20de%20retweets.ipynb)**
* **[Hashtags grah](Twarc2%20twitter%20scraper/Hashtags%20graph/Hashtags%20graph.ipynb)**
* **[User->hashtag graph](Twarc2%20twitter%20scraper/User%20to%20hashtag%20graph/User%20to%20hashtag%20graph.ipynb)**
* **[Downloading Twitter images](Twarc2%20twitter%20scraper/Download%20Twitter%20Images/Downloading%20Twitter%20images.ipynb)**
* **[Automating screenshots keeping logged in and cookies](Twarc2%20twitter%20scraper/Download%20Twitter%20Images/Screenshots)**
* **[Counting images](Twarc2%20twitter%20scraper/Download%20Twitter%20Images/Counting%20images.ipynb)**
* **[Counting 8 digits Twitter accounts and checking creation date](Twarc2%20twitter%20scraper/Counting%208%20digits%20Twitter%20accounts)**


# Cómo analizar datos de Twitter
Vamos a ver cómo se pueden analizar los datos de Twitter obteniéndolos con dos programas: **[t-hoarder](https://github.com/congosto/t-hoarder_kit)** y **[twarc2](https://twarc-project.readthedocs.io/en/latest/twarc2_en_us/)**. Quiero expresar mi máximo agradecimiento a **[Mari Luz Congosto](https://github.com/congosto)** por crear t-hoarder y a Jara Juana Bermejo Vega (**@queenofquanta** en redes) y **[Pynomaly](https://github.com/pynomaly)** por su apoyo y guía. También quiero dar las gracias al Vicerrectorado de Igualdad, Inclusión y Sostenibilidad de la Universidad de Granada por haber hecho este aprendizaje posible.

He grabado todo el proceso de instalación y análisis en este vídeo por si alguna parte no queda clara:
* **[Cómo analizar datos de Twitter con t-hoarder, Gephi y Python (Youtube)](https://www.youtube.com/watch?v=Fb5ZsmasuVw)**

Falta la parte de pedir el acceso elevado por temas de privacidad, aunque está explicado. El vídeo está dividido en capítulos para navegarlo más fácilmente.

## Pedir acceso a la API de Twitter
### Acceso esencial
Lo primero de todo es solicitar acceso esencial a la API de Twitter. Esto es suficiente para poder trabajar con twarc2, aunque vamos a priorizar t-hoarder porque tiene una opción muy útil que twarc2 no tiene. Lo hacemos con el siguiente enlace:
* **[Pedir acceso esencial](https://developer.twitter.com/en/portal/petition/essential/basic-info)**

El proceso es muy sencillo, tenemos que decir qué uso le vamos a dar a la API y aceptar los términos y condiciones. Por último creamos una app y guardamos sus claves en un archivo de texto. Es muy importante guardar las claves porque twarc2 nos las pedirá más adelante. Si las perdemos se pueden regenerar fácilmente.

### Acceso elevado
Para poder usar t-hoarder necesitamos acceso elevado o académico. Este programa usa la API v1.1, que solo se puede acceder mediante esos dos tipos de acceso. El acceso esencial solo nos permite usar la API v2, que es con la que trabaja twarc2. Para obtener el acceso elevado o académico (mayores requisitos) usamos este enlace:

* **[Pedir acceso elevado](https://developer.twitter.com/en/portal/petition/standard/basic-info)**

Una vez tengamos el acceso elevado tenemos que crear una app de la API v1.1 de Twitter. En el menú de la izquierda nos vamos a "Overview" y abajo a "Standalone Apps" y creamos una. Ej: "prueba_ate". Si lo hacemos en el proyecto principal usará la API v2 y no nos servirá para t-hoarder. Por último guardamos todas las keys y tokens en un archivo de texto.

* **[Información detallada sobre los tipos de acceso](https://developer.twitter.com/en/docs/twitter-api/getting-started/about-twitter-api)**
### Resumen tipos de acceso
- Esencial: hasta 500.000 tweets mensuales. Tweets con antigüedad de 6 días. API v2 - twarc2

- Elevado: hasta 2 millones de tweets mensuales. Tweets con antigüedad de 6 días. API v1.1 y API v2 - twarc2 y t-hoarder

- Académico: hasta 10 millones de tweets mensuales. Sin límite de antigüedad. API v1.1 y API v2 - twarc2 y t-hoarder

## t-hoarder
Por lo fácil que es recomiendo usar t-hoarder con esta máquina virtual Linux donde viene ya instalado:
* **[Tutorial para instalar máquina virtual](https://www.dropbox.com/s/j0p26bmgmct3vll/como_instalar_VM_taller_datos_twitter.pdf?dl=0)**<br />
Dentro del Linux de la máquina virtual podemos ir a "Menu" -> "Pantallas" y clicamos en "Resolución". Con mi pantalla de 1920x1080 me funciona bien 1600x900 en la máquina virtual.

### Configurar t-hoarder
Una vez que tengamos la máquina virtual instalada y una app que funcione con la API v1.1 podemos pasar a la configuración de t-hoarder. Para ello tenemos que enlazar el programa con la app dentro de la máquina virtual. 

  1. Vamos a "/Carpeta personal de tallerdatos" -> "/t-hoarder kit" -> "/keys" y creamos un archivo de texto, preferentemente con el mismo nombre de la app que hemos creado antes. Ej: "prueba_ate.key".<br />
  2. En la primera línea pegamos la "public key", le damos a  intro y en la segunda línea pegamos la "private key". Estas las habíamos guardado en un archivo de texto. También se puede copiar y pegar el archivo, pero es mejor crearlo en Linux. Guardamos y cerramos.<br />
  3. Vamos una carpeta hacia atrás, entramos en la carpeta "/Store" y creamos una carpeta vacía con el nombre que queramos, que será el de nuestro experimento/proyecto.<br />
  4. En el escritorio abrimos t-hoarder e introducimos el nombre del archivo donde hemos guardado las keys, un nombre de usuario de Twitter y el nombre de la carpeta experimento/proyecto. Con esto podremos acceder al menú de t-hoarder.<br />
  5. Dentro de la máquina virtual entramos en Mozilla Firefox y abrimos nuestra cuenta de Twitter.<br />
  6. Volvemos a t-hoarder, tecleamos "1" (Get an user token access) y le damos a intro para crear las keys de nuestra cuenta de Twitter, que son diferentes de las de "prueba_ate.key", esas son de la app. Se abrirá Firefox y aceptamos que la app pueda acceder a nuestra cuenta de Twitter<br />
  7. Copiamos el código que aparece y lo pegamos en t-hoarder.

### Usar t-hoarder
Ya podemos usarlo. Elegimos una opción y seguimos las instrucciones. Las opciones que yo uso más son:
* 3 make a query on Twitter. Para buscar tweets que contengan una palabra o un hashtag y guardarlos en un archivo .txt. Ej: "#felizjueves".
* 8 remove-duplicate-tweets. Para limpiar el archivo. Se puede hacer con otro lenguaje de programación.
* 8 sort. Para ordenar de más antiguo a más reciente (el archivo se genera al revés). Se puede hacer con otro lenguaje también.
* 6 generate dynamic relations - RT. Para obtener el archivo .gdf que nos permite generar el grafo de RTs.
* 7 entities. Para obtener diversas métricas como los hashtags secundarios, las menciones, los tweets por día, las apps usadas...
* 6 generate static relations - following-followers. Para obtener un archivo .gdf que nos permite generar un grafo de seguidores y seguidos. Es una relación con más peso que la de los retweets. La desventaja es que tarda muchas horas.
* El resto se explican aquí: **[t-hoarder WIKI](https://github.com/congosto/t-hoarder_kit/wiki/)**

## Gephi
Gephi es un programa de código abierto para representar grafos. Con él podemos abrir los archivos .gdf que obtenemos con la opción 6 de t-hoarder. Aquí hay un tutorial básico de como manipular grafos:
* **[Tutorial Gephi](http://periodisme-dades.recursos.uoc.edu/es/6-1-4-preguntas-a-resolver/)** (sobre la mitad de la página).
Gephi es clave porque nos permite separar las cuentas en comunidades. Mientras más relaciones hay entre un grupo de nodos más se atraen, con lo que se terminan formando nubes, que serán las comunidades. Luego esos datos se pueden exportar y juntarlos con el archivo del hashtag obtenido con t-hoarder. Con Python se podrá filtrar por comunidad y así podemos separar los tweets, por ejemplo entre gente a favor y en contra de un tema. Los detalles de este proceso se pueden ver en el **[Notebook](t-hoarder%20twitter%20scraper/0.%20Analisis%20de%20FelizMartes%20con%20Python.ipynb)** y en el **[vídeo de youtube](https://www.youtube.com/watch?v=Fb5ZsmasuVw)**.

## Análisis de datos
En mi caso me he decantado por Python, aunque se podrían utilizar otros lenguajes como R, por ejemplo. En este repositorio he dejado un **[Notebook](t-hoarder%20twitter%20scraper/0.%20Analisis%20de%20FelizMartes%20con%20Python.ipynb)** con el análisis que he hecho hasta ahora, aunque se podrían hacer muchas más cosas. En el **[vídeo de youtube](https://www.youtube.com/watch?v=Fb5ZsmasuVw)** muestro como adaptar el Notebook según el archivo de tweets guardado y también cambió algunos parámetros que dependen de los datos, como las coordenadas de los gráficos hechos con Matplotlib.

He elegido Visual Studio Code para escribir el código.
* **[Descarga de Visual Studio Code](https://code.visualstudio.com/download)**

También habría que instalar Python (aunque esté diponible la 3.11 he descargado la 3.10.8 para evitar un error en Visual Studio Code) y las librerías usadas al principio del notebook. Pip viene con python, pero si no viniera también habría que instalarlo.
* **[Descargar Python](https://www.python.org/downloads/)**
* **[Cómo instalar librerías (Ejemplo pandas)](https://pandas.pydata.org/docs/getting_started/install.html#installing-from-pypi)**
* **[Pip](https://stackoverflow.com/questions/4750806/how-do-i-install-pip-on-windows)**

Y ya con todo esto podríamos obtener tweets con cualquier búsqueda y analizarlos a nuestro gusto.

## Crear un grafo de hashtags

Un aspecto muy interesante de Twitter son las relaciones que se forman entre hashtags. Esto se puede averiguar analizando los hashtags que conviven en un tweet, y si de un hashtag recolectamos miles de tweets podremos obtener un grafo bastante completo.<br />
Vamos a la carpeta **[Grafo de hashtags](Twarc2%20twitter%20scraper/Hashtags%20graph)**. En esta tenemos un **[Notebook](Twarc2%20twitter%20scraper/Hashtags%20graph/Hashtags%20graph.ipynb)**. Simplemente tenemos que modificar el nombre de archivo .txt que pandas abrirá y poner el nuestro. Le damos a `Ejecutar todo` y respondemos a las preguntas que nos surgirán. Como alternativa, dentro de **[Script directo](Grafo%20de%20hashtags/Script%20directo)** tendremos un archivo .py que hace lo mismo por consola. Para ejecutarlo en el ordenador tenemos que abrir una terminal en la carpeta donde este el script y escribir `python .\crear_grafo_de_hashtags.py`. Elegimos el archivo con Intro y respondemos a las preguntas. Ambas opciones nos generarán un archivo .gdf que podemos abrir con Gephi. Vuelvo a enlazar el tutorial:
* **[Tutorial Gephi](http://periodisme-dades.recursos.uoc.edu/es/6-1-4-preguntas-a-resolver/)** (sobre la mitad de la página).

Pueden contactarme con cualquier duda en **[Twitter](https://twitter.com/Estrohacker_)** y en el correo electrónico: **estrohacker@protonmail.com**.

Muchas gracias.
