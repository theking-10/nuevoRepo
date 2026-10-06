from machine import Pin, Timer
import time

# --- Pines tiras 1-7 ---
PINES_SEQ = [2, 4, 5, 18, 19, 21, 22]

# --- Pin tira 8 independiente ---
PIN_LED8 = 23

# --- Tiempo entre cada tira (ms) --- mas rapido
TIEMPO_PASO = 150

# --- Pausa con todas encendidas (ms) ---
TIEMPO_ESTATICO = 10000

# --- Pausa cuando queda solo la 1 (ms) --- 1 segundo
TIEMPO_SOLA = 1000

# --- LED 8 cada 2 segundos ---
INTERVALO_LED8 = 2000

leds = [Pin(p, Pin.OUT) for p in PINES_SEQ]
led8 = Pin(PIN_LED8, Pin.OUT)

for led in leds:
    led.value(1)
led8.value(1)

estado_led8 = [False]

def toggle_led8(timer):
    estado_led8[0] = not estado_led8[0]
    led8.value(0 if estado_led8[0] else 1)

timer_led8 = Timer(0)
timer_led8.init(period=INTERVALO_LED8, mode=Timer.PERIODIC, callback=toggle_led8)

def secuencia():
    # Ida: encienden una a una y se quedan
    for i in range(7):
        leds[i].value(0)
        time.sleep_ms(TIEMPO_PASO)

    # Pausa todas encendidas
    time.sleep_ms(TIEMPO_ESTATICO)

    # Regreso: apagan de 7 hasta 2
    for i in range(6, 0, -1):
        leds[i].value(1)
        time.sleep_ms(TIEMPO_PASO)

    # Solo queda la 1, espera 1 segundo y se va
    time.sleep_ms(TIEMPO_SOLA)

    # Apaga la 1 y reinicia
    leds[0].value(1)
    time.sleep_ms(100)

while True:
    secuencia()
