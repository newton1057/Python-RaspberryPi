"""
Archivo: Ejercicio4.py
Equipo: #6
Integrantes del equipo: Integrante #1 Eduardo Isaac Dávila Bernal
                        Integrante #2 Natalia Victoria Nava
                        Integrante #3 Araujo Galan Maximiliano
Fecha: 16 / 10 / 2023
Descripcion: Escribe un programa donde se lea el uso de memoria ram y la gaurde en un archivo *.txt Para leer la memoria ram en porcentaje usar la siguiente linea. psutil.virtual_memory().available * 100 / psutil.virtual_memory().total
"""

import psutil
import RPi.GPIO as GPIO
import time

# Configura los pines GPIO
GPIO.setmode(GPIO.BCM)
led_pins = [17, 18, 19, 20]
for pin in led_pins:
    GPIO.setup(pin, GPIO.OUT)

# Función para encender los LEDs según el uso de la RAM
def controlar_leds(ram_percent):
    if ram_percent < 25:
        GPIO.output(17, 1)
        GPIO.output(18, 0)
        GPIO.output(19, 0)
        GPIO.output(20, 0)
    elif ram_percent < 50:
        GPIO.output(17, 1)
        GPIO.output(18, 1)
        GPIO.output(19, 0)
        GPIO.output(20, 0)
    elif ram_percent < 75:
        GPIO.output(17, 1)
        GPIO.output(18, 1)
        GPIO.output(19, 1)
        GPIO.output(20, 0)
    elif ram_percent < 90:
        GPIO.output(17, 1)
        GPIO.output(18, 1)
        GPIO.output(19, 1)
        GPIO.output(20, 1)

try:
    while True:
        # Obtener el uso de RAM en porcentaje
        ram_percent = psutil.virtual_memory().available * 100 / psutil.virtual_memory().total

        # Guardar el valor en un archivo de texto
        with open('uso_de_ram.txt', 'w') as file:
            file.write(f'Uso de RAM: {ram_percent:.2f}%')

        # Controlar los LEDs
        controlar_leds(ram_percent)

        time.sleep(60)  # Leer y actualizar cada minuto
except KeyboardInterrupt:
    GPIO.cleanup()

