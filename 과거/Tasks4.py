import time
from cs1robots import*

#create_world(streets=7, avenues=9)
load_world("./worlds/hurdles1.wld")
hubo=Robot()
hubo.set_trace("blue")
hubo.move()
def turn_right():
  hubo.turn_left()
  hubo.turn_left()
  hubo.turn_left()

def MAIN():
    while(True):
        hubo.turn_left()
        hubo.move()
        turn_right()
        if hubo.on_beeper():
            break
        hubo.move()
        turn_right()
        if hubo.on_beeper():
            break
        hubo.move()
        hubo.turn_left()
        if hubo.on_beeper():
            break
        hubo.move()
        if hubo.on_beeper():
            break
    hubo.pick_beeper()
MAIN()