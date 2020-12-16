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
from Robot import Robot
from menu import menu

# Create a robot object from our Robot class
# so we can use it's functions
r = Robot()

# This checks for gyro drift which is bad, but can
# be fixed by unplugging/plugging the gyro sensor, which
# it lets you do
r.gyroDriftCheck()

# This lets you access all the launches.
menu()

