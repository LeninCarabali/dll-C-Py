# DLL-C-Py

Este repositorio contiene los archivos necesarios para crear una DLL (Biblioteca de enlace dinámico (Dynamic-link library)) escrito en C y consumirlo otro lenguaje de progrmación, en este caso, Python. Calcular el tiempo de ejecución de la función con timeit y el tiempo total del aplicativo con CProfile. 

El código en c nos permite usar las instrucciones AVX (Advanced Vector Extensions) que son un conjunto de extensiones de conjunto de instrucciones introducidas por Intel y AMD para mejorar el rendimiento en cálculos vectoriales y de punto flotante, para nosotros poder hacer una multipliación de un escalar por un vector usando estas instrucciones que nos son de ayuda para aprovechar la infraestructura vetorial del procesador.

En el código de Py consumimos el dll, eclaramos e instanciamos los parametros con unos tipos de datos los parametros llamados ctypes que es un modulo que nos permite a los programas de Python llamar a funciones de bibliotecas compartidas escritas en C, y después realizar el llamado a la función con los valores instanciados y calcularle un small profiling a esas lineas de código.

## Instrucciones

### Compilación del archivo C

- gcc -fPIC -shared -o lib-mult-avx.so multescalar-avx-dll.c -mavx

### Flags ###

- -fPIC: Genera código de posición independiente.

- -shared: Produce una biblioteca compartida en lugar de un ejecutable.

- -o lib-mult-avx.so: Especifica el nombre del archivo de salida (biblioteca compartida).

- -mavx: Habilita las extensiones de instrucciones AVX durante la compilación.

### Ejecutar el archivo Py 

- python3 -m cProfile -s tottime mult_escalar_avx_dll.py

### Flags ###

- -m cProfile: Ejecuta el script con el módulo cProfile para hacer profiling del código Python.
- -s tottime: Ordena los resultados del profiling por tiempo total de ejecución en cada función.

### En caso de querer eliminar el .so creado: ###
- rm -f lib-mult-avx.so


## Integrantes 
- Lenin Carabali
- Victor Acuña
- Nicolas Granada
