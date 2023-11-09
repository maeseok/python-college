import time
from cs1robots import*

load_world("./worlds/newspaper.wld")

#비퍼의 개수 1개
hubo = Robot(beepers = 1)
#이동한 위치 기록
hubo.set_trace("blue")

def turn_right():
  hubo.turn_left()
  hubo.turn_left()
  hubo.turn_left()

def turn_around():
  hubo.turn_left()
  hubo.turn_left()

def climb_up_four_stairs():
  for i in range(4):
    climb_up_one_stair()
    time.sleep(0.5)   

def climb_down_four_stairs():
  for i in range(4):
    climb_down_one_stair()
    time.sleep(0.5)   

def climb_up_one_stair():
  hubo.turn_left()
  hubo.move()
  turn_right()
  hubo.move()
  hubo.move()

def climb_down_one_stair():
  hubo.move()
  hubo.move()
  hubo.turn_left()
  hubo.move()
  turn_right()


climb_up_four_stairs()
#초기 비퍼가 0개이면 에러가 발생
hubo.drop_beeper()
#비퍼를 주움
hubo.pick_beeper()
turn_around()
climb_down_four_stairs()