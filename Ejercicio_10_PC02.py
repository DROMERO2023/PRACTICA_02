# EJERCICIO 10 - PC 02 - DENNIS ALFREDO ROMERO ROJAS
# Pseudocódigo:

# PASO 01: Definir función (convertir_Fecha), declaramos a la vez lista de meses contemplados en un año:

def convertir_fecha(fecha):
    meses = [
        "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
        "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
    ]
    
# PASO 02: Realizar un proceso de verificación para validar si la fecha se encuentra en el formato: mes-día-año
    if "/" in fecha:
        partes = fecha.split("/")
        mes = int(partes[0])
        dia = int(partes[1])
        anio = int(partes[2])

# PASO 03: Verificar si la fecha ingresada está en el formato "Mes dia, año"
    else:
        partes = fecha.split()
        mes = meses.index(partes[0]) + 1
        dia = int(partes[1].strip(','))
        anio = int(partes[2])

# PASO 04: Cambiar de formato a la fecha inicial ingresada con la siguiente nomenclatura:AAAA-MM-DD
    fecha_formateada = f"{anio:04d}-{mes:02d}-{dia:02d}"
    return fecha_formateada

# PASO 05:  Luego de definir la función y sus variables. Solicitar al usuario ingresar una fecha:
fecha_usuario = input("Ingrese una fecha (en formato mes/día/año o Mes dia, año), importante no anteponga un cero (cero a la izquierda): ")

# PASO 06: Evaluar la información ingresada a través de la función definida (convertir_fecha)
resultado = convertir_fecha(fecha_usuario)

# PASO 07: Imprimir nuevo resultado:
print(f"Fecha formateada: {resultado}")
