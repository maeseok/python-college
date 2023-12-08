import time
from cs1robots import*
n=9
create_world(avenues=n, streets=n)
hubo = Robot(beepers=n*n)
hubo.set_trace("blue")
hubo.drop_beeper()
def turn_right():
  for i in range(3):
    hubo.turn_left()
def Move():
    for i in range(n-1):
        hubo.move()
        hubo.drop_beeper()
Move()
hubo.turn_left()
cnt=0
while(n!=0):
    if(cnt%2==0 and cnt!=0):
        n-=1
    Move()
    cnt+=1
    hubo.turn_left()