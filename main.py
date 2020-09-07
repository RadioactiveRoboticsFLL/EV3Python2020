#!/usr/bin/env pybricks-micropython

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

r = Robot()

# do a quick menu
r.gyroDriftCheck()
btns = brick.buttons()

brick.display.text("")
brick.display.text("LEFT == motorControl")
brick.display.text("RIGHT == pullUpBars")
brick.display.text("CENTER == bocciBench")
while True:
    if len(btns) == 1:
        btn = btns[0]
        if btn == Button.LEFT:
            motorControl()
        elif btn == Button.RIGHT:
            pullUpBar()
            # r.driveStraightCms(500, 100)
        elif btn == Button.UP:    
            r.runTopMotors(500, 6*360)
        elif btn == Button.DOWN:
            r.runTopMotors(-500, 6*360)
        elif btn == Button.CENTER:
            bocciBench()

    btns = brick.buttons()


# test 