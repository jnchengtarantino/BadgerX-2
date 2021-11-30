from pyPS4Controller.controller import Controller
from adafruit_servokit import ServoKit
from time import sleep

class MyController(Controller):
   
	def __init__(self, pcaBoard, interface, connecting_using_ds4drv):
		self.pca = pcaBoard
		print(interface)
		print(connecting_using_ds4drv)
		Controller.__init__(self, interface, connecting_using_ds4drv)
    
    # Example of overloading button press functions
	def on_x_press(self):
		print("on_x_press")
		self.pca.servo[0].angle = 0

	def on_x_release(self):
		print("on_x_release")

	def on_triangle_press(self):
		print("on_triangle_press")

	def on_triangle_release(self):
		print("on_triangle_release")

	def on_circle_press(self):
		print("on_circle_press")
		self.pca.servo[0].angle = 90

	def on_circle_release(self):
		print("on_circle_release")

	def on_square_press(self):
		print("on_square_press")

	def on_square_release(self):
		print("on_square_release")

	def on_L1_press(self):
		print("on_L1_press")

	def on_L1_release(self):
		print("on_L1_release")

	# Ranges from -32431 (barely pressed) to 32767 (fully pressed)
	def on_L2_press(self, value):
		print("on_L2_press: {}".format(value))

	# Deadzone from [-32432, -32767]
	def on_L2_release(self):
		print("on_L2_release")

	def on_R1_press(self):
		print("on_R1_press")

	def on_R1_release(self):
		print("on_R1_release")

	# Ranges from -32431 (barely pressed) to 32767 (fully pressed)
	def on_R2_press(self, value):
		print("on_R2_press: {}".format(value))

	# Deadzone from [-32432, -32767]
	def on_R2_release(self):
		print("on_R2_release")

	def on_up_arrow_press(self):
		print("on_up_arrow_press")

	def on_up_down_arrow_release(self):
		print("on_up_down_arrow_release")

	def on_down_arrow_press(self):
		print("on_down_arrow_press")

	def on_left_arrow_press(self):
		print("on_left_arrow_press")

	def on_left_right_arrow_release(self):
		print("on_left_right_arrow_release")

	def on_right_arrow_press(self):
		print("on_right_arrow_press")

	# ranges from -338 (barely tilted) to -32767 (fully pressed)
	def on_L3_up(self, value):
		print("on_L3_up: {}".format(value))

	# ranges from 337 (barely tilted) to 32767 (fully pressed)
	def on_L3_down(self, value):
		print("on_L3_down: {}".format(value))

	# ranges from -338 (barely tilted) to -32767 (fully pressed)
	def on_L3_left(self, value):
		print("on_L3_left: {}".format(value))

	# ranges from 337 (barely tilted) to 32767 (fully pressed)
	def on_L3_right(self, value):
		print("on_L3_right: {}".format(value))

	# Deadzone in range [-337, 336]
	def on_L3_y_at_rest(self):
		"""L3 joystick is at rest after the joystick was moved and let go off"""
		print("on_L3_y_at_rest")

	# Deadzone in range [-337, 336]
	def on_L3_x_at_rest(self):
		"""L3 joystick is at rest after the joystick was moved and let go off"""
		print("on_L3_x_at_rest")

	def on_L3_press(self):
		"""L3 joystick is clicked. This event is only detected when connecting without ds4drv"""
		print("on_L3_press")

	def on_L3_release(self):
		"""L3 joystick is released after the click. This event is only detected when connecting without ds4drv"""
		print("on_L3_release")

	# ranges from -338 (barely tilted) to -32767 (fully pressed)
	def on_R3_up(self, value):
		print("on_R3_up: {}".format(value))

	# ranges from 337 (barely tilted) to 32767 (fully pressed)
	def on_R3_down(self, value):
		print("on_R3_down: {}".format(value))

	# ranges from -338 (barely tilted) to -32767 (fully pressed)
	def on_R3_left(self, value):
		print("on_R3_left: {}".format(value))

	# ranges from 337 (barely tilted) to 32767 (fully pressed)
	def on_R3_right(self, value):
		print("on_R3_right: {}".format(value))

	# Deadzone in range [-337, 336]
	def on_R3_y_at_rest(self):
		"""R3 joystick is at rest after the joystick was moved and let go off"""
		print("on_R3_y_at_rest")

	# Deadzone in range [-337, 336]
	def on_R3_x_at_rest(self):
		"""R3 joystick is at rest after the joystick was moved and let go off"""
		print("on_R3_x_at_rest")

	def on_R3_press(self):
		"""R3 joystick is clicked. This event is only detected when connecting without ds4drv"""
		print("on_R3_press")

	def on_R3_release(self):
		"""R3 joystick is released after the click. This event is only detected when connecting without ds4drv"""
		print("on_R3_release")

	def on_options_press(self):
		print("on_options_press")

	def on_options_release(self):
		print("on_options_release")

	def on_share_press(self):
		"""this event is only detected when connecting without ds4drv"""
		print("on_share_press")

	def on_share_release(self):
		"""this event is only detected when connecting without ds4drv"""
		print("on_share_release")

	def on_playstation_button_press(self):
		"""this event is only detected when connecting without ds4drv"""
		print("on_playstation_button_press")

	def on_playstation_button_release(self):
		"""this event is only detected when connecting without ds4drv"""
		print("on_playstation_button_release")
