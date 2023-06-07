import tkinter as tk
import csv
from datetime import datetime


def guardar_datos():
    # Obtener los datos ingresados por el usuario
    nombre = entry_nombre.get()
    edad = entry_edad.get()
    hora_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Guardar los datos en un archivo CSV
    with open('datos.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([nombre, edad, hora_actual])

    # Limpiar los campos de entrada
    entry_nombre.delete(0, tk.END)
    entry_edad.delete(0, tk.END)


if __name__ == "__main__":
    # Crear la ventana principal
    ventana = tk.Tk()
    ventana.title("Aplicativo CSV")

    # Crear etiquetas y campos de entrada para nombre y edad
    label_nombre = tk.Label(ventana, text="Nombre:")
    label_nombre.pack()
    entry_nombre = tk.Entry(ventana)
    entry_nombre.pack()

    label_edad = tk.Label(ventana, text="Edad:")
    label_edad.pack()
    entry_edad = tk.Entry(ventana)
    entry_edad.pack()

    # Crear el botón para guardar los datos
    boton_guardar = tk.Button(ventana, text="Guardar", command=guardar_datos)
    boton_guardar.pack()

    # Ejecutar la ventana principal
    ventana.mainloop()
