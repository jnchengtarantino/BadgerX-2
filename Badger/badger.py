from controller import MyController
from pcaBoard import PcaBoard
from time import sleep
import threading
import os
import RPi.GPIO as GPIO
import driveSystem

def restart():
	os.system('sudo reboot')
def threadFunction(controller):
	print("Spawning controller thread")
	controller.listen(timeout = 60) #set on_disconnect=restart for final usage

GPIO.setmode(GPIO.BCM)
pca = PcaBoard()
pca.addServo(initAngle=90, minAngle=80,maxAngle=100)
#pca.addServo(minAngle = 0, maxAngle = 105)
FL = pca.addMotor(14,15)
FR = pca.addMotor(23,24)
BL = pca.addMotor(10,9)
BR = pca.addMotor(8,7)
drive = driveSystem(pca, FL,FR,BL,BR)
controller = MyController(drive, pca, "/dev/input/js0", False)
controllerThread = threading.Thread(target=threadFunction, args=[controller])
controllerThread.start()

while True:
	drive.step()
	pca.step()
	sleep(0.05)
