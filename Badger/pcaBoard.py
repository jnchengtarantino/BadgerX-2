from board import SCL, SDA
import busio
from adafruit_pca9685 import PCA9685
from adafruit_motor import servo
from time import sleep

DEFAULT_SCALE_FACTOR = -1/(2**11)

class mServo:
	def __init__(self, pin, initAngle=0, minAngle=0, maxAngle=270):
		print("initializing new servo on pin " + str(pin))
		self.initAngle = initAngle
		self.minAngle = minAngle
		self.maxAngle = maxAngle
		self.pin = pin
		self.increment = 0	# Raw value from joy stick, needs to be scaled by self.scale
		self.servo = None
		self.scale = DEFAULT_SCALE_FACTOR

	def setScale(self,val):
		self.scale = val
	
	def setAngle(self, angle):
		print("PCA setAngle, servo: "+str(self.pin)+ " angle: "+str(angle))
		if (self.minAngle <= angle <= self.maxAngle):
			self.servo.angle = angle
		else:
			print("Angle " + str(angle) + " illegal")
	
	def setIncrement(self, val):
		self.increment = val

	def step(self):
		self.servo.angle = min(max(self.servo.angle + (self.increment * self.scale), self.minAngle), self.maxAngle)


# Assuming Servos are always going to be on the pins [0,nServos-1] 
# and pins [nServos, 15] can be used for pure pwm output
class PcaBoard: 
	def __init__(self, address = 64):
		print("PCA board init, address:"+str(address)) 
		self.i2c_bus = busio.I2C(SCL, SDA)
		self.pca = PCA9685(self.i2c_bus, address = address)
		self.pca.frequency = 50
		self.servos = []
		self.motors = []

	def addServo(self, initAngle=0, minAngle=0, maxAngle=270):
		if len(self.servos) < 16:
			i = len(self.servos)
			self.servos.append(mServo(i))
			self.servos[i].servo = servo.Servo(self.pca.channels[i], min_pulse=500,max_pulse=2500, actuation_range=270)
			return i
		else:
			print("Already at max servos")
			return None

	def setAngle(self, servo, angle):
		self.servos[servo].setAngle(angle)

	def setIncrement(self, servo, val):
		self.servos[servo].setIncrement(val)

	# Duty Cycle range [0x0000, 0xFFFF] = [0, 65535] for 0% to 100%
	def setDutyCycle(self, pin, amount):
		print("PCA setDutyCycle, pin: " +str(pin)+ " amount: " +str(amount))
		if (self.n <= pin <= 15 and 0x0000 <= amount <= 0xFFFF):
			self.pca.channels[pin].duty_cycle = amount
		else:
			print("Amount " + str(amount) + " or pin " + str(pin) + " illegal")

	def step(self):
		for s in self.servos:
			s.step()