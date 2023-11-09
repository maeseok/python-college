import time
from cs1robots import*
load_world("./worlds/harvest4.wld")
hubo = Robot(beepers=10)
hubo.set_trace("blue")
hubo.move()
hubo.pick_beeper()
cnt=0
def turn_right():
  for i in range(3):
    hubo.turn_left()
def pick():
    while(1):
        if not hubo.on_beeper():
            break
        hubo.pick_beeper()
for i in range(7):
    for j in range(5):
        hubo.move()
        pick()
    if i==6:
        try:
            while(1):
                hubo.drop_beeper()
                cnt+=1
        except:
            break
    if i%2==0:
        hubo.turn_left()
        hubo.move()
        pick()
        hubo.turn_left()
    else:
        turn_right()
        hubo.move()
        pick()
        turn_right()
print(cnt)
        