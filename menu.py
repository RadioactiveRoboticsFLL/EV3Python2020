from pybricks import ev3brick as brick
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
  
from launches import pullUpBar, bocciBench, stepCOUNTER, basketLift, benchAll
from launches import treadmill, blueTriangle, Bocci, bocciPlainBocci, innovationbench, bocciOtherTable, BASKETbocci

# displays which button runs each launch
def displayMENU():
    # top left center bottom right
    brick.display.text("")
    brick.display.text("TOP == bocciPlainBocci")
    brick.display.text("LEFT == benchAll")
    brick.display.text("CENTER == blueTriangle")
    brick.display.text("RIGHT == pullUpBar")
    brick.display.text("BOTTOM == BocciOtherTable")

# the menu fuction allows you to choose what
# launch to do
def menu():

    displayMENU()

    btns = brick.buttons()

    while True:
        if len(btns) == 1:
            btn = btns[0]
            if btn == Button.LEFT:
                benchAll()
            elif btn == Button.RIGHT:
                pullUpBar()
            elif btn == Button.UP:    
                bocciPlainBocci()
            elif btn == Button.DOWN:
                bocciOtherTable()
                # BASKETbocci()
                # basketLift()
            elif btn == Button.CENTER:
                blueTriangle()
                # stepCOUNTER()
            brick.display.clear()
            displayMENU()

        btns = brick.buttons()