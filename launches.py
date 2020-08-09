from Robot import Robot

def pullUpBar():
    r = Robot()
    r.driveForwardCms(500, 106-11)
    r.spinRight(250, 120)
    r.driveForwardCms(-500, 23)
    r.runTopMotors(-500, 7*360)