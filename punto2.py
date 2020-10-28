# 2.-Ejercicio 2
# Generar una clase denominada Matriz la cual reciba 3 parámetros un
# parámetro para la cantidad de filas, un parámetro para cantidad de
# columnas y un tercer parámetro opcional que nos indica el valor con el
# cual se inicializara la matriz si no se indica se debe inicializar toda la
# matriz con ceros.
# ejemplo de instanciación
# p = Matriz(2,2) en este caso se genera una matriz de 2 filas y 2
# columnas , como no se envia el tercer parámetro la matriz se inicializa
# con ceros.
# otra= Matriz(5,2,-1) en este caso se genera una matriz de 5 filas y 2
# columnas , como se envia el tercer parametro la matriz se inicializa con
# toda con -1.

from tkinter import Tk, Frame, Label

# ------CONSTANTES---------
COLOR_FONDO = "#8eedd2"
COLOR_TITULO = "#03076b"
COLOR_RED = "#f26e50"


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


class Matriz():
    def __init__(self, filas, columnas, valorInicial = 0):
        self.filas = filas
        self.columnas = columnas
        self.valorInicial = valorInicial
        self.matriz = self.crearMatriz()
    
    def crearMatriz(self):
        matriz = []
        for _ in range(self.filas):
            matriz.append([self.valorInicial] * self.columnas)
        return matriz

p = Matriz(2,2)
print(p.matriz)
mostrarMatriz(p.matriz)

p1 = Matriz(2,2,2)
print(p1.matriz)
mostrarMatriz(p1.matriz)
