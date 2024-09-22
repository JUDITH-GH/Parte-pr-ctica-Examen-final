"""
Utilizar el concepto de módulo necesariamente.
Escribir un programa para el manejo de listas
el cuál cumplirá los siguientes requerimientos (4 ptos):
"""

# Crear una función que le permitirá almacenar 10 números aleatorios en una lista y finalmente los imprimirá por consola al llamar la función.
import random
def ListaNumerosAleatorios(cantidad=10):
    numeros_aleatorios = [random.randint(1, 100) for _ in range(cantidad)]
    print("Números aleatorios generados: {}".format(numeros_aleatorios))
    return numeros_aleatorios

# Crear una función que le permita almacenar los números no repetidos de la lista anterior, retornar este valor e imprimirlo por consola.
def ListaNumerosNoRepetidos(numeros_aleatorios):
    numerosAleatoriosNoReapetidos = list(set(numeros_aleatorios))
    print("Lista de numeros no repetidos: {}".format(numerosAleatoriosNoReapetidos))
    return numerosAleatoriosNoReapetidos

# Crear una función donde se creará una lista para ordenar de mayor a menor la lista que se creó en el ítem anterior (número no repetidos) y otra lista para ordenarlas de menor a mayor, retornar este valor e imprimirlos por consola.

def ordenarLista(numeros_aleatorios):
    mayor_a_menor = sorted(numeros_aleatorios, reverse=True)
    menor_a_mayor = sorted(numeros_aleatorios)
    print(" De mayor a menor: {}".format(mayor_a_menor))
    print(" De menor a mayor: {}".format(menor_a_mayor))
    return mayor_a_menor, menor_a_mayor

def mayor_numero_par(numeros):
    numeros_pares = [num for num in numeros if num % 2 == 0]
    mayor_par = max(numeros_pares) if numeros_pares else None
    print("Mayor número par:", mayor_par)
    return mayor_par

numeros_aleatorios = ListaNumerosAleatorios()
numeros_noRepetidos = ListaNumerosNoRepetidos(numeros_aleatorios)
ordenar_numeros = ordenarLista(numeros_aleatorios)
