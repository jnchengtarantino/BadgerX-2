from board import SCL, SDA
import busio
from adafruit_pca9685 import PCA9685
from adafruit_motor import servo
from time import sleep

# Assuming Servos are always going to be on the pins [0,nServos-1] 
# and pins [nServos, 15] can be used for pure pwm output
class PcaBoard: 
	def __init__(self, nServos, address = 64):
		print("PCA board init, nServos: "+str(nServos)+" address:"+str(address)) 
		self.i2c_bus = busio.I2C(SCL, SDA)
		self.pca = PCA9685(self.i2c_bus, address = address)
		self.pca.frequency = 50
		self.n = nServos
		self.servos = [servo.Servo(self.pca.channels[i], min_pulse=500,max_pulse=2500, actuation_range=270) for i in range(nServos)]

	def setAngle(self, servo, angle):
		print("PCA setAngle, servo: "+str(servo)+ " angle: "+str(angle))
		if (0 <= servo < self.n and 0 <= angle <= 270):
			self.servos[servo].angle = angle
		else:
			print("Angle " + str(angle) + " or servo " + str(servo) + " illegal")

	# Duty Cycle range [0x0000, 0xFFFF] = [0, 65535] for 0% to 100%
	def setDutyCycle(self, pin, amount):
		print("PCA setDutyCycle, pin: " +str(pin)+ "amount: " +str(amount))
		if (self.n <= pin <= 15 and 0x0000 <= amount <= 0xFFFF):
			self.pca.channels[pin].duty_cycle = amount
		else:
			print("Amount " + str(amount) + " or pin " + str(pin) + " illegal")
