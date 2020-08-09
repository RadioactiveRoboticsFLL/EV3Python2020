# pybrick imports
from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import wait, print


def driveForward(speed, rotation_angle):
    leftMotor = Motor(Port.B)
    rightMotor = Motor(Port.C)
    leftMotor.run_angle(speed,rotation_angle,Stop.COAST,False)
    rightMotor.run_angle(speed,rotation_angle,Stop.COAST,True)
    
def spinRight(speed, rotation_angle):
    leftMotor = Motor(Port.B)
    rightMotor = Motor(Port.C)
    leftMotor.run_angle(speed,rotation_angle,Stop.COAST,False)
    rightMotor.run_angle(-speed,rotation_angle,Stop.COAST,True)
    
def spinLeft(speed, rotation_angle):
    leftMotor = Motor(Port.B)
    rightMotor = Motor(Port.C)
    leftMotor.run_angle(-speed,rotation_angle,Stop.COAST,False)
    rightMotor.run_angle(speed,rotation_angle,Stop.COAST,True)