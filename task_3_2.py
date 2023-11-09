import time
from cs1robots import *
create_world(avenues=10,streets=10)
hubo=Robot(orientation='N', avenue=2, street=1)
hubo.set_trace("blue")

def turn_right():
    for _ in range(3):
        hubo.turn_left()
def turn_around():
    for _ in range(2):
        hubo.turn_left()

def ori():
    for i in range(4):
        if hubo.facing_north():
            return i
        else:
            hubo.turn_left()
def ave():
    for i in range(10):
        if not hubo.front_is_clear():
            y= 10-i
            turn_around()
            for j in range(i):
                hubo.move()
            turn_around()
            return y
        else:
            hubo.move()   

def sol():
    z = ori()
    y = ave()
    turn_right()
    x = ave()
    hubo.turn_left()
    if z==0:
        z="N"
    elif z==1:
        z="E"
    elif z==2:
        z="S"
    elif z==3:
        z="W"
    print(z,x,y)
sol()
