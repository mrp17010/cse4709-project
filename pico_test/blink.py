from machine import Pin, Timer

led = Pin("LED", Pin.OUT)
tim = Timer()
def tick(timer):
    led.toggle()

tim.init(freq=2, mode=Timer.PERIODIC, callback=tick)


# from machine import Pin
# from time import sleep

# pin = Pin("LED", Pin.OUT)

# while True:
#     pin.toggle()
#     sleep(1)
