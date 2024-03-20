import ctypes
import timeit

# Cargar la biblioteca compartida
lib_mult_avx = ctypes.CDLL('/home/lecm/IDP/clase_5/lib-mult-avx.so')

# Definir la firma de la función
lib_mult_avx.vectorScalarMultiply.argtypes = [ctypes.POINTER(ctypes.c_double), ctypes.c_double, ctypes.POINTER(ctypes.c_double), ctypes.c_int]

# Ejemplo de datos de entrada
vectorSize = 10000000
vector = (ctypes.c_double * vectorSize)(*range(1, vectorSize + 1))
scalar = 2
result = (ctypes.c_double * vectorSize)()

#inicar a medir le tiempo
starting_time = timeit.default_timer()

# Llamar a la función desde la biblioteca compartida
lib_mult_avx.vectorScalarMultiply(vector, scalar, result, vectorSize)

# finalizar la medición de tiempo
ending_time = timeit.default_timer()

# Imprimir el tiempo transcurrido
print(f"Tiempo transcurrido {ending_time - starting_time}") # f-strings

# Imprimir el resultado
# print("Resultado:")
# for i in range(vectorSize):
#     print(result[i])
