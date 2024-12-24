from machine import Pin
import time

# Configurar el pin 8 como salida
led = Pin(8, Pin.OUT)

while True:
    led.value(1)  # Encender el LED
    time.sleep(3) # Esperar 3 segundos
    led.value(0)  # Apagar el LED
    time.sleep(6) # Esperar 5 segundos
