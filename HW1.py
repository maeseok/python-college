import time
from cs1robots import*

def Move():
    for i in range(n-1):
        hubo.move()
        hubo.drop_beeper()
        
n=9
create_world(avenues=n,streets=n)
hubo=Robot(beepers=n**2)
hubo.set_trace("blue")
hubo.drop_beeper()

Move()
hubo.turn_left()
cnt=0
while(n!=0):
    if(cnt%2==0 and cnt!=0):
        n-=1
    Move()
    hubo.turn_left()
    cnt+=1