import time
from cs1robots import*
load_world("./worlds/harvest3.wld")
hubo = Robot(beepers=10)
hubo.set_trace("blue")
hubo.move()
def turn_right():
  for i in range(3):
    hubo.turn_left()
for i in range(6):
    for j in range(5):
        hubo.move()
        if not hubo.on_beeper():
            hubo.drop_beeper()
    if i==5:
        break
    if i%2==0:
        hubo.turn_left()
        hubo.move()
        if not hubo.on_beeper():
            hubo.drop_beeper()
        hubo.turn_left()
    else:
        turn_right()
        hubo.move()
        if not hubo.on_beeper():
            hubo.drop_beeper()
        turn_right()

        