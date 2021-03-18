from pybricks import ev3brick as brick
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
# :-)   
from launches import pullUpBar, bocciBench, stepCOUNTER, basketLift
from launches import treadmill, blueTriangle, Bocci, bocciPlainBocci, innovationbench, bocciOtherTable

# displays which button runs each launch
def displayMENU():
    # top left center bottom right
    brick.display.text("")
    brick.display.text("TOP == bocciPlainBocci")
    brick.display.text("LEFT == innavationBench")
    brick.display.text("CENTER == blueTriangle")
    brick.display.text("BOTTOM == bocciOtherTable")
    brick.display.text("RIGHT == pullUpBar")

# the menu fuction allows you to choose what
# launch to do
def menu():

    displayMENU()

    btns = brick.buttons()

    while True:
        if len(btns) == 1:
            btn = btns[0]
            if btn == Button.LEFT:
                innovationbench()
            elif btn == Button.RIGHT:
                pullUpBar()
            elif btn == Button.UP:    
                bocciPlainBocci()
            elif btn == Button.DOWN:
                bocciOtherTable()
                # basketLift()
            elif btn == Button.CENTER:
                blueTriangle()
                # stepCOUNTER()
            brick.display.clear()
            displayMENU()

        btns = brick.buttons()