# 04 display

import time
import game
# from 문서이름 import 전역변수, 함수이름만
from game import user_id,user_pwd

print('03play.py')
time.sleep(0.3)

print(user_id)
print(user_pwd)


game.terran()
game.lol('LOL')

len = game.bass()
print('현의 수:',len)
print('현의 수:', game.bass)