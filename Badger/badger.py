from controller import MyController

controller = MyController(interface = "/dev/input/js0", connecting_using_ds4drv = False)
controller.listen(timeout = 60)