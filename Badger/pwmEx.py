from board import SCL, SDA
import busio
from adafruit_pca9685 import PCA9685
from adafruit_motor import servo
from time import sleep

i2c_bus = busio.I2C(SCL, SDA)
pca = PCA9685(i2c_bus)
pca.frequency = 50

# Set the PWM duty cycle for channel zero to 50%. duty_cycle is 16 bits to match other PWM objects
# but the PCA9685 will only actually give 12 bits of resolution.
# pca.channels[0].duty_cycle = 0x7FFF

servo = servo.Servo(pca.channels[0], min_pulse=500,max_pulse=2500, actuation_range=270)
for i in range(270):
    servo.angle = i
    sleep(0.03)
for i in range(270):
    servo.angle = 270 - i
    sleep(0.03)