# Capitulo 04 - Raspberry Pi con Python
## Actividad 02

1. Escribe un programa que lea los valores del sensor de humedad y temperatura y generen una grafica animada en tiempo real. Desplegar ambos valores (humedad y temperatura) en la misma figura, utilicen diferentes colores de lineas, agreguen titulo, nombre de los ejes y leyenda.

*No olviden siempre conectar una resistencia en serie a cada LED.
*Revisen la conexion correcta del sensor DHT11 (sección de abajo).
*No olviden utilizar el formato para el encabezado en cada archivo generado. 

## Requisitos
* Utilizar la libreria Adafruit_DHT para el ejercicio.
* Subir cada ejercicio en diferentes ramas de su repositorio (sean consistentes al momento de nombrar las ramas).
* Hacer merge de todas las ramas a la rama principal Main.
* Todos los integrantes deberán hacer al menos un commit por actividad.

## Formato para encabezado
```
"""
Archivo: nombreArchivo.py
Equipo: #
Integrantes del equipo: Integrante #1
                        Integrante #2
                        Integrante #3
Fecha: Fecha de creación
Descripcion: Copiar la instrucción del ejercicio.
"""
```

## Recursos
#### Documentacion Adafruit_DHT
[https://gpiozero.readthedocs.io/en/latest/index.html ](https://github.com/adafruit/Adafruit_CircuitPython_DHT)

#### Ejemplo conexion Sensor de Humedad y Temperatura (DHT11)
![image](https://github.com/Samsung-Innovation-Campus-OT23/C04_A02/assets/59269349/fa679ce5-8eaa-441b-a8aa-60b992453d08)

Para evitar algun error por falta de alguna dependencia correr los siguientes comandos:
```
sudo apt-get install libatlas-base-dev  
pip3 uninstall numpy  
sudo apt install python3-matplotlib   
sudo apt install python3-numpy 
sudo apt install pyhon3-pandas 
pip install Adafruit-DHT 
```

#### GPIO
![image](https://github.com/Samsung-Innovation-Campus-OT23/C03_A01/assets/59269349/efef1934-5244-4d22-9d8f-56442d71f5c9)
