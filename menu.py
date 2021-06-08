from pybricks import ev3brick as brick
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
  
from launches import pullUpBar, bocciBench, stepCOUNTER, basketLift, benchAll, Slide
from launches import treadmill, blueTriangle, Bocci, bocciPlainBocci, innovationbench, bocciOtherTable, BASKETbocci

from pybricks.tools import wait

# displays which button runs each launch
def displayMENU():
    # top left center bottom right
    brick.display.text("")
    brick.display.text("TOP == bocciPlainBocci")
    brick.display.text("LEFT == benchAll")
    brick.display.text("CENTER == blueTriangle")
    brick.display.text("RIGHT == pullUpBar or Slide (submenu)")
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
            elif btn == Button.CENTER:
                blueTriangle()
                
            elif btn == Button.UP:    
                bocciPlainBocci()
            elif btn == Button.DOWN:
                bocciOtherTable()
                # BASKETbocci()
                # basketLift()
            elif btn == Button.RIGHT:
                brick.display.clear()
                brick.display.text("")
                brick.display.text("Left = Slide")
                brick.display.text("Top = PullupBar")
                brick.display.text("Center = Baack")
                
                DoNotExit = True
                while DoNotExit == True:
                    btns = brick.buttons()

                    # exits to main menu if any other key than left or right is pressed
                    if len(btns) == 1:
                        # button pressed! now check witch one it was
                        btn = btns[0]
                        if btn == Button.LEFT or btn == Button.UP:
                            DoNotExit = True
                            if btn == Button.LEFT:
                                Slide()
                            if btn == Button.UP:
                                pullUpBar()
                        else:
                            if btn == Button.CENTER:
                                brick.display.text("EXITING...")
                                wait(3000)
                                # EXIT submenu!
                                DoNotExit = False
                            else:
                                # ignore pressed button
                                DoNotExit = True


                    else:
                        # no buttons or more than 1 buttons pressed
                        DoNotExit = True

                # blueTriangle()
                # stepCOUNTER()
            brick.display.clear()
            displayMENU()

        btns = brick.buttons()