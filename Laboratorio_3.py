# Nombre de los estudiantes:
# 1. Reychel Fallas Monge
# 2. Jordana Montoya


# Laboratorio #3 de Estructuras de Datos
# Fecha de entrega: 28 de agosto, 2026

# ---------------------------------------------------------------------------------
# Librerias
import random
import time




# ---------------------------------------------------------------------------------
# PARTE I: Genere una lista con 20 nUmeros enteros aleatorios entre 1 y 100

datos = [random.randint(1, 100) for _ in range(20)]

print("----------------- PARTE I -----------------")
print("Lista NO copia:")
print(datos)

# Se utilizara una copia de la lista
lista = datos.copy()






# ---------------------------------------------------------------------------------
# PARTE II: selection sort
# Buscar el menor elemento de la sección no ordenada de la lista y colocarlo en su posición correcta.
# Retornar: lista_ordenada, comparaciones e intercambios.

def selection_sort(a):
    n = len(a)
   
    for i in range(n-1):
        min_idx = i
        for j in range(i+1, n):
            if a[j]<a[min_idx]:
                min_idx = j
               
            if min_idx != i:
                a[i], a[min_idx] = a[min_idx], a[i]
              


# Casos de prueba
print("\n----------------- PARTE II -----------------")
print(f"Lista sin ordenar:", lista)
selection_sort(lista)
print(f"Lista ordenada:   ", lista)




# ---------------------------------------------------------------------------------
# PARTE III: Comparacion experimental
# Mide el tiempo de recorrido del ordenamiento

inicio = time.perf_counter()
# algoritmo
fin = time.perf_counter()
tiempo = fin - inicio

# Lista aleatoria de 100
d1 = [random.randint(1, 10000) for _ in range(100)]

# Lista aleatoria de 500
d2 = [random.randint(1, 10000) for _ in range(500)]

# Lista aleatoria de 1000
d3 = [random.randint(1, 10000) for _ in range(1000)]

# Lista aleatoria de 5000
d4 = [random.randint(1, 10000) for _ in range(5000)]

# Medicion para 100 elementos
print("\n----------------- Parte III -----------------")
inicio = time.perf_counter()
selection_sort(d1.copy())
fin = time.perf_counter()
print(f"Lista de 100 elementos  : {fin - inicio:.6f} segundos")

# Medicion para 500 elementos
inicio = time.perf_counter()
selection_sort(d2.copy())
fin = time.perf_counter()
print(f"Lista de 500 elementos  : {fin - inicio:.6f} segundos")

# Medicion para 1000 elementos
inicio = time.perf_counter()
selection_sort(d3.copy())
fin = time.perf_counter()
print(f"Lista de 1000 elementos : {fin - inicio:.6f} segundos")

# Medicion para 5000 elementos
inicio = time.perf_counter()
selection_sort(d4.copy())
fin = time.perf_counter()
print(f"Lista de 5000 elementos : {fin - inicio:.6f} segundos")

# ---------------------------------------------------------------------------------
# PARTE IV: Diferentes condiciones de entrada

# CASO A: lista aleatoria
listaA = random.sample(range(1, 10000), 1000)

# Caso B: lista ordenada
listaB = list(range(1000))

# Caso C: lista ordenamiento inversamente
listaC = list(range(1000, 0, -1))

print("\n----------------- PARTE IV ----------------- ")
# Medicion para 500 elementos
inicio = time.perf_counter()
selection_sort(listaA.copy())
fin = time.perf_counter()
print(f"Lista A de 1000 elementos (ALEATORIA)     : {fin - inicio:.6f} segundos")

# Medicion para 1000 elementos
inicio = time.perf_counter()
selection_sort(listaB.copy())
fin = time.perf_counter()
print(f"Lista B de 1000 elementos (ORDANADA)      : {fin - inicio:.6f} segundos")

# Medicion para 5000 elementos
inicio = time.perf_counter()
selection_sort(listaC.copy())
fin = time.perf_counter()
print(f"Lista C de 5000 elementos (ORDEN INVERSO) : {fin - inicio:.6f} segundos")
# ---------------------------------------------------------------------------------
# Parte V: Comparacion con Python

datos = random.sample(range(1, 1000000), 100000)

def merge_sort(lista):  # <--- Agregado 'lista' aquí
    if len(lista) <= 1:
        return lista

    medio = len(lista) // 2
    # Debes pasar las sublistas como argumento en las llamadas recursivas
    izquierda = merge_sort(lista[:medio])  
    derecha = merge_sort(lista[medio:])

    return _merge(izquierda, derecha)

def _merge(izquierda, derecha):
    resultado = []
    i = j = 0

    while i < len(izquierda) and j < len(derecha):
        if izquierda[i] < derecha[j]:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1

    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])
    return resultado

def quick_sort(lista):
    if len(lista) <= 1:
        return lista

    pivote = lista[len(lista) // 2]
    menores = [x for x in lista if x < pivote]
    iguales = [x for x in lista if x == pivote]
    mayores = [x for x in lista if x > pivote]

    return quick_sort(menores) + iguales + quick_sort(mayores)


print("----------------- PARTE V ----------------- ")

# 1. Prueba con sorted()
copia = datos.copy()
inicio = time.perf_counter()
resultado = sorted(copia)
fin = time.perf_counter()
print(f"sorted() nativo: {fin - inicio:.5f} segundos")

# 2. Prueba con Merge Sort
copia = datos.copy()
inicio = time.perf_counter()
merge_sort(copia)
fin = time.perf_counter()
print(f"Merge Sort: {fin - inicio:.5f} segundos")

# 3. Prueba con Quick Sort
copia = datos.copy()
inicio = time.perf_counter()
quick_sort(copia)  # Coloca aquí tu función de Quick Sort
fin = time.perf_counter()
print(f"Quick Sort: {fin - inicio:.5f} segundos")

