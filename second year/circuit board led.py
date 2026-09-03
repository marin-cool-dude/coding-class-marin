#coding will become real in 3 2 1
import machine
import time
orangeLED = machine.Pin(0,machine.Pin.OUT)
while True:
    print('LED is on for 5 seconds')
    orangeLED.value(1)
    time.sleep_ms(5000)
    orangeLED.value(0)
    time.sleep_ms(5000) 