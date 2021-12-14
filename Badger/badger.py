from controller import MyController
from pcaBoard import PcaBoard
from time import sleep
import threading
import os
import RPi.GPIO as GPIO
from driveSystem import Drive
from arm import Arm

def restart():
	os.system('sudo reboot')
def threadFunction(controller):
	print("Spawning controller thread")
	controller.listen(timeout = 60) #set on_disconnect=restart for final usage

GPIO.setmode(GPIO.BCM)
pca = PcaBoard()

#TODO test and fix all init/min/max angles
rotServo = pca.addServo(initAngle=0, minAngle=0,maxAngle=100)
fbServo = pca.addServo(minAngle = 0, maxAngle = 105)
udServo = pca.addServo() 
clawServo = pca.addServo
arm = Arm(pca, rotServo, fbServo, udServo, clawServo)

FL = pca.addMotor(14,15)
FR = pca.addMotor(23,24)
BL = pca.addMotor(10,9)
BR = pca.addMotor(6,5)
drive = Drive(pca, FL,FR,BL,BR)
controller = MyController(drive, arm, pca, "/dev/input/js0", False)
controllerThread = threading.Thread(target=threadFunction, args=[controller])
controllerThread.start()

while True:
	drive.step()
	pca.step()
	sleep(0.05)
