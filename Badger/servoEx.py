from adafruit_servokit import ServoKit
from time import sleep

# Example code on how to run the servo motors using the PCA9685 PWM board
# requires "sudo pip3 install adafruit-circuitpython-pca9685"
# requires "sudo pip3 install adafruit-circuitpython-servokit"

pca = ServoKit(channels = 16)
pca.servo[0].actuation_range = 270
pca.servo[1].actuation_range = 270
pca.servo[2].actuation_range = 270
pca.servo[3].actuation_range = 270
try:
    pca.servo[0].angle = 1
    while True:
        pca.servo[0].angle = 0
        pca.servo[1].angle = 0 
        pca.servo[2].angle = 0 
        pca.servo[3].angle = 0 
        sleep(2)
        pca.servo[0].angle = 270
        pca.servo[1].angle = 270
        pca.servo[2].angle = 270
        pca.servo[3].angle = 270
        sleep(2)
except KeyboardInterrupt:
	print("program stopped")
