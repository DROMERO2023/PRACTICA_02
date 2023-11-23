# EJERCICIO 01 - PC 02 - DENNIS ALFREDO ROMERO ROJAS
# Pseudocódigo:

print("********* CÓDIGO USANDO FOR *********")

# PASO 01: Ingresar el rango de 1500 a 2700 con fines de encontrar números divisibles por 7 y múltiplos de 05
for numeroI in range(1500, 2701):
# PASO 02: Verificaremos si el número es divisible por 7 y múltiplo de 5
 if numeroI % 7 == 0 and numeroI % 5 == 0:
# PASO 03: Imrpimir los números encontrados
     print(numeroI)

print("********* CÓDIGO USANDO WHILE *********")

# PASO 01: Encontrar números divisibles por 7 y múltiplos de 05, en el rango de 1500 a 2700
   
numeroII = 1500

while numeroII <= 2700:
    if numeroII % 7 == 0 and numeroII % 5 == 0:
        
# PASO 02: Imprimir los números encontrados siempre y cuando cumpla la condición.
 
        print(numeroII)
    numeroII += 1