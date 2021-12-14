import pcaBoard

CONTROLLER_SCALE = 2**15
FAST_SCALE = 1/(2**12)
SLOW_SCALE = 1/(2**14)
CLAW_SCALE = 1/(2**12)

class Arm:
    
    # rotMotor does Base Rotation:
    # fbServo generally does forward/backward movement
    # udServo generally does up/down movement
    # clawServo opens/closes the claw
    def __init__(self,pca,rotServo,fbServo, udServo, clawServo):
        self.pca = pca
        self.rotServo = rotServo
        self.fbServo = fbServo
        self.udServo = udServo
        self.clawServo = clawServo
        self.SLOW_MODE = False
        self.pca.setServoScale(self.rotServo, CLAW_SCALE)

    def toggleSlowMode(self):
        self.SLOW_MODE = not self.SLOW_MODE
        scale = SLOW_SCALE if self.SLOW_MODE else FAST_SCALE
        self.pca.setServoScale(self.rotServo, scale)
        self.pca.setServoScale(self.fbServo, scale)
        self.pca.setServoScale(self.udServo, scale)

    def rotateArm(self, val):
        val = CONTROLLER_SCALE * (val / CONTROLLER_SCALE)**3
        self.pca.setServoIncrement(self.rotServo, val)

    def moveFB(self, val):
        val = CONTROLLER_SCALE * (val / CONTROLLER_SCALE)**3
        self.pca.setServoIncrement(self.fbServo, val)

    def moveUD(self, val):
        val = CONTROLLER_SCALE * (val / CONTROLLER_SCALE)**3
        self.pca.setServoIncrement(self.udServo, val)

    def openClaw(self, val):
        val = CONTROLLER_SCALE * ( (val + CONTROLLER_SCALE) / (2 * CONTROLLER_SCALE) )**3
        self.pca.setServoIncrement(self.clawServo, val)

    def closeClaw(self, val):
        val = -CONTROLLER_SCALE * ( (val + CONTROLLER_SCALE) / (2 * CONTROLLER_SCALE) )**3
        self.pca.setServoIncrement(self.clawServo, val)