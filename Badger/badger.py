from controller import MyController
from pcaBoard import PcaBoard
from time import sleep
import threading
import os
import RPi.GPIO as GPIO

def restart():
	os.system('sudo reboot')
def threadFunction(controller):
	print("Spawning controller thread")
	controller.listen(timeout = 60) #set on_disconnect=restart for final usage

GPIO.setmode(GPIO.BCM)
pca = PcaBoard()
pca.addServo()
pca.addServo(initAngle=90)
pca.addMotor(14,15)
controller = MyController(pca,"/dev/input/js0", False)
controllerThread = threading.Thread(target=threadFunction, args=[controller])
controllerThread.start()

while True:
	pca.step()
	sleep(0.05)