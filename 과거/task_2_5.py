import time
from cs1robots import*
m=10
n=20
create_world(streets=m, avenues=n)
hubo = Robot(beepers=10)
hubo.set_trace("blue")
hubo.turn_left()
def turn_right():
  for i in range(3):
    hubo.turn_left()

for i in range(n):
    for j in range(m-1):
        hubo.move()
    if i==n-1:
        break
    if(i%2==0):
        turn_right()
        hubo.move()
        turn_right()
    else:
        hubo.turn_left()
        hubo.move()
        hubo.turn_left()