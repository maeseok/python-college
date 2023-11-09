import time
from cs1robots import*
def turn_right():
  hubo.turn_left()
  hubo.turn_left()
  hubo.turn_left()
m=20
n=30
create_world(streets=m, avenues=n)
hubo=Robot()
hubo.set_trace("blue")
hubo.turn_left()
#n에따라  right left clear
def MAIN(cnt,n):
    while(True):
        if hubo.front_is_clear():
            hubo.move()
        else:
            cnt+=1
            if hubo.right_is_clear() & cnt%2==0:
                turn_right()
                hubo.move()
                turn_right()
            elif hubo.left_is_clear() & cnt%2!=0:
                hubo.turn_left()
                hubo.move()
                hubo.turn_left()
            if cnt==n+1:
                break

MAIN(0,n)