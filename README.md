# Librería de Sistemas determinísticos, probabilísticos y cuánticos
Esta librería consta de funciones que evalúa lo siguiente: 
- Sistema determinístico con valores Booleanos
- Sistema probabilísticos
- Sistema cuántico 
- Experimento de multiples rendijas probabilístico
- Experimento de multiples rendijas cuántico
- Graficar los vectores estados de un sistema
## Comenzando 
En la carpeta del proyecto debes tener dos archivos llamados:
* LibrarySystems.py
* testSystems.py

Es importante que estos archivos se encuentren, ya que uno es la librería con todas las operaciones, y el otro contiene el test que más adelante ejecutaremos
para verificar que la librería funciona adecuadamente.
### Pre-requisitos
Debes tener instalado python y algún entorno de desarrollo interactivo(IDE). El IDE que recomiendo, con el cual fue hecho esta librería, es PyCharm.
### Instalación
1. Para instalar python solo debes ir al sitio web oficial de python.
2. Debes ir a la sección de "Downloads" y descargas la última versión que te recomienda. 
3. Una vez que lo tengas descargado, ejecutas el archivo y le das a instalar.
4. Para Pycharm debes hacer lo mismo, ir al sitio web y buscar la opción "descargar".
5. Ejecutas el archivo y aceptas términos y condiciones y le das en instalar.
6. Al tener descargado python, ejecutas Pycharm y abres la carpeta de la librería de complejos.
7. Verás que en un panel de la derecha de Pycharm tendrás todos los archivos de la carpeta que se usaran.
8. Si abres el archivo LibrarySystems.py podrás ver todas las operaciones que contiene la librería.
### Ejecutar el test
Para poder ejecutar el test debes ir al archivo denominado testSystems.py y abrirlo con ayuda de Pycharm, se ejecuta el código presionando "ctrl + shift + f10".
### Análisis del Test
Con ayuda de la librería numpy y unittest el test consta del siguiente mecanismo:
1. Al ejecutar el test debera aparecer una gráfica, esta corresponde al sistema determinístico, esta simplemente se emplea para corroborar si la función para graficar el vector estado funciona adecuadamente.
2. Después de cerrar la grafica debera aparecer que el test debió haber corrido 5 test, que corresponden a las respectivas funciones, sin contar la de graficar.
3. Si por alguna razón votara Error, esto se debe al mal funcionamiento del código, si por el contrario saliera Failure, significa que algún caso de prueba no dio el resultado esperado, y si da OK, eso es porque el test ejecuto y los casos de prueba pasaron sin ningún inconveniente.
4. Cada función ejecuta un maximo de dos pruebas, estas pruebas son tomadas del ejemplo del libro, y los resultados esperados también son tomados del libro.
### Observaciones
Para las tres primeras funciones, cabe aclarar que están en una misma, es decir la función "sistemaDeterProbaCuan" puede evaluar:

- Sistema determinístico con valores Booleanos
- Sistema probabilísticos
- Sistema cuántico 

Esto es gracias a numpy y a que python puede hacer multiplicaciones entre complejos, aclarar que la de valores boléanos tomamos a 1 como "True" y a 0 como "False", para poder implementar esta función para los tres casos ya mencionados. 

Para la función "multipleRendija", simplemente se pide que el usuario diga la cantidad de rendijas, la cantidad de blancos disponibles por rendija, y la cantidad de clicks que quisiera, con ayuda de esto montamos las probabilidades correspondientes a cada suceso, es decir:

- prob_1 = 1/rendijas
- prob_2 = 1/blancos

La primera corresponde a la probabilidad de ir alguna de las rendijas, mientras que la segunda es de ir a algunos de los blancos despues de cruzar una rendija.
Con esto montamos la matriz y ejecutamos los clicks correspondientes.

En la función "multipleRendijaCuantico" hicimos un pequeño cambio siguiendo las recomendaciones del libro, además de que el usuario diga la cantidad de rendijas, blancos, y clicks, diera las probabilidades de ir a cada blanco después de cruzar una rendija, esto se hace, ya que no se sabe con claridad si al multiplicar, haya superposiciones en las probabilidades que se cancelen, puesto que esto puede pasar en la multiples rendijas cuánticas.

Ejemplo:
Tenemos 4 blancos se necesitará un vector con sus correspondientes probabilidades a cada blanco:

[1/2, i/2, -1/2, -i/2]

Este sería el vector con las probabilidades solicitadas, como podemos a primera impresion no se parecen, sin embargo al hacer su norma al cuadrado comprobara que son la misma.
Se hace una observación que al evaluar la norma al cuadrado a cada probabilidad, la suma de estas debe dar 1:

Ejemplo:

(1/2)^2 + (i/2) ^2  + (-1/2)^2 + (-i/2)^2 = 1/4 + 1/4 + 1/4 + 1/4 = 1

Esto es para corroborar que los resultados de la función son correctos.

Por último la función de graficar solo recibe un parámetro, en esta función lo que debe graficar es el vector estado, la matriz asociada al sistema no se grafica.
### Construido con
* Python - Lenguaje de Programación
* Pycharm - IDE
* Git - Control de versiones
* GitHub - Aloja las versiones de Git
### Autores
* Wilmer Rodríguez
### Expresiones de Gratitud
Gracias a todo aquel que use esta librería, espero que les sea de ayuda.
