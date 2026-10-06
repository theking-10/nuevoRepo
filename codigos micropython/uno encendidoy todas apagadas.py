from machine import Pin, Timer
import time

# --- Pines 1-7 ---
PINES_SEQ = [2, 4, 5, 18, 19, 21, 22]

# --- Pin independiente ---
PIN_LED8 = 23

# --- Tiempo entre pasos ---
TIEMPO_PASO = 150

# --- LED 8 cada 2 segundos ---
INTERVALO_LED8 = 2000

# Crear LEDs
leds = [Pin(p, Pin.OUT) for p in PINES_SEQ]
led8 = Pin(PIN_LED8, Pin.OUT)

# Todos encendidos al inicio
for led in leds:
    led.value(1)

led8.value(1)

# -------------------------
# LED 23 independiente
# -------------------------
estado_led8 = [False]

def toggle_led8(timer):
    estado_led8[0] = not estado_led8[0]
    led8.value(1 if estado_led8[0] else 0)

timer_led8 = Timer(0)
timer_led8.init(
    period=INTERVALO_LED8,
    mode=Timer.PERIODIC,
    callback=toggle_led8
)

# -------------------------
# Secuencia principal
# -------------------------
def secuencia():

    # Encender todas
    for led in leds:
        led.value(1)

    time.sleep_ms(TIEMPO_PASO)

    # Ir apagando una por una
    for i in range(7):

        # Mantener todas prendidas
        for j in range(7):
            leds[j].value(1)

        # Apagar la actual
        leds[i].value(0)

        time.sleep_ms(TIEMPO_PASO)

    # Apagar todas
    for led in leds:
        led.value(0)

    time.sleep_ms(TIEMPO_PASO)

    # Prender todas instantáneamente
    for led in leds:
        led.value(1)

# -------------------------
# Loop infinito
# -------------------------
while True:
    secuencia()