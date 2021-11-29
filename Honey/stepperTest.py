import RPi.GPIO as GPIO
from time import sleep

# GPIO mapping
DIR = 17
PUL = 27
EN = 22

# Directions
cw = 0
ccw = 1

GPIO.setmode(GPIO.BCM)
GPIO.setup(DIR, GPIO.OUT)
GPIO.setup(PUL, GPIO.OUT)
GPIO.setup(EN, GPIO.OUT)

GPIO.output(DIR,ccw)


try:
	while True:
		GPIO.output(DIR, cw)
		GPIO.output(PUL, GPIO.HIGH)
		sleep(0.005)
		GPIO.output(PUL, GPIO.LOW)
		sleep(0.005)
except KeyboardInterrupt:
	print("cleanup")
	GPIO.cleanup()


