import time
from cs1robots import*
create_world()
hubo = Robot()
hubo.set_trace("blue")
def turn_right():
    for _ in range(3):
        hubo.turn_left()
hubo.turn_left()
for i in range(9):
    if i%2==0:
        for i in range(9):
            hubo.move()
        turn_right()
        hubo.move()
        turn_right()
    else:
        for i in range(9):
            hubo.move()
        hubo.turn_left()
        hubo.move()
        hubo.turn_left()
for _ in range(9):
    hubo.move()

            