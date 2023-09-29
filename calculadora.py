lista_alumnos = []
lista_notas = []

# Función para calcular promedio por alumno
def calcular_promedio(nota1, nota2, nota3):
    promedio = (nota1 + nota2 + nota3) / 3
    return promedio

# Función para calcular promedio de toda la clase
def calcular_promedio_clase(lista):
    suma = 0
    for x in lista:
        suma += x
    return suma / len(lista)

# Función para encontrar la nota más baja de un alumno
def encontrar_menor(lista):
    menor = lista[0]
    for x in lista:
        if x < menor:
            menor = x
    print(f"\nLa nota más baja es: {menor}")

# Función para encontrar la nota más alta de un alumno
def encontrar_mayor(lista):
    mayor = lista[0]
    for x in lista:
        if x > mayor:
            mayor = x
    print(f"\nLa nota más alta es: {mayor}")

# Función para calcular los alumnos que están por encima del promedio de la clase
def alumnos_arriba_promedio(lista, promedio_clase):
    indice = 0
    print("\nAlumnos por encima del promedio de la clase:")
    for a in lista:
        indice += 1
        if a.get('promedio')>promedio_clase:
            print(a.get('nombre').title(), a.get('promedio'))

cantidad_estudiantes = input("Ingrese el número total de estudiantes: ")
print("Esta clase tiene", cantidad_estudiantes, "estudiantes.")

for alumno in range(int(cantidad_estudiantes)):
    nombre = input("Ingrese el nombre y apellido del estudiante: ")
    calificaciones = input("Ingrese las calificaciones de este estudiante: ").split(" ")
    int_notas = list(map(int, calificaciones))
    nota1, nota2, nota3 = int_notas
    lista_notas.extend(int_notas)
    if 0<=int(nota1)<=100 and 0<=int(nota2)<=100 and 0<=int(nota3)<=100:
        promedio = calcular_promedio(nota1, nota2, nota3)
        alumno = dict([('nombre', nombre), ('promedio', promedio)])
        lista_alumnos.append(alumno)
    else:
        print(("---error: los datos ingresados no son correctos").upper())

print("---------\nLista de estudiantes:")
for a in lista_alumnos:
    print(f"-> {a.get('nombre').title()} -- {a.get('promedio')}")

promedio_clase = calcular_promedio_clase(lista_notas)
print(f"\nEl promedio de la clase es: {promedio_clase}")
encontrar_mayor(lista_notas)
encontrar_menor(lista_notas)
alumnos_arriba_promedio(lista_alumnos, promedio_clase)