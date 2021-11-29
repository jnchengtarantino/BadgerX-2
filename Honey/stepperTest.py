import RPi.GPIO as GPIO
from time import sleep

# GPIO mapping
DIR = 17
PUL = 3
EN = 4

# Directions
cw = 1
ccw = 0

GPIO.setmode(GPIO.BCM)
GPIO.setup(DIR, GPIO.OUT)
GPIO.setup(PUL, GPIO.OUT)
GPIO.setup(EN, GPIO.OUT)

GPIO.output(DIR, cw)


try:
	while True:
		sleep(1)
		GPIO.output(DIR, cw)
		GPIO.output(PUL, GPIO.HIGH)
		sleep(0.005)
		GPIO.output(PUL, GPIO.LOW)
		sleep(0.005)

		sleep(1)
		GPIO.output(DIR, ccw)
		GPIO.output(PUL, GPIO.HIGH)
		sleep(0.005)
		GPIO.output(PUL, GPIO.LOW)
		sleep(0.005)

except KeyboardInterrupt:
	print("cleanup")
	GPIO.cleanup()


