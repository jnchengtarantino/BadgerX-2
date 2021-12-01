from controller import MyController
from pcaBoard import PcaBoard
from time import sleep
import os

def restart():
	os.system('sudo reboot')

pca = PcaBoard(nServos=4)
controller = MyController(pca,"/dev/input/js0", False)
controller.listen(timeout = 60, on_disconnect=restart)
