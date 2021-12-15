from controller import MyController
from pcaBoard import PcaBoard
from time import sleep
import threading
import os
import RPi.GPIO as GPIO
from driveSystem import Drive
from arm import Arm
from stepperHandler import steppers

def restart():
	os.system('sudo reboot')
def threadFunction(controller):
	print("Spawning controller thread")
	controller.listen(timeout = 60) #set on_disconnect=restart for final usage

GPIO.setmode(GPIO.BCM)
pca = PcaBoard()
stepperHandler = steppers()

#TODO test and fix all init/min/max angles
Claw1Servo = pca.addServo
Claw1Motor = pca.addMotor(17, 27)
DropperMotor = pca.addMotor(10, 9)
TensionnerMotor = pca.addMotor(13, 19)
RotationStepper = stepperHandler.addStepper(14,15)
SlidingStepper = stepperHandler.addStepper(23,24)


controller = MyController(stepperHandler, pca, "/dev/input/js0", False)
controllerThread = threading.Thread(target=threadFunction, args=[controller])
controllerThread.start()




while True:
	stepperHandler.step()
	pca.step()
	sleep(0.05)
