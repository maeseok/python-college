import time
from cs1robots import*
load_world("./worlds/add34.wld")
def turn_right():
  for i in range(3):
    hubo.turn_left()
def turn_around():
  for i in range(2):
    hubo.turn_left()
hubo = Robot()
hubo.turn_left()
hubo.move()
turn_right()
tmp=0
def pick(tmp):
    while(1):
        if hubo.on_beeper():
            hubo.pick_beeper()
            tmp+=1
        else:
            break
    return tmp

cnt=0
while(1):
    if not hubo.front_is_clear():
        turn_right()
        break
    hubo.move()

for _ in range(5):
    tmp=pick(tmp)
    hubo.move()
    tmp=pick(tmp)
    if tmp>=10:
        tmp-=10
        cnt+=1
    for _ in range(tmp):
        hubo.drop_beeper()
    tmp=cnt
    cnt=0
    turn_right()
    hubo.move()
    turn_right()
    hubo.move()
    turn_around()