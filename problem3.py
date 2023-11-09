import time
from cs1robots import*

avenue = int(input("avenue?"))
street = int(input("street?"))
hubo_avenue = int(input("avenue of hubo?"))
hubo_street = int(input("street of hubo?"))
hubo_ori = input("orientation of hubo?")

def turn_right():
    for _ in range(3):
        hubo.turn_left()

def turn_around():
    for _ in range(2):
        hubo.turn_left()
        
def north():
    for _ in range(4):
        if hubo.facing_north():
            break
        else:
            hubo.turn_left()

def check():
    while(hubo.front_is_clear()):
        hubo.move()
    turn_around()
    cnt=1
    while(hubo.front_is_clear()):
        hubo.move()
        cnt+=1
    return cnt
create_world(avenues=avenue, streets=street)
hubo=Robot(orientation=hubo_ori,avenue=hubo_avenue,street=hubo_street)
north()
y = check()
hubo.turn_left()
x = check()
ans = (x,y)
print(ans)