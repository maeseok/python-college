from cs1robots import*

#9월 14일 + 9월 19일 수업시간 실습

#Task1
create_world()
hubo = Robot()
#이동한 위치 기록
hubo.set_trace("blue")
hubo.turn_left()

def turn_right():
  hubo.turn_left()
  hubo.turn_left()
  hubo.turn_left()

def zigzag():
    for _ in range(9):
        hubo.move()
    turn_right()
    hubo.move()
    turn_right()
    
def zigzag2():
    for _ in range(9):
        hubo.move()
    hubo.turn_left()
    hubo.move()
    hubo.turn_left()

def MAIN():
    for i in range(1,10+1):
        if i==10:
            for _ in range(9):
                hubo.move()
        elif i%2==1:
            zigzag()
        else:
            zigzag2()
MAIN()