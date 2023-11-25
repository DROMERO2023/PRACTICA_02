# EJERCICIO 09 - PC 02 - DENNIS ALFREDO ROMERO ROJAS
# Pseudocódigo:

# PASO 01: Se creará la función (omitir_vocales) definiéndose la variable "cadena_texto"

def omitir_vocales(cadena_texto):
    
# PASO 02: Declarar las variables vocales y resultado, precisando los elementos a ser evaluados y retirados de la cadena de texto (en este caso las vocales)  
    vocales = "aeiouAEIOU"
    
# PASO 03:  Construir una nueva cadena de texto, omitiendo las vocacales
    resultado = ""
    for letra in cadena_texto:
        if letra not in vocales:
            resultado += letra
    return resultado

# PASO 04:  Solicitar al usuario una cadena de texto
entrada_usuario = input("Ingrese una cadena de texto: ")

# PASO 05: Evaluar el resultado tomando como referencia la función (omitir_vocales)
resultado = omitir_vocales(entrada_usuario)

# PASO 06: Imprimir resultados
print(f"Texto con vocales omitidas: {resultado}")
