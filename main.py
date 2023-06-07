import tkinter as tk
import csv
from datetime import datetime


def guardar_datos(evento):
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


def inicio_entrenamiento():
    hora_inicio = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    guardar_datos_entrenamiento("Inicio", hora_inicio)


def final_entrenamiento():
    hora_final = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    guardar_datos_entrenamiento("Final", hora_final)


def guardar_datos_entrenamiento(etapa, hora):
    # Guardar los datos de entrenamiento en un archivo CSV
    with open('datos_entrenamiento.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([etapa, hora])


if __name__ == "__main__":
    # Crear la ventana principal
    ventana = tk.Tk()
    ventana.title("Aplicativo CSV")

    # Crear etiquetas y campos de entrada para nombre y edad
    label_nombre = tk.Label(ventana, text="Peso_kg:")
    label_nombre.pack()
    entry_nombre = tk.Entry(ventana)
    entry_nombre.pack()

    label_edad = tk.Label(ventana, text="Alimento:")
    label_edad.pack()
    entry_edad = tk.Entry(ventana)
    entry_edad.pack()

    # Crear el botón para guardar los datos
    boton_guardar = tk.Button(ventana, text="Guardar", command=guardar_datos)
    boton_guardar.pack()

    # Crear el botón para iniciar el entrenamiento
    boton_inicio = tk.Button(ventana, text="Inicio Entrenamiento", command=inicio_entrenamiento)
    boton_inicio.pack()

    # Crear el botón para finalizar el entrenamiento
    boton_final = tk.Button(ventana, text="Final Entrenamiento", command=final_entrenamiento)
    boton_final.pack()

    # Ejecutar la ventana principal
    ventana.mainloop()
