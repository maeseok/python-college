from cs1robots import *
load_world("./worlds/newspaper.wld")

hubo = Robot(beepers = 1)

def turn_right():
#3번 돌면 현재 방향의 오른쪽으로 돌게된다.
  hubo.turn_left()
  hubo.turn_left()
  hubo.turn_left()


def turn_around():
#총 4방향으로 구성되기에 2방향을 변환하면 반대 방향으로 전환된다.
  hubo.turn_left()
  hubo.turn_left()
  
def climb_up_onestair():
  hubo.turn_left()
  hubo.move()
  turn_right()
  hubo.move()
  hubo.move()

def climb_down_onestair():
  hubo.move()
  hubo.move()
  hubo.turn_left()
  hubo.move()
  turn_right()
    

def climb_up_fourstairs():
    for i in range(4):
        climb_up_onestair()


def climb_down_fourstairs():
    for i in range(4):
        climb_down_onestair()
    
#계단 4번 올라감
#climb_up_fourstairs()
#비퍼(원) 놓고옴
#hubo.drop_beeper()
#반대쪽으로 방향 전환
#turn_around()
#계단 4번 내려옴
#climb_down_fourstairs()

