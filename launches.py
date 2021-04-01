
from pybricks import ev3brick as brick
from pybricks.tools import wait, print
from Robot import Robot

from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.robotics import DriveBase

# launches.py is where we keep functions to do missions

# This launch gets the bot haning on the pull-up bar
# -------------
# Set up the bot with the right attachment. Use the main jig and the
# jig attachment that is designed for pull-up bar
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


# This launch does the treadmill
# =========
# Set it up with the main jig and the yellow jig attachment
# (The bot should be pointed twords the treadmill)
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
    r.driveForwardCms(-1000, 75)
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
    r.driveForwardCms(-900, 35)

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
    # when we used the big jig
    # r.driveStraightCms(500, 47.5)
    # r.spinLeftToAngle(50, -44)
    # r.driveStraightCms(500, 32)

    r.driveStraightCms(500, 47.5 + 10)
    r.spinLeftToAngle(50, -43) # in theory, 45?
    r.driveStraightCms(500, 32 - 1)
    brick.sound.beep()
    # now push against the wall so we know where we are
    r.moveForTime(50, 50, 3000)
    # then back up just the right amount
    # r.driveForwardCms(-150, 5)

    # knock the ball on the other table!!
    r.runTopMotors(500, 50)
    # r.runTopMotors(-500, 50)
    #Go back home!!
    # r.driveForwardCms(-500, 40 )
    # r.spinLeftToAngle(400, -150)
    # r.driveForwardCms(800, 90)
    power = 500
    r.driveMotorsCms(-power - 135, -power, 125)
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
    # The BEST function for the BEST attachment.
    # Uses the CUBE DROPPER atachment
    # DROP CUBE!!!!!!!!
    robot.leftTopMotor.run_angle(-100, 95, Stop.BRAKE, True)
    # Wait for cube to fall down maggazine and detachable barrel
    wait(500)    
    # Reset CUBE DROPPER
    robot.leftTopMotor.run_angle(100, 95, Stop.BRAKE, True)



# Does the stepcounter, drives under the pull-up bar, 
# knocks the dude off the slide, and brings him home
# ----------
# Set it up with the back of the bot against the thick black line,
# the right side of the bot should be touching the wall
def blueTriangle():
    r = Robot()
    # test
    # r.runTopMotors(200, 120)
    # return
    # r.driveStraightCms(450, 85)
    # hug the wall on the right
    power = 600
    r.driveMotorsCms(power, power + 20, 81)
    # r.driveForwardCms(25, 19)
    # this should push for time, not distance,
    # and continue pushing against the wall too
    r.moveForTime(25, 27, 10000)
    # r.driveForwardCms(-500, 120)
    # r.driveForwardCms(-100, 7)
    # r.spinLeftToAngle(100, -90)
    # r.driveStraightCms(700, 50)
    # turn backwards
    power = 200
    r.moveForTime(-power, -(power - 100), 2000)
    # straighetn out again
    r.spinLeftToAngle(200, 0)
    # get lined up for pull up bar
    r.driveStraightCms(200, 5)
    # and point towards pull up bar
    r.spinLeftToAngle(200, -90)
    # We are trying to get the arm out of the way
    r.leftTopMotor.run_time(500, 500, Stop.COAST, True)
    # We are going backwards to get strait with the wall.
    r.moveForTime(-200, -200, 1000)
    r.gyro.reset_angle(-90)
    # go under pullupbar
    r.driveStraightCms(500, 53 + 10)
    # turn 90 degeres
    # r.spinLeftToAngle(100, -180)
    r.SpinLeftAngularDistance(50, 90)
    # go foward up to slide
    r.driveForwardCms(300, 22)
    # turn so parallel with slide
    #r.spinLeftToAngle(100, -210)
    r.SpinLeftAngularDistance(50, 30)
    # extend the arm to shove the dude down the slide
    # r.runTopMotors(200, 120)
    # r.leftTopMotor.run_angle(-50, 68, Stop.BRAKE, True)
    r.leftTopMotor.run_angle(-50, 75, Stop.BRAKE, True)
    # r.leftTopMotor.run(-1)
    r.driveForwardCms(100, 13)
    r.leftTopMotor.run_time(-500, 1000, Stop.COAST, True)
    # self.leftMotor.run_time(leftPower, msecs, Stop.COAST, False)
    # GO HOME!!!!  push the guy with us
    r.driveForwardCms(900, 80)
    # r.spinRight(400, 45)
    # r.driveForwardCms(700, 25)

    
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



