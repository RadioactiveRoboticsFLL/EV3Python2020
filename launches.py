# :-)
from pybricks import ev3brick as brick
from pybricks.tools import wait, print
from Robot import Robot

from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.robotics import DriveBase

def pullUpBar():
    r = Robot()
    r.driveStraightCms(250, 106-21)
    brick.sound.beep()
    r.spinRightToAngle(150, 87.5)
    # r.driveForwardCms(500, 106-11)
    # r.spinRight(250, 120)
    wait(1000)
    #go backwards
    r.driveForwardCms(-200, 28)
    # pull up!
    r.runTopMotors(-500, 9*360)

def bocciBench():
    r = Robot()
    r.driveStraightCms(500, 50-5.5)
    r.spinLeftToAngle(150, -90)
    r.driveStraightCms(500, 94-15.5)
    # we have arrived at the bocci ball
    r.rightTopMotor.run_time(500, 1000)
    # r.rightTopMotor.run_time(-500, 1000)


def treadmill():
    r = Robot()
    
    # Benched!!
    # Use if we have time
    # maybe not... :-( too many penlties

    # This will get us on top, but we want to stop.
    # doesn't go straight when it's too fast
    # r.driveStraightCms(600, 172)
    r.driveStraightCms(200, 172 - 25)
    r.driveForwardCms(600, 10)
    #onTopOfTreadmill!!!!!!!!
    #turn on one (right) motor
    r.rightMotor.run_time(256, 5000)
    # Get off!!!
    r.driveForwardCms(-600, 25)
    # Straiten out!!
    gyroAngle = r.gyro.angle()
    if gyroAngle > 0:
        r.spinLeftToAngle(30, 0)
    else:
        r.spinRightToAngle(30, 0)
    # To Home!!!!!
    # r.driveStraightCms(-650, 150) this does not work.
    # to go backwards, just give it neg. power
    r.driveForwardCms(-150, 75)
    r.driveForwardCms(-999999999999999999999999999, 75)
    # BOOM!!!!!!!!!

def Bocci():
    # This dumps Sabastion and heath units at bench.
    r = Robot()
    r.driveStraightCms(500, 30)
    #DUMP!! Sabastion and the health units.
    r.runTopMotors(500, 90)
    # r.driveStraightCms(200, 5)
    r.spinLeftToAngle(150, -90)
    r.driveStraightCms(500, 40)

def benchBall():
    # this only works with Florian's Ev3 bot
    #The bot should be alligned one square to ye right and toching ye olde wall.
    r = Robot()
    # approach bench
    r.driveStraightCms(500, 37)
    #knock down ye olde bench by turning
    r.spinLeftToAngle(100, -55)
    r.driveStraightCms(100, 6.5)
    #We should be lined up with ye olde bench
    r.spinRightToAngle(100, 3)
    r.driveStraightCms(100, 7.5)
    #Wham!! Ye olde bench should be knocked down.
    r.spinLeftToAngle(500, -45)
    r.spinRightToAngle(100, 3)
    #Aproch the bench and drop cubes!
    r.driveStraightCms(100, 4)
    r.leftTopMotor.run_angle(100,180,Stop.COAST,False)
    

def testTurn():
    r = Robot()
    r.spinRightToAngle(150, 90)

# def testThis():
    # pass

