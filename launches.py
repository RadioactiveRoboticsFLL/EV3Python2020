from pybricks.tools import wait, print
from Robot import Robot

def pullUpBar():
    r = Robot()
    r.driveStraightCms(500, 106-15)
    r.spinRightToAngle(250, 90)
    # r.driveForwardCms(500, 106-11)
    # r.spinRight(250, 120)
    wait(1000)
    r.driveForwardCms(-500, 29)
    r.runTopMotors(-500, 7*360)