# setup robot, back to wall, left side on edge of mat, and i was here
def cubesInTheBench2():
    r = Robot()
    r.driveStraightCms(200, 43)
    r.spinLeftToAngle(100, -45)
    r.driveStraightCms(100, 5)
    r.spinRightToAngle(100, 10)
    # push up against bar ready to drop into left sides hole
    r.moveForTime(75, 75, 600)
    
    # drop a cube, then move to the next hole on the right
    for i in range(2):

        # DROPcube(r)
        DROPcube(r)

        # back up, and get set up for dropping next ones
        r.driveForwardCms(-100, 10)
        r.spinRightToAngle(100, 90)
        r.driveStraightCms(100, 6.0)
        r.spinLeftToAngle(100, 10)
        r.driveStraightCms(100, 10)
# DROPcube(r)
    DROPcube(r)

    # back up, and get set up for dropping next ones
    r.driveForwardCms(-100, 10)
    r.spinRightToAngle(100, 90)
    r.driveStraightCms(100, 8.0)
    r.spinLeftToAngle(100, 10)
    r.driveStraightCms(100, 10)

    DROPcube(r)
    r.driveForwardCms(-200, 40)


def basketLift():
    r=Robot()

    # Here is one option:
    #front right corner of robot lines up with the back of the 2nd E in leauge 

    # but instead, we'll set up like this:
    #setup robot at a set angle(jig)
    #drive straight a bit past bench
    r.driveStraightCms(500, 50)
    #spin left until the back is facing the wall
    r.spinLeftToAngle(250, -135)
    #Back up and line up with the wall
    r.moveForTime(-400, -400, 2000)
    r.gyro.reset_angle(0)
    #drive forward a little bit and spin to the left 90 degrees
    r.driveStraightCms(500, 10)
    r.spinLeftToAngle(150, -90)
    #back up 
    r.moveForTime(-400, -400, 1500)
    #drive forward
    r.driveStraightCms(300, 40)
    #spin left until arm is under basketball hoop
    # TBF: spin for time!!! this will make sure bar is under basket
    r.moveForTime(150, -150, 1000)
    #r.spinLeftToAngle(150, -120)
    # r.driveStraightCms(300, 4.5)
    r.moveForTime(300, 300, 1000)

    #raise :-)
    #r.runTopMotors(-1000, 30*360)
    r.leftTopMotor.run_time(1000, 8000, Stop.COAST, True)
    brick.sound.beep()
    r.leftTopMotor.run_time(-1000, 4000, Stop.COAST, True)

    #r.moveForTime(-150, 150, 600)
    #r.leftTopMotor.run_time(1000, 6000, Stop.COAST, True)
    #straghten out!!!!!!!!!!!!!
    r.spinRightToAngle(200, -90)
    #GO backWARDS to HOME!!!
    r.driveForwardCms(-500, 70)

# This launch knocks down the bench, removes the bar, puts cubes in the spaces, 
# and puts Sabastion and the health units in the grey area!
# ---------------------
# Set up the BOT with the left side of attachment against the THICK black stsaight line 
# The back of the bot should be against the the wood
def benchAll():
    r = Robot()
    # keep pushing the arm down so attachment does NOT move
    # r.rightTopMotor.run(-100) dos'nt work :-( 
    r.driveStraightCms(150, 35)
    brick.sound.beep()
    r.spinRightToAngle(150, 5)
    # r.SpinRightAngularDistance(150, 7)
    brick.sound.beep()
    r.moveForTime(100, 100, 1000)
    brick.sound.beep()
    # this should knock down the bench and release the bar
    r.spinLeftToAngle(150, -4)
    brick.sound.beep()
    r.spinRightToAngle(150, 5)
    power = 100
    r.moveForTime(power, power + 200, 1000)
    # Release the attachment
    r.runTopMotors(1000, 75)
    r.rightTopMotor.run(300)
    brick.sound.beep()
    r.driveForwardCms(-300, 30)
    brick.sound.beep()
    # stop top motor
    r.rightTopMotor.run(0)

# This is for mission 8
# set up the bot w/ ye tri-angle jig
def BASKETbocci():
    r = Robot()
    # when we used the big jig
    # r.driveStraightCms(500, 47.5)
    # r.spinLeftToAngle(50, -44)
    # r.driveStraightCms(500, 32)

    r.driveStraightCms(500, 47.5 + 10)
    r.spinLeftToAngle(50, -43) # in theory, 45?
    r.driveStraightCms(200, 8)
    brick.sound.beep()
    r.spinLeftToAngle(100, -90)
    r.driveStraightCms(200, 26)
    # aadded 2 cms no test yet
    r.moveForTime(-50, 50, 500)
    r.runTopMotors(300, 180)