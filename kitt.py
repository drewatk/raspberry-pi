import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

leds = [13, 12, 16, 26, 20, 21]

    GPIO.setup(i, GPIO.OUT)
for i in leds:

print('Press ^C to exit')

try:
    while True:
        for i in leds:
            GPIO.output(i, 1)
            time.sleep(.1)
            GPIO.output(i, 0)
        for i in reversed(leds):
            GPIO.output(i, 1)
            time.sleep(.1)
            GPIO.output(i, 0)
except KeyboardInterrupt:
    pass
    
GPIO.cleanup()
