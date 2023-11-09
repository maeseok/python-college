import time
from cs1robots import*

load_world("./worlds/hurdles4.wld")

def turn_right():
    for _ in range(3):
        hubo.turn_left()
def move():
    cnt=0
    while(not hubo.right_is_clear()):
        hubo.move()
        cnt+=1
    return cnt
  
hubo = Robot()
hubo.set_trace("blue")

while(not hubo.on_beeper()):
    if(not hubo.front_is_clear()):
        hubo.turn_left()
        cnt = move()
        turn_right()
        hubo.move()
        turn_right()
        for _ in range(cnt):
            hubo.move()
        hubo.turn_left()
    else:
        hubo.move()
