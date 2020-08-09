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
        self.wheelRadiusCm = 4.0

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