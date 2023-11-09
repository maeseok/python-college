from cs1robots import*

#9월 14일 + 9월 19일 수업시간 실습

#Task2
load_world("./worlds/hurdles1.wld")
hubo = Robot()
#이동한 위치 기록
hubo.turn_left()


def turn_right():
  hubo.turn_left()
  hubo.turn_left()
  hubo.turn_left()

def hurdle():
    hubo.move()
    hubo.turn_left()
    hubo.move()
    turn_right()
    hubo.move()
    turn_right()
    hubo.move()
    hubo.turn_left()
    
def hurdle2():
    for _ in range(9):
        hubo.move()
    hubo.turn_left()
    hubo.move()
    hubo.turn_left()

def MAIN():
    for _ in range(4):
        hurdle()
turn_right()
hubo.set_trace("blue")
MAIN()
hubo.move()
hubo.pick_beeper()