import RPi.GPIO as GPIO
from time import sleep

# GPIO mapping
DIR = 17
PUL = 27
EN = 22

# Directions
cw = GPIO.LOW
ccw = GPIO.HIGH

GPIO.setmode(GPIO.BCM)
GPIO.setup(DIR, GPIO.OUT)
GPIO.setup(PUL, GPIO.OUT)
GPIO.setup(EN, GPIO.OUT)

GPIO.output(DIR,ccw)

CONTROLLER_SCALE = 2**15

class steppers: 

	def __init__(self):
		# a stepper has a direction pin, a pulse pin, a speed pin and a coefficient
		self.Steppers = []

	def addStepper(self, direction, pulse):
		GPIO.setup(direction, GPIO.OUT)
		GPIO.setup(pulse, GPIO.OUT)
		self.Steppers.append([direction, pulse, 0, 0])
		return self.Steppers.index([direction, pulse, 0, 0])

	def step(self):
		for s in self.Steppers:
			if s[3]%s[2] is 0:
				s[1] = GPIO.HIGH
			else:
				s[1] = GPIO.LOW



