import time
from cs1robots import*
load_world("./worlds/hurdles3.wld")
hubo = Robot(beepers=10)
hubo.set_trace("blue")

def turn_right():
  for i in range(3):
    hubo.turn_left()

while(not hubo.on_beeper()):
    if not hubo.front_is_clear():
        hubo.turn_left()
        hubo.move()
        turn_right()
        hubo.move()
        turn_right()
        hubo.move()
        hubo.turn_left()
    else:
        hubo.move()
        
    
