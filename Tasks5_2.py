import time
from cs1robots import *
load_world("./worlds/add1.wld")
hubo = Robot()
cnt=0
ans=0
def turn_right(robot):
 for i in range(3):
  robot.turn_left()
def move():
    while(1):
        if not hubo.front_is_clear():
            break
        hubo.move()
def pick_up(cnt):
    cnt=0
    while(1):
        if hubo.on_beeper():
            hubo.pick_beeper()
            cnt+=1
        else:
            turn_right(hubo)
            hubo.move()
            break
    return cnt
def pick_down(cnt,ans):
    while(1):
        if hubo.on_beeper():
            hubo.pick_beeper()
            cnt+=1
        else:
            break
    if ans!=0:
        cnt+=ans
        ans=0
    if cnt>=10:
        cnt-=10
        ans+=1
    for _ in range(cnt):
        hubo.drop_beeper()
    hubo.turn_left()
    hubo.turn_left()
    hubo.move()
    hubo.turn_left()
    hubo.move()
    hubo.turn_left()
    hubo.turn_left()
    return ans

hubo.turn_left()
hubo.move()
turn_right(hubo)
move()
for _ in range(5):
    cnt = pick_up(cnt)
    ans= pick_down(cnt,ans)