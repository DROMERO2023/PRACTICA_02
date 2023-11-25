# EJERCICIO 07 - PC 02 - DENNIS ALFREDO ROMERO ROJAS
# Pseudocódigo:

# PASO 01: Declarar una funión (numero_primo)
def numero_primo(numero):
    
# PASO 02: Establecer la condición matemática, precisando que los números menores o iguales a uno (1), no son primos:    
    
    if numero <= 1:
        return False  

# PASO 03: Validar si el número que se ha de ingresar, es divisible por algún número desde 2 hasta la raíz cuadrada de número + 1. Si no es divisible por ningún número es primo:
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False  # Si es divisible por algún número, no es primo

    return True  # Si no es divisible por ningún número, es primo

# PASO 04: Solicitar el ingreso de un número para validar si es Primo:
numero_ingresado = int(input("Ingrese un número para verificar si es primo: "))

# PASO 05: Evaluar e imprimir resultados, precisando si es un número primo o no es primo:
if numero_primo(numero_ingresado):
    print(f"{numero_ingresado} es un número primo.")
else:
    print(f"{numero_ingresado} no es un número primo.")
