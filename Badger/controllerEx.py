from pyPS4Controller.controller import Controller

# Bluetooth controller must be paired with the pi using bluetoothctl:
# sudo bluetoothctl
# scan on   (to search for the MAC address)
# pair <MAC>
# trust <MAC>

class MyController(Controller):
   
    def __init__(self, **kwargs):
        Controller.__init__(self, **kwargs)
    
    # Example of overloading button press functions
    def on_x_press(self):
        print("Hello World")
    def on_x_release(self):
        print("Goodbye World")

controller = MyController(interface = "/dev/input/js0", connecting_using_ds4drv = False)
controller.listen(timeout = 60)
