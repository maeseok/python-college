import time
from cs1robots import*
def turn_right():
  hubo.turn_left()
  hubo.turn_left()
  hubo.turn_left()
#create_world(streets=7, avenues=9)
load_world("./worlds/hurdles3.wld")
hubo=Robot()
hubo.set_trace("blue")
hubo.turn_left()
hubo.move()
turn_right()
hubo.move()
def MAIN():
    while(True):
        if hubo.right_is_clear():
            turn_right()
            hubo.move()
            if hubo.on_beeper():
                break
        elif hubo.left_is_clear():
            hubo.turn_left()
            hubo.move()
            if hubo.on_beeper():
                break
        elif not hubo.front_is_clear():
            hubo.turn_left()
            hubo.turn_left()
            hubo.move()
        

    hubo.pick_beeper()
    hubo.turn_left()
MAIN()