from cs1robots import*
import time

load_world("./worlds/harvest4.wld")
hubo = Robot()
hubo.move()
cnt=0
number=0
def turn_right():
  hubo.turn_left()
  hubo.turn_left()
  hubo.turn_left()
def Move(cnt):
    while(1):
        if(hubo.on_beeper()):
            hubo.pick_beeper()
        else:
            if(not hubo.front_is_clear()):
                cnt+=1
                if cnt==7:
                    break
                elif cnt%2==0:
                    turn_right()
                    hubo.move()
                    turn_right()
                else:
                    hubo.turn_left()
                    hubo.move()
                    hubo.turn_left()
                    if(hubo.on_beeper()):
                        hubo.pick_beeper()
            hubo.move()
            time.sleep(0.1)
Move(cnt)
while(1):
    try:
        hubo.drop_beeper()
        time.sleep(0.1)
        number+=1
    except:
        break            
print(number)