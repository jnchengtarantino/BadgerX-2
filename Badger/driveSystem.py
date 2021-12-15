from math import ceil
import pcaBoard
# Left stick is going to be used for translation
# Right stick x is going to be used for rotation

# d-pad will go direct lines at 1/4 speed
# normal control and d-pad control will not work at the same time
CONTROLLER_SCALE = 2**15
MOTOR_SCALE = 2**16
class Drive:
    def __init__(self, pca, motorFL, motorFR, motorBL, motorBR):
        self.pca = pca
        self.motorFL = motorFL
        self.motorFR = motorFR
        self.motorBL = motorBL
        self.motorBR = motorBR
        self.xL = 0x0000    
        self.yL = 0x0000
        self.xR = 0x0000

    def stop(self):
        self.pca.motorStop(self.motorFL)
        self.pca.motorStop(self.motorFR)
        self.pca.motorStop(self.motorBL)
        self.pca.motorStop(self.motorBR)

    def run(self):
        x = self.xL *1.1/ CONTROLLER_SCALE # Additional multiplier to combat imperfect strafing
        y = self.yL / CONTROLLER_SCALE
        xr = -self.xR / CONTROLLER_SCALE
        denom = max( abs(x) + abs(y) + abs(xr), 1)
        frontLeftPower = ((y + x + xr) / denom)**3
        backLeftPower = ((y - x + xr) / denom)**3
        frontRightPower = ((y - x - xr) / denom)**3
        backRightPower  = ((y + x - xr) / denom)**3

        if frontLeftPower == 0:
            self.pca.motorNeutral(self.motorFL)
        elif frontLeftPower > 0:
            self.pca.motorForward(self.motorFL, abs(ceil(frontLeftPower * MOTOR_SCALE))-1)
        else:
            self.pca.motorReverse(self.motorFL, abs(ceil(frontLeftPower * MOTOR_SCALE))-1)
        
        if frontRightPower == 0:
            self.pca.motorNeutral(self.motorFR)
        elif frontRightPower > 0:
            self.pca.motorForward(self.motorFR, abs(ceil(frontRightPower * MOTOR_SCALE))-1)
        else:
            self.pca.motorReverse(self.motorFR, abs(ceil(frontRightPower * MOTOR_SCALE))-1)

        if backLeftPower == 0:
            self.pca.motorNeutral(self.motorBL)
        elif backLeftPower > 0:
            self.pca.motorForward(self.motorBL, abs(ceil(backLeftPower * MOTOR_SCALE))-1)
        else:
            self.pca.motorReverse(self.motorBL, abs(ceil(backLeftPower * MOTOR_SCALE))-1)
        
        if backRightPower == 0:
            self.pca.motorNeutral(self.motorBR)
        elif backRightPower > 0:
            self.pca.motorForward(self.motorBR, abs(ceil(backRightPower * MOTOR_SCALE))-1)
        else:
            self.pca.motorReverse(self.motorBR, abs(ceil(backRightPower * MOTOR_SCALE))-1)

    def setxL(self, val):
        self.xL = val
    
    def setyL(self, val):
        self.yL = val
    
    def setxR(self, val):
        self.xR = val

    def goFront(self):
        self.yL = -0.63 * CONTROLLER_SCALE
    
    def goBack(self):
        self.yL = 0.63 * CONTROLLER_SCALE
    
    def goRight(self):
        self.xL = 0.63 * CONTROLLER_SCALE
        
    def goLeft(self):
        self.xL = -0.63 * CONTROLLER_SCALE

    def step(self):
        if self.xL == 0 and self.yL == 0 and self.xR == 0:
            self.stop()
        else:
            self.run()

