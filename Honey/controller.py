from pyPS4Controller.controller import Controller
from pcaBoard import PcaBoard
from time import sleep
from delegator import Delegator


class MyController(Controller):

	def __init__(self, stepperHandler, pcaBoard, delegator, interface, connecting_using_ds4drv):
		self.pca = pcaBoard
		self.stepperHandler = stepperHandler
		self.delegator = delegator
		print(interface)
		print(connecting_using_ds4drv)
		Controller.__init__(self, interface, connecting_using_ds4drv)
    
    # Toggle self.ARM_MODE
	def on_x_press(self):		
		print( "xpress")

	def on_x_release(self):
		print("on_x_release")

	# Toggle arm.SLOW_MODE
	def on_triangle_press(self):
		print("on_triangle_press")
		self.arm.toggleSlowMode()

	def on_triangle_release(self):
		print("on_triangle_release")

	def on_circle_press(self):
		print("on_circle_press")

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

	# Sets Claw closing speed
	# Ranges from -32431 (barely pressed) to 32767 (fully pressed)
	def on_L2_press(self, value):
		print("on_L2_press: {}".format(value))
		self.delegator.CloseClaw(value)

	# Resets Claw closing speed
	def on_L2_release(self):
		print("on_L2_release")
		self.delegator.OpenClaw(0)

	def on_R1_press(self):
		print("on_R1_press")

	def on_R1_release(self):
		print("on_R1_release")

	# Sets Claw opening speed
	# Ranges from -32431 (barely pressed) to 32767 (fully pressed)
	def on_R2_press(self, value):
		print("on_R2_press: {}".format(value))
		self.arm.openClaw(value)

	# Resets claw opening speed
	# Ranges from -32431 (barely pressed) to 32767 (fully pressed)
	def on_R2_release(self):
		print("on_R2_release")
		self.arm.openClaw(0)

	# Go forward at (max speed)/4
	def on_up_arrow_press(self):
		print("on_up_arrow_press")
		self.drive.goFront()

	# Reset forward speed
	def on_up_down_arrow_release(self):
		print("on_up_down_arrow_release")
		self.drive.setyL(0)

	# Go Backward at (max speed)/4
	def on_down_arrow_press(self):
		print("on_down_arrow_press")
		self.drive.goBack()

	# Go left at (max speed)/4
	def on_left_arrow_press(self):
		print("on_left_arrow_press")
		self.drive.goLeft()

	# Reset horizontal speed
	def on_left_right_arrow_release(self):
		print("on_left_right_arrow_release")
		self.drive.setxL(0)

	# Go right at (max speed)/4
	def on_right_arrow_press(self):
		print("on_right_arrow_press")
		self.drive.goRight()

	# Claw goes away from crane 
	# ranges from -338 (barely tilted) to -32767 (fully pressed)
	def on_L3_up(self, value):
		print("on_L3_up: {}".format(value))
		self.delegator.CraneAway(value)
		
		

	# Drive mode: -ve Vertical movement
	# Arm mode : Backward arm movement
	# ranges from 337 (barely tilted) to 32767 (fully pressed)
	def on_L3_down(self, value):
		print("on_L3_down: {}".format(value))
		self.delegator.CraneTowards(value)

	# Drive mode: -ve Horizontal Movement
	# Arm mode: ccw Arm Rotation
	# ranges from -338 (barely tilted) to -32767 (fully pressed)
	def on_L3_left(self, value):
		print("on_L3_left: {}".format(value))
		self.delegator.CraneCCW(value)


	# Drive mode: +ve Horizontal Movement
	# Arm mode: cw Arm Rotation
	# ranges from 337 (barely tilted) to 32767 (fully pressed)
	def on_L3_right(self, value):
		print("on_L3_right: {}".format(value))
		self.delegator.CraneClockwise(value)

	# Drive mode: 0 Vertical Movement
	# Arm mode: 0 forward/backward Movement
	# Deadzone in range [-337, 336]
	def on_L3_y_at_rest(self):
		"""L3 joystick is at rest after the joystick was moved and let go off"""
		print("on_L3_y_at_rest")
		self.delegator.CraneRestY()
		# self.pca.motorStop(15)
		# self.pca.setServoIncrement(1, 0)

	# Drive mode: 0 Horizontal Movement
	# Arm mode: 0 Arm Rotation
	# Deadzone in range [-337, 336]
	def on_L3_x_at_rest(self):
		"""L3 joystick is at rest after the joystick was moved and let go off"""
		print("on_L3_x_at_rest")
		self.delegator.CraneRestX()

	def on_L3_press(self):
		"""L3 joystick is clicked. This event is only detected when connecting without ds4drv"""
		print("on_L3_press")

	def on_L3_release(self):
		"""L3 joystick is released after the click. This event is only detected when connecting without ds4drv"""
		print("on_L3_release")

	# Arm Mode : Up Arm movement
	# ranges from -338 (barely tilted) to -32767 (fully pressed)
	def on_R3_up(self, value):
		print("on_R3_up: {}".format(value))
		self.delegator.RaiseClaw(value)

	# Arm Mode: Down Arm movement
	# ranges from 337 (barely tilted) to 32767 (fully pressed)
	def on_R3_down(self, value):
		print("on_R3_down: {}".format(value))
		self.delegator.LowerClaw(value)


	# Drive Mode: -ve Rotational Movement
	# ranges from -338 (barely tilted) to -32767 (fully pressed)
	def on_R3_left(self, value):
		print("on_R3_left: {}".format(value))

	# Drive mode: +ve Rotational Movement
	# ranges from 337 (barely tilted) to 32767 (fully pressed)
	def on_R3_right(self, value):
		print("on_R3_right: {}".format(value))

	# Arm mode: TODO
	# Deadzone in range [-337, 336]
	def on_R3_y_at_rest(self):
		"""R3 joystick is at rest after the joystick was moved and let go off"""
		print("on_R3_y_at_rest")
		self.delegator.ClawYRest()
	# Drive mode: 0 Rotational Movement
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
