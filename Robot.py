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
        self.minSpeed = 60.
        self.gyro = GyroSensor(Port.S4)
        self.wheelRadiusCm = 4.0
        self.gyroGain = 0.7
        self.rampDownRatio = 0.5

    def runTopMotors(self, speed, rotation_angle):
        "Turns on top motors in opposite directions for as many degrees as you tell it"
        self.leftTopMotor.run_angle(-speed,rotation_angle,Stop.COAST,False)
        self.rightTopMotor.run_angle(speed,rotation_angle,Stop.COAST,True)

    def driveForward(self, speed, rotation_angle):
        "Turns on bottom motors in same direction to dirve foward for degrees you tell it"
        # don't wait here, so that both motors can turn at the same time
        self.leftMotor.run_angle(speed,rotation_angle,Stop.COAST,False)
        # but wait here!
        self.rightMotor.run_angle(speed,rotation_angle,Stop.COAST,True)
    
    def spinRight(self, speed, rotation_angle):
        "Just like drive forward, except right motor goes backward"
        self.leftMotor.run_angle(speed,rotation_angle,Stop.COAST,False)
        self.rightMotor.run_angle(-speed,rotation_angle,Stop.COAST,True)
        
    def spinLeft(self, speed, rotation_angle):
        "Just like drive forward, except left motor goes backward"
        self.leftMotor.run_angle(-speed,rotation_angle,Stop.COAST,False)
        self.rightMotor.run_angle(speed,rotation_angle,Stop.COAST,True)
    
    def cms2degrees(self, cms):
        "converts centimeters to rotation degrees of the wheels"
        circumfrence = 2*3.14*self.wheelRadiusCm
        conversion = 360.0/circumfrence
        degrees = cms*conversion
        return degrees

    def driveForwardCms(self, speed, cms):
        "drives foward how many centimeters you tell it"
        #convert cm to degrees
        degrees = self.cms2degrees(cms)
        self.driveForward(speed, degrees)
    
    def driveStraightCms(self, speed, cms):
        "drives straight with gyro sensor, however many cms you tell it"
        # resets both motor angles
        self.leftMotor.reset_angle(0)
        self.rightMotor.reset_angle(0)
        degreesTarget = self.cms2degrees(cms)
        intialGyroAngle = self.gyro.angle()
        rotation_angle = self.rightMotor.angle()
        # TBF: get the robot to slow down as it
        # gets close to it's destination
        while rotation_angle < degreesTarget:
            # get the latest value that the gyro sensor is reading
            gyroAngle = self.gyro.angle()
            error = gyroAngle - intialGyroAngle
            # this is the correction to each motor to 
            # keep the robot going straight
            correction = error * self.gyroGain

            # ramp down the speed as we get close to our destination!
            ratio = rotation_angle / degreesTarget
            if ratio < self.rampDownRatio:
                # go at a constant speed
                rampSpeed = speed
            else:
                # RAMP down speed!
                scale = (1 - ratio) / (1 - self.rampDownRatio)
                rampSpeed = speed * scale

            # make sure we never slow down so much that the robot
            # can't make it's destination    
            rampSpeed = max(rampSpeed, self.minSpeed)
            #print(rampSeed)

            self.rightMotor.run(rampSpeed + correction)
            self.leftMotor.run(rampSpeed - correction)
            rotation_angle = self.rightMotor.angle()
        self.rightMotor.stop()
        self.leftMotor.stop()

    def spinRightToAngle(self, speed, targetAngle):
        "spins right until gyro reads the angle that you tell it"
        gyroAngle = self.gyro.angle()
        startingAngle = gyroAngle
        while gyroAngle < targetAngle:
            gyroAngle = self.gyro.angle()
            # this makes it so that you start going fast in your turn
            # but then as you get closer to your angle, you slow down
            scale = (gyroAngle - startingAngle) / (targetAngle - startingAngle)
            rampSpeed = speed * (1 - scale)
            rampSpeed = max(rampSpeed, self.minSpeed)
            self.rightMotor.run(-rampSpeed)
            self.leftMotor.run(rampSpeed)
            print(scale)
            print(gyroAngle)
        self.rightMotor.stop(Stop.BRAKE)
        self.leftMotor.stop(Stop.BRAKE)
        brick.display.text("last angle:")
        brick.display.text(gyroAngle)
        
    def spinLeftToAngle(self, speed, targetAngle):
        "spins left until gyro reads the angle that you tell it"
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
        brick.display.text("last angle:")
        brick.display.text(gyroAngle)