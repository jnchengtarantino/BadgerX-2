from controller import MyController
from pcaBoard import PcaBoard
from time import sleep
import threading
import os

def restart():
	os.system('sudo reboot')
def threadFunction(controller):
	print("Spawning controller thread")
	controller.listen(timeout = 60) #set on_disconnect=restart for final usage

pca = PcaBoard(nServos=4)
controller = MyController(pca,"/dev/input/js0", False)
controllerThread = threading.Thread(target=threadFunction, args=(controller), daemon=True)
controllerThread.start()
