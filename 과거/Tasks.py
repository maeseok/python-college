import time
from cs1robots import*

#create_world(streets=7, avenues=9)
load_world("./worlds/harvest3.wld")
hubo = Robot()
hubo.set_trace("blue")
#time.sleep(0.5)
hubo.move()
hubo.pick_beeper()
def turn_right():
  for i in range(3):
    hubo.turn_left()
    
for i in range(6):
    if i%2==0:
        for _ in range(5):
            hubo.move()
            if hubo.on_beeper():
                hubo.pick_beeper()
        hubo.turn_left()
        hubo.move()
        if hubo.on_beeper():
            hubo.pick_beeper()
        hubo.turn_left()
    else:
        for _ in range(5):
            hubo.move()
            if hubo.on_beeper():
                hubo.pick_beeper()
        if i!=5:
            turn_right()
            hubo.move()
            if hubo.on_beeper():
                hubo.pick_beeper()
            turn_right()

#hubo.front(left/right)_is_clear()

