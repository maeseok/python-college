import time
from cs1robots import*

load_world("./worlds/hurdles1.wld")
hubo = Robot()
hubo.set_trace("blue")
def turn_right():
    for _ in range(3):
        hubo.turn_left()
hubo.move()
for _ in range(4):
    hubo.turn_left()
    hubo.move()
    turn_right()
    hubo.move()
    turn_right()
    hubo.move()
    hubo.turn_left()
    hubo.move()
hubo.pick_beeper()