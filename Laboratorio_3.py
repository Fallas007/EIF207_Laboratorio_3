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

print("Lista original:")
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
d1 = [random.randint(1, 1000) for _ in range(100)]

# Lista aleatoria de 500
d2 = [random.randint(1, 1000) for _ in range(500)]

# Lista aleatoria de 1000
d3 = [random.randint(1, 1000) for _ in range(1000)]

# Lista aleatoria de 5000
d4 = [random.randint(1, 1000) for _ in range(5000)]

# Medición para 100 elementos
inicio = time.perf_counter()
selection_sort(d1.copy())
fin = time.perf_counter()
print(f"Lista de 100 elementos  : {fin - inicio:.6f} segundos")

# Medición para 500 elementos
inicio = time.perf_counter()
selection_sort(d2.copy())
fin = time.perf_counter()
print(f"Lista de 500 elementos  : {fin - inicio:.6f} segundos")

# Medición para 1000 elementos
inicio = time.perf_counter()
selection_sort(d3.copy())
fin = time.perf_counter()
print(f"Lista de 1000 elementos : {fin - inicio:.6f} segundos")

# Medición para 5000 elementos
inicio = time.perf_counter()
selection_sort(d4.copy())
fin = time.perf_counter()
print(f"Lista de 5000 elementos : {fin - inicio:.6f} segundos")

# ---------------------------------------------------------------------------------
# PARTE IV: Diferentes condiciones de entrada
# CASO A: lista aleatoria
random.sample(range(1, 10000), 1000)

# Caso B: lista ordenada
list(range(1000))

# Caso C: lista ordenamiento inversamente
list(range(1000, 0, -1))

# ---------------------------------------------------------------------------------
# Parte V: Comparación con Python
