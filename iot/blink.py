#blink.py

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)

try:

	while (True):
		GPIO.output(18, True)
		time.sleep(1)
		GPIO.output(18, False)
		time.sleep(1)

except KeyboardInterrupt:
	GPIO.output(18, GPIO.LOW)
	GPIO.cleanup()