# def florianBenchAndBasketball():
def testThis():
    # ev3 = EV3Brick()

    # Initialize the motors.
    left_motor = Motor(Port.B)
    right_motor = Motor(Port.C)
    medium_motor = Motor(Port.A)
    Ball_dropper = Motor(Port.D)

    robot = DriveBase(left_motor, right_motor, wheel_diameter=82, axle_track=108)
    # ev3.speaker.beep()
    #sys.exit()

    # BLACK=10
    # WHITE=100
    # threshold=(BLACK+WHITE)/2.0
    # # mm/sec
    # DRIVE_SPEED=200.0
    # # factor, adjust
    # GAIN=1.4
    # # seconds milliseconds, adjust
    # STEP=100

    # degrees/sec
    turn_rate = 0

    #robot.drive_time(DRIVE_SPEED,0,1000)
    #robot.drive_time(DRIVE_SPEED,-145,500)
    #robot.drive_time(DRIVE_SPEED,0,3500)

    #this Was the knocking down misi=sion for the blue and red cube
    #robot.drive_time(250,0,2170)
    #robot.drive_time(0,-56,1000)
    #robot.drive_time(200,0,1300)
    #medium_motor.reset_angle(0)
    #medium_motor.run_angle(100, -30, Stop.COAST, True)
    #medium_motor.run_angle(100, +80, Stop.COAST, True)

    robot.drive_time(250,0,1300)
    robot.drive_time(0, -20,1000)
    robot.drive_time(200,0,400)
    robot.drive_time(0,45,1000)
    robot.drive_time(200,0,750)
    robot.drive_time(0,-43,1000)
    robot.drive_time(0,43,1000)
    robot.drive_time(-250,0,300)
    robot.drive_time(0,-20,1000)
    #medium_motor.run_angle(100000, -105, Stop.COAST, True)

    robot.drive_time(-200,0,3300)
    #medium_motor.run_angle(400, 105, Stop.COAST, True)
    robot.drive_time(250,0,1000)
    robot.drive_time(0,90,1000)
    robot.drive_time(250,0,2100)
    robot.drive_time(0,-90,1000)
    robot.drive_time(250,0,1700)
    robot.drive_time(0,-50,1000)
    robot.drive_time(250,0,900)

    #robot.drive_time(0,90,1000)
    #robot.drive_time(250,0,1500)
    Ball_dropper.run_angle(300, -180, Stop.COAST, True)
    Ball_dropper.run_angle(300, 180, Stop.COAST, True)
    robot.drive_time(-250,0,750)
    robot.drive_time(0,-23,1000)
    robot.drive_time(250,0,465)
    medium_motor.run_angle(100, -200,Stop.COAST, True)
    robot.drive_time(-250,0,1000)  
      
def benchBall():
    r = Robot()
    r.driveStraightCms(500, 35)
    r.spinLeftToAngle(100, -55)
    r.driveStraightCms(100, 5)
    r.spinRightToAngle(100, 35)

# bocci mission (M08)
# put jig in normal spot, then put triangle
# jig in that jig.  Back of robot is against
# triangle jig.
def bocciPlainBocci():
    r = Robot()
    r.driveStraightCms(500, 100)
    # dump blocks!
    r.runTopMotors(500, 45)
    #go backwards to base
    r.driveForwardCms(-500, 120)
    # this will get us off the mat
    # r.spinRight(350, 35)
    # r.driveForwardCms(-500, 60)

# M01 & M04
#Set it up with the jig and point the robot up and you also need 
# the attachment to dump the innovation and health units.
def innovationbench():
    r = Robot()
    r.driveStraightCms(500, 37)
    r.spinRightToAngle(100,37)
    # dump stuff
    r.runTopMotors(500, 360)
    # knock down bench
    # r.spinLeftToAngle(250, -19)
    r.moveForTime(200, -200, 1000)
    # go home
    r.spinRightToAngle(500, 15)
    r.driveForwardCms(-500,35)

# start this against the wall
# goes up to step counter, then pushes it SLOW!    
# and does NOT bump it!
def stepCOUNTER():
    r = Robot()
    r.driveStraightCms(450, 85)
    r.driveForwardCms(25, 19)
    # REVERSE!!!!!!
    r.driveForwardCms(-500, 120)


