import time
from cs1robots import*
load_world("./worlds/harvest3.wld")
hubo = Robot()
hubo.set_trace("blue")
hubo.move()
hubo.pick_beeper()
def turn_right():
  for i in range(3):
    hubo.turn_left()
for i in range(6):
    for j in range(5):
        hubo.move()
        if hubo.on_beeper():
            hubo.pick_beeper()
    if i==5:
        break
    if i%2==0:
        hubo.turn_left()
        hubo.move()
        if hubo.on_beeper():
            hubo.pick_beeper()
        hubo.turn_left()
    else:
        turn_right()
        hubo.move()
        if hubo.on_beeper():
            hubo.pick_beeper()
        turn_right()

        