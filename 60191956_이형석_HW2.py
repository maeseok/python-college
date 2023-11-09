import time
from cs1robots import*

def turn_right():
  for i in range(3):
    hubo.turn_left()
    
def turn_around():
  for i in range(2):
    hubo.turn_left() 
    
def window():
    cnt=0
    hubo.move()
    if(not hubo.right_is_clear()):
        cnt=1
    turn_around()
    hubo.move()
    turn_around()
    if cnt==1:
        turn_right()
        hubo.move()
        if hubo.front_is_clear and hubo.right_is_clear and hubo.left_is_clear:
            pass
        else:
            cnt=0
        turn_around()
        hubo.move()
        turn_right()
    return cnt

load_world("./worlds/rain2.wld")   
hubo = Robot(orientation="E",avenue=2,street=6,beepers=10)
hubo.move()
hubo.drop_beeper()
turn_right()
hubo.move()
while(not hubo.on_beeper()):
    if hubo.right_is_clear() and hubo.front_is_clear():
        cnt=window()
        if cnt==1:
            hubo.drop_beeper()
            hubo.move()
        else:
            turn_right()
            hubo.move()
    elif hubo.front_is_clear():
        hubo.move()
    elif hubo.left_is_clear():
        hubo.turn_left()
        hubo.move()
    else:
        turn_right()
        hubo.move()
    time.sleep(0.1)
turn_right()