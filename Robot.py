# pybrick imports
from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import wait, print

class Robot:

    def __init__(self):
        self.leftMotor = Motor(Port.B)
        self.rightMotor = Motor(Port.C)
        self.leftTopMotor = Motor(Port.A)
        self.rightTopMotor = Motor(Port.D)
        self.minSpeed = 30.
        self.gyro = GyroSensor(Port.S4)
        self.wheelRadiusCm = 4.0
        self.gyroGain = 0.7

    def runTopMotors(self, speed, rotation_angle):
        self.leftTopMotor.run_angle(-speed,rotation_angle,Stop.COAST,False)
        self.rightTopMotor.run_angle(speed,rotation_angle,Stop.COAST,True)

    def driveForward(self, speed, rotation_angle):
        self.leftMotor.run_angle(speed,rotation_angle,Stop.COAST,False)
        self.rightMotor.run_angle(speed,rotation_angle,Stop.COAST,True)
    
    def spinRight(self, speed, rotation_angle):
        self.leftMotor.run_angle(speed,rotation_angle,Stop.COAST,False)
        self.rightMotor.run_angle(-speed,rotation_angle,Stop.COAST,True)
        
    def spinLeft(self, speed, rotation_angle):
        self.leftMotor.run_angle(-speed,rotation_angle,Stop.COAST,False)
        self.rightMotor.run_angle(speed,rotation_angle,Stop.COAST,True)
    
    def cms2degrees(self, cms):
        circumfrence = 2*3.14*self.wheelRadiusCm
        conversion = 360.0/circumfrence
        degrees = cms*conversion
        return degrees

    def driveForwardCms(self, speed, cms):
        #convert cm to degrees
        degrees = self.cms2degrees(cms)
        self.driveForward(speed, degrees)
    
    def driveStraightCms(self, speed, cms):
        degreesTarget = self.cms2degrees(cms)
        intialGyroAngle = self.gyro.angle()
        rotation_angle = self.rightMotor.angle()
        while rotation_angle < degreesTarget:
            gyroAngle = self.gyro.angle()
            error = gyroAngle - intialGyroAngle
            correction = error * self.gyroGain
            self.rightMotor.run(speed + correction)
            self.leftMotor.run(speed - correction)
            rotation_angle = self.rightMotor.angle()
        self.rightMotor.stop()
        self.leftMotor.stop()

    def spinRightToAngle(self, speed, targetAngle):
        gyroAngle = self.gyro.angle()
        startingAngle = gyroAngle
        while gyroAngle < targetAngle:
            gyroAngle = self.gyro.angle()
            scale = (gyroAngle - startingAngle) / (targetAngle - startingAngle)
            rampSpeed = speed * (1 - scale)
            rampSpeed = max(rampSpeed, self.minSpeed)
            self.rightMotor.run(-rampSpeed)
            self.leftMotor.run(rampSpeed)
            print(scale)
            print(gyroAngle)
        self.rightMotor.stop(Stop.BRAKE)
        self.leftMotor.stop(Stop.BRAKE)

    def spinLeftToAngle(self, speed, targetAngle):
        gyroAngle = self.gyro.angle()
        startingAngle = gyroAngle
        while gyroAngle > targetAngle:
            gyroAngle = self.gyro.angle()
            scale = (gyroAngle - startingAngle) / (targetAngle - startingAngle)
            rampSpeed = speed * (1 - scale)
            rampSpeed = max(rampSpeed, self.minSpeed)
            self.rightMotor.run(rampSpeed)
            self.leftMotor.run(-rampSpeed)
            print(scale)
            print(gyroAngle)
        self.rightMotor.stop(Stop.BRAKE)
        self.leftMotor.stop(Stop.BRAKE)