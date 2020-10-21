from pybricks import ev3brick as brick
from pybricks.tools import wait, print
from Robot import Robot

def pullUpBar():
    r = Robot()
    r.driveStraightCms(500, 106-15)
    brick.sound.beep()
    r.spinRightToAngle(250, 90)
    # r.driveForwardCms(500, 106-11)
    # r.spinRight(250, 120)
    wait(1000)
    r.driveForwardCms(-500, 33)
    r.runTopMotors(-500, 7.5*360)

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

    # This v will get us on top, but we want to stop.
    # r.driveStraightCms(600, 172)
    r.driveStraightCms(600, 172 - 25)
    r.driveForwardCms(600, 10)
    #onTopOfTreadmill!!!!!!!!
    #turn on one (right) motor
    r.rightMotor.run_time(256, 5000)
    # Get off!!!
    r.driveForwardCms(-600, 25)
    # Straiten out!!
    gyroAngle = r.gyro.angle()
    if gyroAngle > 0:
        r.spinLeftToAngle(100, 0)
    else:
        r.spinRightToAngle(100, 0)
    # To Home!!!!!
    # r.driveStraightCms(-650, 150) this does not work.
    # to go backwards, just give it neg. power
    r.driveForwardCms(-650, 150)

def Bocci():
    # This dumps Sabastion and heath units at bench.
    r = Robot()
    r.driveStraightCms(500, 30)
    #DUMP!! Sabastion and the health units.
    r.runTopMotors(500, 90)
    # r.driveStraightCms(200, 5)
    r.spinLeftToAngle(150, -90)
    r.driveStraightCms(500, 40)