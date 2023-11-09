import time
from cs1robots import*

load_world("./worlds/rain2.wld")

def turn_right():
    for _ in range(3):
        hubo.turn_left()
def turn_around():
    for _ in range(2):
        hubo.turn_left()
def window():
    cnt=0
    hubo.move()
    if(not hubo.left_is_clear()):
        cnt=1
    turn_around()
    hubo.move()
    turn_around()
    if cnt==1:
        hubo.turn_left()
        hubo.move()
        if hubo.front_is_clear and hubo.right_is_clear and hubo.left_is_clear:
            hubo.drop_beeper()
        else:
            cnt=0
        turn_around()
        hubo.move()
        hubo.turn_left()
    return cnt

hubo = Robot(orientation="E",avenue=2,street=6,beepers=10)
turn_right()
hubo.drop_beeper()
hubo.move()

while(not hubo.on_beeper()):
    if hubo.left_is_clear() and hubo.front_is_clear():
        cnt=window()
        if cnt==1:
            hubo.move()
        else:
            hubo.turn_left()
            hubo.move()
    elif hubo.front_is_clear():
        hubo.move()
    elif hubo.right_is_clear():
        turn_right()
        hubo.move()
    else:
        hubo.turn_left()
        hubo.move()
    time.sleep(0.1)
hubo.turn_left()
