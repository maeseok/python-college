from cs1robots import*
import time

create_world(avenues=10, streets=10)
hubo=Robot(orientation='S', avenue=2, street=1)


def turn_right():
  hubo.turn_left()
  hubo.turn_left()
  hubo.turn_left()
  
def north():
    cnt=0
    while(1):
        if hubo.facing_north():
            break
        else:
            hubo.turn_left()
            cnt+=1
    if cnt==0:
        return cnt,"N"
    elif cnt==1:
        return cnt,"E"
    elif cnt==2:
        return cnt,"S"
    elif cnt==3:
        return cnt,"W"

def Street():
    cnt=0
    while(1):
        if not hubo.front_is_clear():
            break
        else:
            hubo.move()
            cnt+=1
    hubo.turn_left()
    hubo.turn_left()
    for _ in range(cnt):
        hubo.move()
    hubo.turn_left()
    return 10-cnt

def Avenue():
    cnt=0
    while(1):
        if not hubo.front_is_clear():
            break
        else:
            hubo.move()
            cnt+=1
    hubo.turn_left()
    hubo.turn_left()
    for _ in range(cnt):
        hubo.move()
    turn_right()
    return 10-cnt
cnt,dire=north()
stre=Street()
aven=Avenue()

for _ in range(cnt):
    turn_right()
print(dire,aven,stre)