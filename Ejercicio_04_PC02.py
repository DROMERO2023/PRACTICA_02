# EJERCICIO 04 - PC 02 - DENNIS ALFREDO ROMERO ROJAS
# Pseudocódigo:

# PASO 01: Creamos una lista para almacenar los datos de los alumnos y sus respectivas calificaciones:
lista_alumnos = []

#  PASO 02: Solicitar al docente del curso, ingresar la cantidad de alumnos que desea registrar:
n = int(input("Ingrese la cantidad de alumnos: "))

# PASO 03: Se generará un buble "for" tomando en consideración la cantidad de alumnos almacenados en la variable "n"
for _ in range(n):
 
# PASO 04: Una vez se disponga de la cantidad de estudiantes, se deberá proceder a registrar sus datos personales (Nombres y Apellidos)

    nombre_alumno = input("Ingrese los Nombres y Apellidos del alumno: ")
    
# PASO 05:Ingresado el nombre y apellido, se procederá a registrar las 03 Calificaciones del Alumno, creándose una lista para almacenar tres notas. Se ha considerado "float" para permitir la entrada de calificaciones con parte fraccionaria, ya que las calificaciones a menudo no son números enteros
    calificaciones = []
    for i in range(3):
        calificacion = float(input(f"Ingrese la calificación {i + 1} del alumno {nombre_alumno}: "))
        calificaciones.append(calificacion)

# PASO 06: Proceder a crear un diccionario con la información individual de cada alumno y sus calificaciones correspondientes:

    alumno = {"Alumno": nombre_alumno, "Notas": calificaciones}

# PASO 07: Proceder a agregar el diccionario generado a la Lista de Alumnos 
    lista_alumnos.append(alumno)

# PASO 08: Finalmente, se procederá con la impresión del Listado completo de alumnos y sus respectivas calificaciones:
print("\nListado completo de alumnos:")
for alumno in lista_alumnos:
    print(alumno)
