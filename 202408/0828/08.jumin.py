# 08 jumin

import datetime
import time

jumin = '950327-1649753'

# 12시 15분 split() 사용
# 문제 1. 성별 check
# 문제 2. 생일 3월 27일 HBD!!
# 문제 3. 나이계산 2024 - 1995

# # x = datetime.now()
# y = datetime.datetime.now()
# print(y)
# print(str(y))
# z = str(y)
# print(z[0:4])

# 

dt = datetime.datetime.now()
print(dt.strftime('%Y년-%m월-%d일'))
print(dt.strftime('%H시-%M분-%S초'))

a_time = time.localtime()
print(a_time)
print(a_time.tm_year)