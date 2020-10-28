# 1. Ejercicio 1
# Una agencia de ventas de vehículos nos suministra la ventas de 5
# marcas diferentes de autos (por ej. Fiat, Ford, VW, Audi, Toyota)
# correspondiente a los primeros 6 meses del año 2020
# Nota: generar en forma aleotoria la venta correspondiente a los 6
# meses.
# Escribir el código en Python que nos permita obtener los siguientes
# datos:
# a. Cuántos autos se vendieron en el primer trimestre del año.
# b. Cuántos autos se vendieron, por marca.
# c. Cuál marca de auto se vendió menos.
# d. El total de autos vendidos.
from random import randint

def crearMatriz(f, c):
  matriz = []
  for i in range(f):
    matriz.append([0] * c)
  return matriz

def controlMin(sumaXmodelo):
    ventaMenor = min(sumaXmodelo)
    # Controlo si más de un modelo tiene el mismo n° de ventas minimas 
    if sumaXmodelo.count(ventaMenor) > 1: 
        for i in range(len(sumaXmodelo)):
            if sumaXmodelo[i] == ventaMenor:
                print("El modelo", i + 1, "fue uno de los menos vendidos, con un total de,", ventaMenor)
    else:
        index = sumaXmodelo.index(ventaMenor)
        print("El modelo", index + 1, "fue el menos vendidos, con un total de,", ventaMenor)

def controlMax(sumaXmodelo, str1):
    ventaMayor = max(sumaXmodelo)
    # Controlo si más de un modelo tiene el mismo n° de ventas maxima 
    if sumaXmodelo.count(ventaMayor) > 1: 
        for i in range(len(sumaXmodelo)):
            if sumaXmodelo[i] == ventaMayor:
                print(str1, i + 1, "fue uno de los más vendidos, con un total de", ventaMayor)
    else:
        index = sumaXmodelo.index(ventaMayor)
        print(str1, index + 1, "fue el más vendidos, con un total de ", ventaMayor)

def controlVentaTotal(matriz, cantidadMeses):
    suma = 0
    for i in range(len(matriz)):
        for j in range(cantidadMeses):
            suma += matriz[i][j]
    return suma

def ventaTotalXmarca(matriz):
    sumaXmodelo = [0] * len(matriz)
    for i in range(filas):
        for j in range(len(matriz[0])):
            sumaXmodelo[i] += matriz[i][j]
    
    return sumaXmodelo

def ventaTotal(matriz):
    suma = 0
    for fila in matriz:
        for elemento in fila:
            suma += elemento
    return suma

filas, columnas = 5, 6
STOCK_INICIAL = 30

matriz = crearMatriz(filas, columnas)
for i in range(filas):
    for j in range(columnas):
        matriz[i][j] = randint(1, 6)

ventaXmodelo = ventaTotalXmarca(matriz)

print(matriz)
print("Suma de venta primer trimestre", controlVentaTotal(matriz, 3))
print("Suma de venta por marca", ventaXmodelo)
controlMin(ventaXmodelo)
print("Suma de ventas total", ventaTotal(matriz))

