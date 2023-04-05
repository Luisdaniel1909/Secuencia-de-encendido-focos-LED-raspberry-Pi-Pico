import machine
import utime

# Se definen los pines a utilizar para los LEDs
led_pins = [2, 3, 4, 5, 6, 7, 8]

# Configurar los pines como salidas
leds = [machine.Pin(pin, machine.Pin.OUT) for pin in led_pins]

# Se define la duración de cada estado de encendido/apagado de los LEDs en segundos
duracion = 0.1

while True:
    # Enciende el LED del medio
    leds[3].value(1)
    utime.sleep(duracion)

    # Enciende los LEDs de los extremos
    leds[2].value(1)
    leds[4].value(1)
    utime.sleep(duracion)

    # Enciende los LEDs adyacentes a los de los extremos
    leds[1].value(1)
    leds[5].value(1)
    utime.sleep(duracion)

    # Enciende los LEDs adyacentes a los del paso anterior
    leds[0].value(1)
    leds[6].value(1)
    utime.sleep(duracion)

    # Apaga todos los LEDs
    for led in leds:
        led.value(0)
    utime.sleep(duracion)
