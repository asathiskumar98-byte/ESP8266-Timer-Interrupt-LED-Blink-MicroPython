import machine
#GPIO2 = LED1
#GPIO0 = Pushbutton
led = machine.Pin(2,machine.Pin.OUT)

tim0 = machine.Timer(0)

def timer0_handle(timer):
    led.value(not led.value()) #toggling of LED GPIO2
    
tim0.init(period=1000, mode=machine.Timer.PERIODIC, callback=timer0_handle)
