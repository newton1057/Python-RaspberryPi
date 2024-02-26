"""
Archivo: Ejercicio2.py
Equipo: #6
Integrantes del equipo: Integrante #1 Eduardo Isaac Dávila Bernal
                        Integrante #2 Natalia Victoria Nava
                        Integrante #3 Araujo Galan Maximiliano 
Fecha: 09 / 10 / 2023
Descripcion: Escribe un programa de control de LEDs utilizando GPIO Zero para simbolizar un semaforo: LED Verde, Ámbar y Rojo. Por consola se escribe si queremos el siga (Verde), precaución (Ámbar) y alto (Rojo).
"""

from gpiozero import LED
from time import sleep

# Configura los pines GPIO para los LEDs
led_verde = LED(17)  # Cambia el número de pin según tu configuración
led_ambar = LED(18)  # Cambia el número de pin según tu configuración
led_rojo = LED(19)   # Cambia el número de pin según tu configuración

# Función para controlar el semáforo
def controlar_semaforo(estado):
    if estado == "verde":
        led_verde.on()
        led_ambar.off()
        led_rojo.off()
    elif estado == "ambar":
        led_verde.off()
        led_ambar.on()
        led_rojo.off()
    elif estado == "rojo":
        led_verde.off()
        led_ambar.off()
        led_rojo.on()
    else:
        print("Estado desconocido")

try:
    while True:
        opcion = input("Escribe 'verde', 'ambar' o 'rojo' para controlar el semáforo (o 'salir' para salir): ")
        if opcion == "salir":
            break
        controlar_semaforo(opcion)
except KeyboardInterrupt:
    pass
finally:
    # Apaga todos los LEDs antes de salir
    led_verde.off()
    led_ambar.off()
    led_rojo.off()

