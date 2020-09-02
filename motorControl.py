# pybrick imports
from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import wait, print


def motorControl():


    # left, right: motor1
    # up, down: motor2

    motor1 = Motor(Port.A)
    motor2 = Motor(Port.D)

    speed = 500

    while True:
        btn = None
        btns = brick.buttons()
        if len(btns) == 0:
            motor1.stop()
            motor2.stop()
            continue
        if len(btns) == 1:   
            btn = btns[0]
            print("button:", btn)

            if btn == Button.LEFT:
                motor1.run(-speed)
                motor2.stop()
            elif btn == Button.RIGHT:
                motor1.run(speed)
                motor2.stop()
            elif btn == Button.DOWN:
                motor1.stop()
                motor2.run(-speed)    
            elif btn == Button.UP:
                motor1.stop()
                motor2.run(speed)        
            else:
                motor1.stop()
                motor2.stop()
        if len(btns) == 2:
            pass   