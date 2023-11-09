import time
from cs1robots import*
load_world("./worlds/harvest4.wld")
hubo = Robot(beepers=10)
hubo.set_trace("blue")
hubo.move()
hubo.pick_beeper()
def turn_right():
  for i in range(3):
    hubo.turn_left()
def pick():
    while(1):
        if not hubo.on_beeper():
            break
        hubo.pick_beeper()
for i in range(6):
    for j in range(5):
        hubo.move()
        pick()
    if i==5:
        break
    if i%2==0:
        hubo.turn_left()
        hubo.move()
        pick()
        hubo.turn_left()
    else:
        turn_right()
        hubo.move()
        pick()
        turn_right()

        