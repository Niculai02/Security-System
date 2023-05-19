from machine import Pin, UART
import time
 
pir = Pin(22, Pin.IN, Pin.PULL_DOWN) #PIR sensor
ser = UART(0, 9600)  # Bluetooth module
n = 0
red = Pin(6, Pin.OUT) # LED
red.low()
print('Starting up the PIR Module')
time.sleep(1)
print('Ready')
ser.write('Ready\n')
 
while True:
     if pir.value() == 1:
          red.high()
          n = n+1
          ser.write('*/Motion Detected \n') # The * characters will be replaced by the phone number where the alert will be sent
     time.sleep(1)
     red.low()
