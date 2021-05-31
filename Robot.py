# pybrick imports
import math
try:
    from pybricks import ev3brick as brick
    from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                    InfraredSensor, UltrasonicSensor, GyroSensor)
    from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                    SoundFile, ImageFile, Align)
    from pybricks.tools import wait, print

    portA = Port.A
    portB = Port.B
    portC = Port.C
    portD = Port.D
    port4 = Port.S4
    stopBrake = Stop.BRAKE
    stopCoast = Stop.COAST
    SIM = False
except:
    print("Better to ask forgiveness then permission: ")
    print("We are running in simulation mode") 
    portA = "a"  
    portB = "b"
    portC = "c"
    portD = "d"
    port4 = "4"
    stopBrake = "BRAKE"
    stopCoast = "COAST"
    SIM = True
    class Motor:
        """
        fakes pybrick motor class.
        keeps track of angle and power!
        """
        def __init__(self, port):
            self.power = 0
            self.myAngle = 0
            
        def run(self, power):
            self.power = power

        def run_angle(self, power, degrees, brake, wait):
            self.power = power

        def reset_angle(self, newAngle):
            self.myAngle = newAngle

        def angle(self):
            """
            uses power t o keep track of angle!
            angle increses proportional to POWER
            """
            if self.power == 0.:
                return 0.
            else:
                self.myAngle = self.myAngle + (self.power / 100.0)
                return self.myAngle  

        def stop(self, stopType=None):
            # reset POWER to 0
            self.power = 0      

    class GyroSensor:

        def __init__(self, port):
            pass
        def angle(self):
            return 0


import math

# robot.py is where we keep our robot class
# the robot class is where we keep functions 
# to make the robot do simple actions.
# it also holds important variables about the bot

