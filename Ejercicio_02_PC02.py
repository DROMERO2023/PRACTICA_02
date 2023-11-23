# EJERCICIO 02 - PC 02 - DENNIS ALFREDO ROMERO ROJAS

# Pseudocódigo:

print("********* CÓDIGO USANDO FOR *********")

# PASO 01: Definir el número de filas tanto del nivel superior y nivel inferior del patrón
numero_filasI = 5

# PASO 02: Iniciar con la impresión de la parte superior del patrón
for i in range(1, numero_filasI + 1):
    print('* ' * i)

# PASO 03: Iniciar con la impresión de la parte inferior del patrón
for i in range(numero_filasI - 1, 0, -1):
    print('* ' * i)
    

print("********* CÓDIGO USANDO WHILE *********")    
    

# PASO 01: Definición de la cantidad de filas en la parte superior e inferior del patrón
numero_filasII = 5

# PASO 02: Iniciar con la impresión de la parte superior del patrón con un bucle while
i = 1
while i <= numero_filasII:
    print('* ' * i)
    i += 1

# PASO 03: Iniciar con la impresión de la parte inferior del patrón con un bucle while
i = numero_filasII - 1
while i > 0:
    print('* ' * i)
    i -= 1