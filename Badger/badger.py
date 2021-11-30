from controller import MyController
from adafruit_servokit import ServoKit
from time import sleep

pca = ServoKit(channels = 16)
controller = MyController(pca,"/dev/input/js0", False)
controller.listen(timeout = 60)