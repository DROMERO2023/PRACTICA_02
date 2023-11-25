# EJERCICIO 06 - PC 02 - DENNIS ALFREDO ROMERO ROJAS
# Pseudocódigo:

# PASO 01: Definir una función (Serie_Fibonacci), declarando a la vez la variable "n"

def Serie_Fibonacci(n):
    
# PASO 02: Crear una lista con dos elementos [0, 1], definiendo la variable "Series", dichos valores de la lista se configurarán con los primeros números de la serie de Fibonacci, el método "append" servirá para agregar nuevos valores al final de la lista    
    series = [0, 1]
    while series[-1] + series[-2] <= n:
        series.append(series[-1] + series[-2])
    return series

# PASO 03:  Imprimir la serie de Fibonacci entre 0 y 50
resultado = Serie_Fibonacci(50)
print("Serie de Fibonacci hasta 50:", resultado)
