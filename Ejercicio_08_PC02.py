# EJERCICIO 08 - PC 02 - DENNIS ALFREDO ROMERO ROJAS
# Pseudocódigo:

# PASO 01: Definición de la variable "factorial"

def factorial(n):

# PASO 02: Validación, precisándose que el factorial no se encuentra definido para negativos. Caso contrario aplicar la fórmula de factoriales:
    if n < 0:
        return "El factorial no está definido para números negativos."
    elif n == 0 or n == 1:
        return 1
    else:
        resultado = 1
        for i in range(2, n + 1):
            resultado *= i
        return resultado

# PASO 03: Ingresar número para el cálculo del factorial correspondiente:

numero_ingresado = int(input("Ingrese un número para calcular su factorial: "))

# PASO 04: Analizar el valor ingresado e imprimir resultados:

if numero_ingresado < 0:
    print("El factorial no está definido para números negativos.")
else:
    resultado_factorial = factorial(numero_ingresado)
    print(f"El factorial de {numero_ingresado} es {resultado_factorial}.")
