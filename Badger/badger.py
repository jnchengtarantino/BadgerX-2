from controller import MyController
from adafruit_servokit import ServoKit
from time import sleep
import os

def restart():
	os.system('sudo reboot')

pca = ServoKit(channels = 16)
controller = MyController(pca,"/dev/input/js0", False)
controller.listen(timeout = 60, on_disconnect=restart)
