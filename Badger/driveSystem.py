from math import ceil
import pcaBoard
# Left stick is going to be used for translation
# Right stick x is going to be used for rotation
CONTROLLER_SCALE = 2**15
MOTOR_SCALE = 2**16
class driveSystem:
    def __init__(self, pca, motorFL, motorFR, motorBL, motorBR):
        self.pca = pca
        self.motorFL = motorFL
        self.motorFR = motorFR
        self.motorBL = motorBL
        self.motorBR = motorBR
        self.xL = 0x0000    
        self.yL = 0x0000
        self.xR = 0x0000

    def stop(self, val):
        self.pca.motorStop(self.motorFL)
        self.pca.motorStop(self.motorFR)
        self.pca.motorStop(self.motorBL)
        self.pca.motorStop(self.motorBR)

    def run(self):
        x = self.xL / CONTROLLER_SCALE
        y = -self.yL / CONTROLLER_SCALE
        xr = self.xR / CONTROLLER_SCALE
        denom = max( abs(x) + abs(y) + abs(xr), 1)
        # TODO: look into exponential (cubed) scaling for ease of control
        frontLeftPower = (y + x + xr) / denom
        backLeftPower = (y - x + xr) / denom
        frontRightPower = (y - x - xr) / denom
        backRightPower  = (y + x - xr) / denom

        if frontLeftPower == 0:
            self.pca.motorNeutral(self.motorFL)
        elif frontLeftPower > 0:
            self.pca.motorForward(self.motorFL, abs(ceil(frontLeftPower * MOTOR_SCALE)))
        else:
            self.pca.motorReverse(self.motorFL, abs(ceil(frontLeftPower * MOTOR_SCALE)))
        
        if frontRightPower == 0:
            self.pca.motorNeutral(self.motorFR)
        elif frontRightPower > 0:
            self.pca.motorForward(self.motorFR, abs(ceil(frontRightPower * MOTOR_SCALE)))
        else:
            self.pca.motorReverse(self.motorFR, abs(ceil(frontRightPower * MOTOR_SCALE)))

        if backLeftPower == 0:
            self.pca.motorNeutral(self.motorBL)
        elif backLeftPower > 0:
            self.pca.motorForward(self.motorBL, abs(ceil(backLeftPower * MOTOR_SCALE)))
        else:
            self.pca.motorReverse(self.motorBL, abs(ceil(backLeftPower * MOTOR_SCALE)))
        
        if backRightPower == 0:
            self.pca.motorNeutral(self.motorBR)
        elif backRightPower > 0:
            self.pca.motorForward(self.motorBR, abs(ceil(backRightPower * MOTOR_SCALE)))
        else:
            self.pca.motorReverse(self.motorBR, abs(ceil(backRightPower * MOTOR_SCALE)))

    def setxL(self, val):
        self.xL = val
    
    def setyL(self, val):
        self.yL = val
    
    def setxR(self, val):
        self.xR = val

    def step(self):
        if self.xL == 0 and self.yL == 0 and self.xR == 0:
            self.stop()
        else:
            self.run()

