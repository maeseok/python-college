from cs1robots import*
import time

load_world("./worlds/harvest1.wld")
hubo = Robot()
#이동한 위치 기록
hubo.move()
hubo.turn_left()

def turn_right():
  hubo.turn_left()
  hubo.turn_left()
  hubo.turn_left()
  
def harvest_1():
    for _ in range(5):
        hubo.pick_beeper()
        hubo.move()
        time.sleep(0.1)
    hubo.pick_beeper()
    turn_right()
    hubo.move()
    turn_right()
def harvest_2():
    for _ in range(5):
        hubo.pick_beeper()
        hubo.move()
        time.sleep(0.1)
    hubo.pick_beeper()
    hubo.turn_left()
    hubo.move()
    hubo.turn_left()
    
for _ in range(3):
    harvest_1()
    harvest_2()