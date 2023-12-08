import time
from cs1robots import*

def turn_right():
    for _ in range(3):
        hubo.turn_left()

def turn_around():
    for _ in range(2):
        hubo.turn_left()
def check():
    ans=0
    hubo.move()
    if not hubo.right_is_clear():
        ans=1
    turn_around()
    hubo.move()
    turn_around()
    if ans==1:
        turn_right()
        hubo.move()
        if hubo.right_is_clear() and hubo.left_is_clear() and hubo.front_is_clear():
            pass
        else:
            ans=0
        turn_around()
        hubo.move()
        turn_right()
    return ans
load_world("./worlds/rain2.wld")
hubo= Robot(orientation='E',avenue=2,street=6,beepers=20)
hubo.move()
hubo.drop_beeper()
turn_right()
hubo.move()

while(not hubo.on_beeper()):
    if hubo.right_is_clear() & hubo.front_is_clear():
        ans = check()
        if ans==1:
            hubo.drop_beeper()
        else:
            turn_right()
        hubo.move()
    elif hubo.front_is_clear():
        hubo.move()
    elif hubo.left_is_clear():
        hubo.turn_left()
    else:
        turn_right()
turn_right()