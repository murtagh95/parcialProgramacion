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

from tkinter import Tk, Frame, Label

# ------CONSTANTES---------
COLOR_FONDO = "#8eedd2"
COLOR_TITULO = "#03076b"
COLOR_RED = "#f26e50"
SEPARADOR = "|-|"
MODELOS = ["Fiat", "Ford", "VW", "Audi", "Toyota"]


def mostrarMatriz(matriz):
    # Instancio un objeto que creara la ventana
    raiz = Tk()
    raiz.title("Matriz")  # Le doy un titulo a la ventana
    raiz.geometry("400x400")  # Le doy un tamaño a la ventana
    raiz.config(bg=COLOR_FONDO)  # Le doy un color de fondo a la ventana

    # Genero un lienzo para agregar contenido a el
    miFrame1 = Frame(raiz, bg=COLOR_FONDO)
    miFrame1.pack()

    # Recorro la matriz
    for fila in range(len(matriz)):
        for columna in range(len(matriz[fila])):
            # Agrego los nº que representaran las columnas en el grafico
            if fila == 0:
                Label(
                miFrame1, 
                text=columna, 
                bg=COLOR_FONDO, 
                fg=COLOR_RED,
                ).grid(row=fila, column=columna+1, padx=10, pady=10)
            
            # Agrego los nº que representaran las filas en el grafico
            if columna == 0:
                Label(
                miFrame1, 
                text=fila, 
                bg=COLOR_FONDO, 
                fg=COLOR_RED,
                ).grid(row=fila+1, column=columna, padx=10, pady=10)

            # Muestro el valor contenido en la matriz
            Label(
                miFrame1, 
                text=matriz[fila][columna], 
                bg=COLOR_FONDO, 
                fg=COLOR_TITULO,
                ).grid(row=fila+1, column=columna+1, padx=10, pady=10)
    # Hacemos que la ventana queda activa de forma permanente
    raiz.mainloop()

def mostrarVentaModelo(array):
    # Instancio un objeto que creara la ventana
    raiz = Tk()
    raiz.title("Matriz")  # Le doy un titulo a la ventana
    raiz.geometry("400x100")  # Le doy un tamaño a la ventana
    raiz.config(bg=COLOR_FONDO)  # Le doy un color de fondo a la ventana

    # Genero un lienzo para agregar contenido a el
    miFrame1 = Frame(raiz, bg=COLOR_FONDO)
    miFrame1.pack()

    # Recorro el array
    for i in range(len(array)):
        # Agrego los modelos que representaran las columnas en el grafico
        Label(
            miFrame1, 
            text=MODELOS[i], 
            bg=COLOR_FONDO, 
            fg=COLOR_RED,
            ).grid(row=0, column=i, padx=10, pady=10)
            
        # Muestro el valor contenido en la matriz
        Label(
            miFrame1, 
            text=array[i],
            bg=COLOR_FONDO, 
            fg=COLOR_TITULO,
            ).grid(row=1, column=i, padx=10, pady=10)
    
    # Hacemos que la ventana queda activa de forma permanente
    raiz.mainloop()

def guardarMatriz(matriz, nombreArchivo):
    # Abro el archivo en modo escrittura
    archivo = open(nombreArchivo , "w")

    # Guardo la matriz en un archivo
    for fila in matriz:
        for elemento in fila:
            archivo.write(str(elemento) + SEPARADOR)
        archivo.write("\n")
        
    # Cierro el archivo y lo elimino de la memoria
    archivo.close()
    del(archivo)

def leerMatriz(nombreArchivo):
    # Defino una matriz que sera la devuelta
    matriz = []
    #  Este arrey sera para agregar a la matriz
    arreglo = []

    # Abrimos el archivo modo lectura
    archivo = open(nombreArchivo, "r")  # La r es por lectura

    # Leo el contenido del archivo y lo guardo en una variable
    textoLista = archivo.readlines() 

    for lista in textoLista:

        contador = 0
        agregar = ""

        while True:
            try:
                # Separo la cadena segun un separador predefinido
                max = lista.index(SEPARADOR, contador)
                agregar = lista[contador: max]
                # Restablesco el inicio del nuevo elemento 
                contador += len(agregar) + len(SEPARADOR)
                # Compruebo si el valor es un nº para guardarlo como tal
                try:
                    arreglo.append(int(agregar))
                except:
                    try:
                        arreglo.append(float(agregar))
                    except:
                        arreglo.append(agregar)
                    
            except :
                # Como no se encuentra más separadores significa que no hay más elementos
                # Por eso agrego el arreglo a la matriz
                matriz.append(arreglo)
                arreglo = []
                break
    
    # Cierro el archivo y lo elimino de la memoria
    archivo.close()
    del(archivo)

    return matriz

def crearMatriz(f, c):
  matriz = []
  for _ in range(f):
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

def menu():
    print("\t\t----------------------MENU----------------------")
    print("Eligue una opción(escribir solo el nº):")
    print("\t1. Ver venta primer trimestre")
    print("\t2. Ver venta por marca")
    print("\t3. Ver marca vendida")
    print("\t4. Ver total de autos vendidos")
    print("\t5. Ver matriz")
    print("\t6. Salir")

def eleguirSiSeguir():
    while True:
        print("Desea continuar(Y/N):")
        try:
            valor = input(">").lower()
            print(valor)
            if valor != "y" and valor != "n":
                print("----ERROR----")
                continue 
            return valor
        except:
            print("----ERROR----")
            


filas, columnas = len(MODELOS), 6
STOCK_INICIAL = 30

matriz = crearMatriz(filas, columnas)
for i in range(filas):
    for j in range(columnas):
        matriz[i][j] = randint(1, 6)

# OPCIONAL CARGAR LA MATRIZ DE UN ARCHIVO EXTERNO
# guardarMatriz(matriz, "matriz.txt")
# matrizGuardada = leerMatriz("matriz.txt")

while True:
    print("\n\nEleguir que matriz desea usar(ingresar el nº de la opcion): ")
    print("\t 1. Matriz generada al azar")
    print("\t 2. Matriz cargada de un archivo externo")
    try:
        eleguir = int(input(">"))
        if eleguir == 1:
            break
        elif eleguir == 2:
            matriz = leerMatriz("matriz.txt")
            break
        else:
            print("Error, volver a eleguir")

    except:
        print("Error, volver a eleguir")

ventaXmodelo = ventaTotalXmarca(matriz)



while True:
    menu()
    try:
        opcion = int(input(">"))
        if opcion == 1:
            print("Suma de venta primer trimestre", controlVentaTotal(matriz, 3))
            op = eleguirSiSeguir()
            if(op == "n"):
                break

        elif opcion == 2:
            print("Suma de venta por marca", ventaXmodelo)
            mostrarVentaModelo(ventaXmodelo)
            op = eleguirSiSeguir()
            if(op == "n"):
                break
        elif opcion == 3:
            controlMin(ventaXmodelo)
            op = eleguirSiSeguir()
            if(op == "n"):
                break
        elif opcion == 4 :
            print("Suma de ventas total", ventaTotal(matriz))
            op = eleguirSiSeguir()
            if(op == "n"):
                break
        elif opcion == 5 :
            mostrarMatriz(matriz)
            op = eleguirSiSeguir()
            if(op == "n"):
                break
        else:
            break

    except:
        print("----------ERROR----------")
        print("Ingresar un número entero")