# This is for mission 8
# set up the bot w/ ye tri-angle jig
def bocciOtherTable():
    r = Robot()
    r.driveStraightCms(300, 47.5)
    r.spinLeftToAngle(50, -44)
    r.driveStraightCms(300, 31.5)
    # knock the ball on the other table!!
    r.runTopMotors(100, 50)
    r.runTopMotors(-100, 50)
    #Go back home!!
    r.driveForwardCms(-500, 40)
    r.spinLeftToAngle(400, -130)
    r.driveForwardCms(500, 70)
    # Back home!!




# does step counter away from wall,
# so we can turn into pullup bar
def stepCOUNTER2():
    r = Robot()
    r.driveStraightCms(450, 85)
    r.driveForwardCms(25, 19)
    # r.driveForwardCms(-500, 120)
    r.driveForwardCms(-100, 7)
    r.spinLeftToAngle(100, -90)
    r.driveStraightCms(700, 50)


def DROPcube(robot):
    # Uses the CUBE DROPPER atachment
    # DROP CUBE!!!!!!!!
    robot.rightTopMotor.run_angle(-100, 190, Stop.BRAKE, True)
    # Wait for cube to fall down maggazine and detachable barrel
    wait(2000)    
    # Reset CUBE DROPPER
    robot.rightTopMotor.run_angle(100, 190, Stop.BRAKE, True)




# does step counter against the wall, like before,
# but then backs off the wall so we can turn into pullup bar
def blueTriangle():
    r = Robot()

    # test
    # r.runTopMotors(200, 120)
    # return
    
    # r.driveStraightCms(450, 85)
    # hug the wall on the right
    r.driveMotorsCms(450, 470, 81)
    # r.driveForwardCms(25, 19)

    # this should push for time, not distance,
    # and continue pushing against the wall too
    r.moveForTime(25, 27, 12000)
    # r.driveForwardCms(-500, 120)
    # r.driveForwardCms(-100, 7)
    # r.spinLeftToAngle(100, -90)
    # r.driveStraightCms(700, 50)

    # turn backwards
    r.moveForTime(-200, -100, 2000)
    # straighetn out again
    r.spinLeftToAngle(100, 0)
    # get lined up for pull up bar
    r.driveStraightCms(100, 5)
    # and point towards pull up bar
    r.spinLeftToAngle(100, -90)
    # We are trying to get the arm out of the way
    r.leftTopMotor.run_time(100, 2000, Stop.COAST, True)
    # We are going backwards to get strait with the wall.
    r.moveForTime(-400, -400, 3000)
    # go under pullupbar
    r.driveStraightCms(200, 53 + 7)

    # turn 90 degeres
    r.spinLeftToAngle(100, -180)
    # go foward up to slide
    r.driveForwardCms(100, 25)
    # turn so parallel with slide
    r.spinLeftToAngle(100, -225)

    # extend the arm to shove the dude down the slide
    # r.runTopMotors(200, 120)
    r.leftTopMotor.run_angle(-50, 73, Stop.BRAKE, True)
    r.leftTopMotor.run(1)
    brick.sound.beep()
    r.driveForwardCms(100, 13)
    brick.sound.beep()
    
    r.leftTopMotor.run_time(-100, 2000, Stop.COAST, True)
    brick.sound.beep()

    # self.leftMotor.run_time(leftPower, msecs, Stop.COAST, False)

    # GO HOME!!!!
    r.driveForwardCms(900, 100)

def cubesInTheBench():
    r = Robot()
    # the robot starts with the triangle jig
    r.driveStraightCms(300, 40)
    # Spin Left until Parralel with BENCH
    r.spinLeftToAngle(100, -120)
    # DrIve unTIL CUBE DROPPER is OvER fiRSt TARget
    r.driveStraightCms(300, 25)
    for dropNumber in range(4):
        # DROP CUBE!!!!!!!!
        DROPcube(r)
        # move to next TARget
        r.driveStraightCms(200, 5)
    # Time to GO HOME!!!!
    r.driveForwardCms(700, 50)












# ;-P
# I was here!!
# Hello future person