class Robot:

    def __init__(self):
        '''
        this is the construtor for our robot class. 
        This function gets called when a robot object is made from the robot class.
        '''
        # This is wich motor or sensor is plugged into a certain port.
        # 'The wiring' 
        self.leftMotor = Motor(portB)
        self.rightMotor = Motor(portC)
        self.leftTopMotor = Motor(portA)
        self.rightTopMotor = Motor(portD)
        self.gyro = GyroSensor(port4)

        # This sets the minimum speed
        # These are for when it ramps the speed, it will stop at this speed, insted of stalling
        self.minSpeed = 60.
        self.minSpinSpeed = 30.

    
        self.rampDownRatio = 0.5
        self.rampUpRatio = 0.2
        # This is the radius of the wheels in cms
        # This is so we can convert distance to wheel rotation(s) or the 
        # other way around
        self.wheelRadiusCm = 4.0

        # half of the distace between the wheels(in cms, obvously)
        # We need this in order to convert from degrees we want to spin the bot
        # to how far those wheels have to move.
        # could be 6, depending on how you measure it
        self.driveTrainRadiusCm = 5.65

        # this is the gain we use when going straight with the gyro sensor
        # better then 0.7
        self.gyroGain = 2.5
         
        # Lets give our bot MEMORY!
        self.distaceTraveledCms = 0
        self.currentPosition = (0, 0)
        self.currentRotation = 0
        self.oldPositions = []

    def updateMemory(self, distanceCms, rotation):
        self.distaceTraveledCms = self.distaceTraveledCms + distanceCms
        # update ANGLE!
        self.currentRotation = self.currentRotation + rotation

        # degres 2 radians
        radians = self.currentRotation * ((2 * math.pi) / 360)
        x = distanceCms * math.cos(radians)
        y = distanceCms * math.sin(radians)

        # now cclculate new current position
        newX = self.currentPosition[0] + x
        newY = self.currentPosition[1] + y
        self.currentPosition = (newX, newY)
        # Rember position
        self.oldPositions.append(self.currentPosition)


    def runTopMotors(self, speed, rotation_angle):
        "Turns on top motors in opposite directions for as many degrees as you tell it"
        self.leftTopMotor.run_angle(-speed,rotation_angle,stopCoast,False)
        self.rightTopMotor.run_angle(speed,rotation_angle,stopCoast,True)

    def driveForward(self, speed, rotation_angle):
        "Turns on bottom motors in same direction to dirve foward for degrees you tell it"
        # don't wait here, so that both motors can turn at the same time
        self.leftMotor.run_angle(speed,rotation_angle,stopCoast,False)
        # but wait here!
        self.rightMotor.run_angle(speed,rotation_angle,stopCoast,True)
        # Update the memory
        distanceCms = self.degrees2cms(rotation_angle)
        self.updateMemory(distanceCms, 0)


    def driveMotors(self, rightSpeed, leftSpeed, rotation_angle, coast=True):
        "Turns on bottom motors in same direction to dirve foward for degrees you tell it"
        if coast:
            brake = stopCoast
        else:
            brake = stopBrake    
        self.leftMotor.reset_angle(0)
        self.rightMotor.reset_angle(0)
        # don't wait here, so that both motors can turn at the same time
        self.leftMotor.run_angle(leftSpeed,rotation_angle,brake,False)
        # but wait here!
        self.rightMotor.run_angle(rightSpeed,rotation_angle,brake,True)

    def moveForTime(self, rightPower, leftPower, msecs):
        self.leftMotor.run_time(leftPower, msecs, Stop.COAST, False)
        self.rightMotor.run_time(rightPower, msecs, Stop.COAST, True)


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

    def degrees2cms(self, degrees):
        circumfrence = 2*3.14*self.wheelRadiusCm
        conversion = circumfrence/360.0
        cms = degrees * conversion
        return cms

    def driveForwardCms(self, speed, cms):
        "drives foward how many centimeters you tell it"
        #convert cm to degrees
        degrees = self.cms2degrees(cms)
        self.driveForward(speed, degrees)
    
    def driveMotorsCms(self, rightSpeed, leftSpeed, cms, coast=True):
        "drives foward how many centimeters you tell it"
        #convert cm to degrees
        degrees = self.cms2degrees(cms)
        self.driveMotors(rightSpeed, leftSpeed, degrees, coast=coast)


    def driveStraightCms(self, speed, cms, useGYRO = True):
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
            if useGYRO:
                correction = error * self.gyroGain
            else:
                correction = 0

            # ramp down the speed as we get close to our destination!
            ratio = rotation_angle / degreesTarget
            # if ratio < self.rampDownRatio:
            #     # go at a constant speed
            #     rampSpeed = speed
            # else:
            #     # RAMP down speed!
            #     scale = (1 - ratio) / (1 - self.rampDownRatio)
            #     rampSpeed = speed * scale

            if ratio > self.rampUpRatio and ratio < self.rampDownRatio:
                # go at a constant speed
               rampSpeed = speed
               
            else:
                if ratio > self.rampDownRatio:
                    # RAMP down speed!
                    scale = (1 - ratio) / (1 - self.rampDownRatio)
                    rampSpeed = speed * scale
                else:
                    # ramp UP!!!
                    rampSpeed = speed * (ratio / self.rampUpRatio)

            # make sure we never slow down so much that the robot
            # can't make it's destination    
            rampSpeed = max(rampSpeed, self.minSpeed)
            print(rampSpeed)

            self.rightMotor.run(rampSpeed + correction)
            self.leftMotor.run(rampSpeed - correction)
            rotation_angle = self.rightMotor.angle()
        self.rightMotor.stop()
        self.leftMotor.stop()

        self.updateMemory(cms, 0)


    def spinRightToAngle(self, speed, targetAngle):
        "spins right until gyro reads the angle that you tell it"
        # compensate for overshoot?
        # targetAngle = targetAngle + 1
        gyroAngle = self.gyro.angle()
        startingAngle = gyroAngle
        # If not running on bot pretend that we are at the target angle
        if SIM:
            gyroAngle = targetAngle
        while gyroAngle < targetAngle:
            gyroAngle = self.gyro.angle()
            # this makes it so that you start going fast in your turn
            # but then as you get closer to your angle, you slow down
            scale = (gyroAngle - startingAngle) / (targetAngle - startingAngle)
            rampSpeed = speed * (1 - scale)
            # make sure speed does not go to zero
            rampSpeed = max(rampSpeed, self.minSpinSpeed)
            self.rightMotor.run(-rampSpeed)
            self.leftMotor.run(rampSpeed)
            print(scale)
            print(gyroAngle)
        self.rightMotor.stop(stopBrake)
        self.leftMotor.stop(stopBrake)
        self.updateMemory(0, targetAngle)
        
    def spinLeftToAngle(self, speed, targetAngle):
        "spins left until gyro reads the angle that you tell it"
        # compensate for overshoot?
        # targetAngle = targetAngle - 1
        gyroAngle = self.gyro.angle()
        startingAngle = gyroAngle
        # If not running on bot pretend that we are at the target angle
        if SIM:
            gyroAngle = targetAngle
        while gyroAngle > targetAngle:
            gyroAngle = self.gyro.angle()
            scale = (gyroAngle - startingAngle) / (targetAngle - startingAngle)
            rampSpeed = speed * (1 - scale)
            rampSpeed = max(rampSpeed, self.minSpinSpeed)
            self.rightMotor.run(rampSpeed)
            self.leftMotor.run(-rampSpeed)
            print(scale)
            print(gyroAngle)
        self.rightMotor.stop(Stop.BRAKE)
        self.leftMotor.stop(Stop.BRAKE)
        self.updateMemory(0, targetAngle)

    def gyroDriftCheck(self):
        self.gyro.reset_angle(0)
        # get all the buttons that are currently pressed
        leftButtonPressed = False
        while not leftButtonPressed:
            btns = brick.buttons()
            if len(btns) == 1:
                btn = btns[0]
                leftButtonPressed = btn == Button.LEFT
            angleDeGyro = self.gyro.angle()
            brick.display.clear()
            brick.display.text("Gyro Value: ")
            for i in range(3):
                brick.display.text(angleDeGyro)
            wait(50)
        wait(1000)
        leftButtonPressed = False
        while not leftButtonPressed:
            btns = brick.buttons()
            if len(btns) == 1:
                btn = btns[0]
                leftButtonPressed = btn == Button.LEFT
            # angleDeGyro = self.gyro.angle()
            brick.display.clear()
            for i in range(3):
                brick.display.text("Hardware Calibrate?")
            wait(50)
        brick.display.clear()
        # give user chance to get finger off button
        wait(2000)

    def SpinLeftAngularDistance(self, power, angle):
        #convert degrees to distance
        conversion = (2 * math.pi * self.driveTrainRadiusCm) / 360.0
        distance = angle * conversion
        self.driveMotorsCms(power, -power, distance, coast = False)
        self.updateMemory(0, angle)

    def SpinRightAngularDistance(self, power, angle):
        #convert degrees to distance
        conversion = (2 * math.pi * self.driveTrainRadiusCm) / 360.0
        distance = angle * conversion
        self.driveMotorsCms(-power, power, distance, coast = False)
        self.updateMemory(0, -angle)