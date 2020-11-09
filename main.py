#!/usr/bin/env pybricks-micropython
# :-)

# pybrick imports
from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import wait, print

# our imports
from motion import driveForward,spinRight,spinLeft
from Robot import Robot
from launches import pullUpBar, bocciBench
from motorControl import motorControl
from launches import treadmill, stepCOUNTER, Bocci, bocciPlainBocci, innovationbench, bocciOtherTable
def displayMENU():
    # top left center bottom right
    brick.display.text("")
    brick.display.text("TOP == bocciPlainBocci")
    brick.display.text("LEFT == innavationBench")
    brick.display.text("CENTER == stepCOUNTER")
    brick.display.text("BOTTOM == treadmill")
    brick.display.text("RIGHT == pullUpBar")
r = Robot()

# do a quick menu
r.gyroDriftCheck()
btns = brick.buttons()

displayMENU()
while True:
    if len(btns) == 1:
        btn = btns[0]
        if btn == Button.LEFT:
            # motorControl()
            # stepCOUNTER()
            # Bocci()
            innovationbench()
        elif btn == Button.RIGHT:
            pullUpBar()
            # r.driveStraightCms(500, 100)
        elif btn == Button.UP:    
            # r.runTopMotors(500, 6*360)
            bocciPlainBocci()
        elif btn == Button.DOWN:
            # r.runTopMotors(-500, 6*360)
            treadmill()
            #bocciOtherTable()
        elif btn == Button.CENTER:
            # bocciBench()
            stepCOUNTER()
        brick.display.clear()
        displayMENU()

    btns = brick.buttons()

