# EJERCICIO 03 - PC 02 - DENNIS ALFREDO ROMERO ROJAS
# Pseudocódigo:

# PASO 01: Crear una lista para almacenar los números a ser ingresados:
numeros_ingresados = []  

# PASO 02: Definimos la variable numeros_pares = 0: Inicializamos esta variable en cero antes de comenzar el bucle para contar la cantidad de números pares. A medida que el usuario ingresa números, el programa verifica si cada número es par (numero % 2 == 0) y, si es así, incrementa la variable numeros_pares en 1.
numeros_pares = 0

# PASO 03: Similar a la variable de números pares, inicializamos numeros_impares en cero. Durante el bucle, si el número ingresado no es par, entonces es impar y se incrementa la variable numeros_impares en 1.
numeros_impares = 0

# PASO 04:  Generamos un bucle While Infinito, donde consulte la opción SI/NO para ingresar números, usaremos "upper" para asegurar el ingreso de texto en mayúscula
while True:
    respuesta = input("¿Desea ingresar un número? (SI/NO): ").upper()

# PASO 05:  Si la opción escrita es NO, se finaliza el bucle con el comando break, permitiendo al programa continuar con la siguiente parte del código
    if respuesta == "NO":
        break
    
# PASO 06:  Emplearemos "try" para manejar posibles errores durante la ejecución del programa (asegurar el ingreso de números enteros). En el caso no se ingrese un número entero se lanzará el error (PASO Nro 09)
    elif respuesta == "SI":
        try:
            numero = int(input("Ingrese el número: "))
# PASO 07:  Ingresado en número entero, emplearemos "append" para grabar el número ingresado al final de la lista generada al inicio

            numeros_ingresados.append(numero)
            
# PASO 08:  Procederemos a evaliar la lista de números almacenados (verificando cuales son los números pares y números impares)

            if numero % 2 == 0:
                numeros_pares += 1
            else:
                numeros_impares += 1
# PASO 09:  Se imprime un error en el caso el valor ingresado no cumple la condición de ser un número entero "try"
        except ValueError:
            print("¡Error! Usted debe ingresar un número entero.")

# PASO 10:  Finalmente se imprimirá la cantidad de números ingresados y por separado la cantidad de números pares e impares de la lista generada.

print("Números ingresados:", numeros_ingresados)
print("Cantidad de números pares:", numeros_pares)
print("Cantidad de números impares:", numeros_impares)
