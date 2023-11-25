# EJERCICIO 05 - PC 02 - DENNIS ALFREDO ROMERO ROJAS
# Pseudocódigo:

# PASO 01: Definir una función que disponga de dos variables (número y dígito). El objetivo será contar cuántas veces aparece el dígito indicado en un determinado número

def contar_digitos(numero, digito):
    
# PASO 02: Realizaremos una conversión de la variable número a una cadena (con el objetivo de usar el método count)
    
    numero_str = str(numero)
    
# PASO 03: Se realizará una validación con fines de saber si el dígito ingresado se encuentra en el número, caso contrario se notificará como valor CERO (0)
    
    if str(digito) in numero_str:
    
# PASO 04: Declarar una variable "contar_cantidad_numeros" y emplear el método count

        contar_cantidad_numeros = numero_str.count(str(digito))
    
        return contar_cantidad_numeros

    else:
        return 0    

# PASO 05: Solicitar al usuario ingresar un número y el dígito a ser analizado (cantidad de veces que se repite)

numero_ingresado = int(input("Ingrese un número entero: "))
digito_solicitado = int(input("Ingrese un dígito: "))

# PASO 06: Llamar a la función creada (contar_digitos)
resultado = contar_digitos(numero_ingresado, digito_solicitado)

# Imprimir el resultado
print(f"Número ingresado: {numero_ingresado} y Dígito: {digito_solicitado}")
print(f"La cantidad de veces que se repite el dígito: {digito_solicitado} en el número ingresado es: {resultado}")