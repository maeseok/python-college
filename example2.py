import time
from cs1robots import*

load_world("./worlds/amazing1.wld")
hubo = Robot(beepers = 1)
print(hubo.on_beeper()) #F
print(hubo.carries_beepers()) #T

hubo.drop_beeper()
print(hubo.on_beeper()) #T
print(hubo.carries_beepers())#F
print(hubo.facing_north()) #F

hubo.turn_left()
print(hubo.facing_north()) #T
print(hubo.front_is_clear()) #T

hubo.turn_left()
print(hubo.front_is_clear()) #F