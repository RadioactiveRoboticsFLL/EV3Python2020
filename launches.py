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