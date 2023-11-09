import time
from cs1robots import*
load_world("./worlds/harvest3.wld")
hubo = Robot()
hubo.set_trace("blue")
hubo.move()
hubo.pick_beeper()
def turn_right():
    hubo.turn_left()
    hubo.turn_left()
    hubo.turn_left()
def check():
    if hubo.on_beeper():
        hubo.pick_beeper() 

def move():
    for i in range(6):
        for j in range(5):
            hubo.move()
            check()
            time.sleep(0.2)
        if i%2==0:
            hubo.turn_left()
            hubo.move()
            hubo.turn_left()
            time.sleep(0.2)
            check()
        else:
            if(i!=5):
                turn_right()
                hubo.move()
                turn_right()
                time.sleep(0.2)
                check()
move()       