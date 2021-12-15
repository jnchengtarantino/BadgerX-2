import RPi.GPIO as GPIO
from time import sleep

##dropper motor
##tensionner motor
##each claw: 1 motor 1 servo
##crane rotation: stepper
##claw sliding: stepper
##motor scaling: 2^16
##controller: 2^15


class Delegator:

    def __init__(self, pca, DropperMotor, TensionnerMotor, Claw1Motor, Claw1Servo, RotationStepper, SlidingStepper):
        self.pca = pca
        self.DropperMotor = DropperMotor
        self.TensionnerMotor = TensionnerMotor
        self.Claw1Motor = Claw1Motor
        self.Claw1Servo = Claw1Servo
        self.RotationStepper = RotationStepper
        self.SlidingStepper = SlidingStepper
        self.xL = 0x0000
        self.yL = 0x0000
        self.xR = 0x0000

    def CraneAway(val):
        return

    def CraneRestY():
        return

    def CraneTowards(val):
        return

    def CraneClockwise(val):
        return

    def CraneCCW(val):
        return
    
    def CraneRestX():
        return

    def LowerClaw(val):
        return

    def RaiseClaw(val):
        return

    def ClawYRest():
        return

    def CloseClaw(val):
        return

    def OpenClaw(val):
        return

    def CraneRest():
        return



    



        