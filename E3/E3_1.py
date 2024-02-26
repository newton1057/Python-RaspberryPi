"""
Archivo: Ejercicio4.py
Equipo: #6
Integrantes del equipo: Integrante #1 Eduardo Isaac Dávila Bernal
                        Integrante #2 Natalia Victoria Nava
                        Integrante #3 Araujo Galan Maximiliano
Fecha: 16 / 10 / 2023
Descripcion: Escribe un programa que mida la distancia a través de un sensor ultrasónico, encienda uno de tres LEDs cuando se encuentre dentro de un rango de distancia específico y guarde la información en un archivo *.txt con el valor de la distancia con mensaje de alerta y fecha de cuando se leyó. Si la distancia calculada es inferior a 10cm, se enciende el LED rojo y se escribe el siguiente mensaje de alerta: MUY CERCA. Cuando es superior a 30, se enciende el LED verde y se escribe el siguiente mensaje de alerta: EXCELENTE. De lo contrario, se enciende el LED ámbar y se escribe el siguiente mensaje de alerta: CERCA.
"""

import RPi.GPIO as GPIO
import time
import datetime

# Configura los pines GPIO para el sensor ultrasónico y LEDs
GPIO.setmode(GPIO.BCM)
trigger_pin = 18
echo_pin = 24
red_led_pin = 17
amber_led_pin = 18
green_led_pin = 19

GPIO.setup(trigger_pin, GPIO.OUT)
GPIO.setup(echo_pin, GPIO.IN)
GPIO.setup(red_led_pin, GPIO.OUT)
GPIO.setup(amber_led_pin, GPIO.OUT)
GPIO.setup(green_led_pin, GPIO.OUT)

# Función para medir la distancia con el sensor ultrasónico
def medir_distancia():
    GPIO.output(trigger_pin, True)
    time.sleep(0.00001)
    GPIO.output(trigger_pin, False)

    pulse_start = time.time()
    pulse_end = time.time()

    while GPIO.input(echo_pin) == 0:
        pulse_start = time.time()

    while GPIO.input(echo_pin) == 1:
        pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start
    distancia = (pulse_duration * 34300) / 2  # La velocidad del sonido es de 343 m/s

    return distancia

try:
    while True:
        distancia = medir_distancia()
        fecha = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        if distancia < 10:
            mensaje_alerta = "MUY CERCA"
            GPIO.output(red_led_pin, GPIO.HIGH)
            GPIO.output(amber_led_pin, GPIO.LOW)
            GPIO.output(green_led_pin, GPIO.LOW)
        elif distancia > 30:
            mensaje_alerta = "EXCELENTE"
            GPIO.output(red_led_pin, GPIO.LOW)
            GPIO.output(amber_led_pin, GPIO.LOW)
            GPIO.output(green_led_pin, GPIO.HIGH)
        else:
            mensaje_alerta = "CERCA"
            GPIO.output(red_led_pin, GPIO.LOW)
            GPIO.output(amber_led_pin, GPIO.HIGH)
            GPIO.output(green_led_pin, GPIO.LOW)

        with open('informacion_distancia.txt', 'a') as file:
            file.write(f'Fecha: {fecha}, Distancia: {distancia:.2f} cm, Alerta: {mensaje_alerta}\n')

        time.sleep(1)  # Leer y actualizar cada segundo

except KeyboardInterrupt:
    GPIO.cleanup()


