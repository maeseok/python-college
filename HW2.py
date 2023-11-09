from cs1robots import*
import time

def turn_right():
    for _ in range(3):
        hubo.turn_left()
def turn_around():
    for _ in range(2):
        hubo.turn_left()
def check_window():
    ans=0
    turn_right()
    hubo.move()
    if hubo.front_is_clear() & hubo.right_is_clear() & hubo.left_is_clear():
        ans=1
    turn_around()
    hubo.move()
    turn_right()
    if ans==1:
        hubo.move()
        if not hubo.right_is_clear():
            ans=1
        else:
            ans=0
        turn_around()
        hubo.move()
        turn_around()
    return ans

def cir_move(position):
    while(1):
        if hubo.right_is_clear() & hubo.front_is_clear():
            ans = check_window()
            if position==hubo.get_pos():
                hubo.move()
            elif ans==1:
                hubo.drop_beeper()
                hubo.move()
            else:
                turn_right()
                hubo.move()
        elif hubo.front_is_clear() :
            hubo.move()
            time.sleep(0.1)
        elif hubo.left_is_clear():
            hubo.turn_left()
            hubo.move()
            time.sleep(0.1)
        else:
            turn_right()
            hubo.move()
        if position==hubo.get_pos():
            break

load_world("./worlds/rain2.wld")
hubo=Robot(orientation='E', avenue=2, street=6, beepers=30)
hubo.move()
turn_right()
position = hubo.get_pos()
cir_move(position)
turn_right()
