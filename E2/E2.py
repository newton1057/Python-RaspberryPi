"""
Archivo: Actividad02.py
Equipo: #6
Integrantes del equipo: Integrante #1 Eduardo Isaac Dávila Bernal
                        Integrante #2 Natalia Victoria Nava
                        Integrante #3 Araujo Galan Maximiliano
Fecha: 20 / 10 / 2023
Descripcion: Escribe un programa que lea los valores del sensor de humedad y temperatura y generen una grafica animada en tiempo real. Desplegar ambos valores (humedad y temperatura) en la misma figura, utilicen diferentes colores de lineas, agreguen titulo, nombre de los ejes y leyenda.
"""


import Adafruit_DHT
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from itertools import count
import time

# Configuración del sensor DHT11
sensor = Adafruit_DHT.DHT11
pin = 27  # Cambia esto al pin GPIO en el que tengas conectado el sensor

# Configuración de la gráfica
fig, ax = plt.subplots()
ax.set_xlabel('Tiempo')
ax.set_ylabel('Humedad (%) / Temperatura (°C)')
ax.set_title('Gráfica en Tiempo Real de Humedad y Temperatura')
humid_line, = ax.plot([], [], label='Humedad (%)', color='blue')
temp_line, = ax.plot([], [], label='Temperatura (°C)', color='red')
ax.legend()

ax.set_xlim([0, 20])  # Límite en el eje x (tiempo)
ax.set_ylim([0, 100])  # Límite en el eje y (humedad y temperatura)

# Inicialización de listas para datos
x_vals = []
y_humid = []
y_temp = []
x = count()

# Función para inicializar la gráfica
def init():
    humid_line.set_data([], [])
    temp_line.set_data([], [])
    return humid_line, temp_line

# Función para actualizar la gráfica en cada frame
def update(frame):
    try:
        humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
        x_vals.append(next(x))
        y_humid.append(humidity)
        y_temp.append(temperature)
        humid_line.set_data(x_vals, y_humid)
        temp_line.set_data(x_vals, y_temp)
        return humid_line, temp_line
    except KeyboardInterrupt:
        ani.event_source.stop()

# Configuración de la animación
ani = FuncAnimation(fig, update, frames=range(200), init_func=init, blit=True, repeat=False, interval=1000)

plt.show()

