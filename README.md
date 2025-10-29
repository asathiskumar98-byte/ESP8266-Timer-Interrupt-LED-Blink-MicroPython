# ⚡ ESP8266 Timer Interrupt LED Blink — MicroPython

## 🧠 Overview
This project demonstrates how to blink an LED using **Timer Interrupts** on an **ESP8266** board with **MicroPython**.  
A hardware timer periodically toggles an LED connected to **GPIO2** every second — no `while True` loop required!

---

## ⚙️ Hardware Setup

| Component | Pin    | Description       |
|------------|--------|-------------------|
| LED        | GPIO2  | Output LED        |
| Timer0     | —      | Internal Timer    |

🪛 Connect an LED (with a 220Ω resistor) to **GPIO2** of your ESP8266.

---

## 🧩 Code

```python
import machine
# GPIO2 = LED1
led = machine.Pin(2, machine.Pin.OUT)

tim0 = machine.Timer(0)

def timer0_handle(timer):
    led.value(not led.value())  # Toggling LED GPIO2

tim0.init(period=1000, mode=machine.Timer.PERIODIC, callback=timer0_handle)
