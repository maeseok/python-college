import time
from cs1robots import*
load_world("./worlds/newspaper.wld")
hubo = Robot(beepers=1)
hubo.set_trace("blue")
hubo.move()
def turn_right():
  for i in range(3):
    hubo.turn_left()
def turn_around():
  for i in range(2):
    hubo.turn_left()
for _ in range(4):
    hubo.turn_left()
    hubo.move()
    turn_right()
    hubo.move()
    hubo.move()
hubo.drop_beeper()
turn_around()
for _ in range(4):
    hubo.move()
    hubo.move()
    hubo.turn_left()
    hubo.move()
    turn_right()
hubo.move()
    