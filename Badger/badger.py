from controller import MyController
from adafruit_servokit import ServoKit
from time import sleep

pca = ServoKit(channels = 16)
controller = MyController(pcaBoard = pca, interface = "/dev/input/js0", connecting_using_ds4drv = False)
controller.listen(timeout = 60)